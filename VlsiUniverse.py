import os
from datetime import datetime
from dotenv import load_dotenv
import time
import re

# CORRECT IMPORT - Make sure you're using this:
from firecrawl import FirecrawlApp  # NOT from firecrawl import Firecrawl

class VLSIUniverseCrawler:
    def __init__(self):
        load_dotenv()
        # CORRECT INITIALIZATION - Use FirecrawlApp, not Firecrawl
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.results = []
        self.base_url = "https://vlsiuniverse.blogspot.com"
        

    
    def test_connection(self):
        """Test if Firecrawl is properly initialized"""
        print("Testing Firecrawl connection...")
        try:
            # Test with a simple scrape
            result = self.app.scrape(
                self.base_url,
                only_main_content=True
            )
            if result:
                print("✅ Firecrawl connection successful!")
                return True
        except Exception as e:
            print(f"❌ Firecrawl connection failed: {str(e)}")
            return False
    
    def extract_vlsi_blogs(self):
        """Extract all VLSI blog posts and save as markdown"""
        
        print("Starting VLSI Universe blog extraction...")
        
        # Test connection first
        if not self.test_connection():
            print("Please check your FIRECRAWL_API_KEY in .env file")
            return None
        
        # New approach: Get archive pages first, then extract individual posts
        return self.scrape_blog_archive_new()
    
    def scrape_blog_archive_new(self):
        """New approach: Scrape archive pages to find individual blog posts"""
        all_results = []
        
        # Step 1: Get the main page to find archive links
        print("\n📁 Fetching main blog page to find archive links...")
        
        try:
            main_result = self.app.scrape(
                self.base_url,
                only_main_content=False
            )
            
            if hasattr(main_result, 'markdown'):
                content = main_result.markdown
                print(f"✅ Main page scraped successfully")
                
                # Step 2: Extract archive page URLs (year/month pages)
                archive_urls = self.extract_archive_page_urls(content)
                print(f"Found {len(archive_urls)} archive pages")
                
                # Step 3: Process each archive page to get individual post URLs
                for i, archive_url in enumerate(archive_urls, 1):
                    print(f"\n📂 Processing archive page {i}/{len(archive_urls)}: {archive_url}")
                    
                    try:
                        archive_result = self.app.scrape(archive_url, only_main_content=False)
                        
                        if hasattr(archive_result, 'markdown'):
                            archive_content = archive_result.markdown
                            
                            # Extract individual blog post URLs from this archive page
                            post_urls = self.extract_individual_post_urls(archive_content)
                            print(f"   Found {len(post_urls)} individual posts in this archive")
                            
                            # Step 4: Scrape each individual blog post
                            for j, post_url in enumerate(post_urls, 1):
                                if not any(post['url'] == post_url for post in all_results):
                                    print(f"   📝 [{j}/{len(post_urls)}] Scraping: {post_url}")
                                    post_data = self.scrape_individual_post(post_url)
                                    if post_data:
                                        all_results.append(post_data)
                                        print(f"      ✅ Added: {post_data['title'][:50]}...")
                                    time.sleep(1)  # Rate limiting
                        
                        time.sleep(2)  # Rate limiting between archive pages
                        
                    except Exception as e:
                        print(f"   ❌ Error processing archive {archive_url}: {str(e)}")
                        continue
                
                # Also try to get posts directly from main page
                main_post_urls = self.extract_individual_post_urls(content)
                print(f"\n📄 Found {len(main_post_urls)} posts directly on main page")
                
                for i, post_url in enumerate(main_post_urls, 1):
                    if not any(post['url'] == post_url for post in all_results):
                        print(f"📝 [{i}/{len(main_post_urls)}] Scraping from main page: {post_url}")
                        post_data = self.scrape_individual_post(post_url)
                        if post_data:
                            all_results.append(post_data)
                            print(f"   ✅ Added: {post_data['title'][:50]}...")
                        time.sleep(1)
                
        except Exception as e:
            print(f"❌ Error fetching main page: {str(e)}")
            import traceback
            traceback.print_exc()
        
        # Remove duplicates
        unique_results = []
        seen_urls = set()
        for post in all_results:
            if post['url'] not in seen_urls:
                seen_urls.add(post['url'])
                unique_results.append(post)
        
        self.results = unique_results
        return self.save_markdown_results()
    
    def extract_archive_page_urls(self, content):
        """Extract archive page URLs (year/month pages) from main page content"""
        archive_urls = []
        
        # Pattern for archive pages like: https://vlsiuniverse.blogspot.com/2020/06/
        archive_pattern = r'https://vlsiuniverse\.blogspot\.com/(\d{4})/(\d{2})/'
        matches = re.findall(archive_pattern, content)
        
        for year, month in matches:
            url = f"{self.base_url}/{year}/{month}/"
            if url not in archive_urls:
                archive_urls.append(url)
        
        # Also look for archive.html format
        archive_html_pattern = r'https://vlsiuniverse\.blogspot\.com/(\d{4})_(\d{2})_\d{2}_archive\.html'
        html_matches = re.findall(archive_html_pattern, content)
        
        for year, month in html_matches:
            url = f"{self.base_url}/{year}_{month}_01_archive.html"
            if url not in archive_urls:
                archive_urls.append(url)
        
        return archive_urls
    
    def extract_individual_post_urls(self, content):
        """Extract individual blog post URLs from content"""
        post_urls = []
        
        # Pattern for individual blog post URLs
        # Example: https://vlsiuniverse.blogspot.com/2020/06/why-is-sum-of-setup-time-and-hold-time.html
        post_pattern = r'https://vlsiuniverse\.blogspot\.com/\d{4}/\d{2}/[^/\s"\']+\.html'
        matches = re.findall(post_pattern, content)
        
        for match in matches:
            # Clean up the URL (remove any trailing characters)
            clean_url = match.split(')')[0].split('"')[0].split("'")[0]
            if clean_url not in post_urls and 'archive' not in clean_url:
                post_urls.append(clean_url)
        
        # Also look for markdown link format
        markdown_pattern = r'\[([^\]]+)\]\((https://vlsiuniverse\.blogspot\.com/\d{4}/\d{2}/[^)]+\.html)\)'
        md_matches = re.findall(markdown_pattern, content)
        
        for title, url in md_matches:
            if url not in post_urls and 'archive' not in url:
                post_urls.append(url)
        
        return post_urls
    
    def scrape_individual_post(self, url, max_retries=3):
        """Scrape an individual blog post with rate limit handling"""
        for attempt in range(max_retries):
            try:
                # Use only_main_content=False to get full page content
                result = self.app.scrape(url, only_main_content=False)
                
                if hasattr(result, 'markdown'):
                    content = result.markdown
                    
                    # Extract the actual blog post content from the full page
                    blog_content = self.extract_blog_content_from_full_page(content)
                    
                    # Check if we got actual content (not just navigation/translation)
                    if self.is_valid_blog_content(blog_content):
                        return {
                            'url': url,
                            'title': self.extract_title_from_result(result, blog_content),
                            'date': self.extract_date_from_url(url),
                            'year': self.extract_year_from_url(url),
                            'content': blog_content
                        }
                    else:
                        print(f"         ⚠️ Skipping - no valid content found")
                        return None
                    
            except Exception as e:
                if "Rate Limit" in str(e):
                    print(f"         ⏳ Rate limit hit (attempt {attempt + 1}/{max_retries}), waiting 60 seconds...")
                    time.sleep(60)
                    continue
                else:
                    print(f"         ❌ Error: {str(e)[:50]}...")
                    break
        
        return None
    
    def extract_blog_content_from_full_page(self, content):
        """Extract the actual blog content from the full page content"""
        if not content:
            return ""
        
        lines = content.split('\n')
        blog_content_lines = []
        
        # Find the start of the blog content (usually after the title)
        in_blog_content = False
        title_found = False
        
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            
            # Skip navigation and header content
            if any(skip_phrase in line_stripped for skip_phrase in [
                'Go to Blogger.com',
                'Create Blog',
                'Sign In',
                'MoreShare by email',
                'Report Abuse',
                '| --- |',
                'VLSI UNIVERSE'
            ]):
                continue
            
            # Look for the blog title (header with ###)
            if line_stripped.startswith('### ') and not title_found:
                title_found = True
                blog_content_lines.append(line)
                in_blog_content = True
                continue
            
            # If we found the title, collect subsequent content
            if in_blog_content:
                # Stop collecting when we hit footer content
                if any(footer_phrase in line_stripped for footer_phrase in [
                    'Email ThisBlogThis',
                    'Newer Posts',
                    'Older Posts',
                    'Subscribe to:',
                    'Popular Posts',
                    'Motivate me to write more',
                    'paypal',
                    'Blog Archive',
                    'Submit a query',
                    'TOP SITES',
                    'Powered by Blogger'
                ]):
                    break
                
                # Skip comment count lines
                if re.match(r'^\d+\s+comments?:?\s*$', line_stripped):
                    continue
                
                # Add the line if it has substantial content
                if line_stripped:
                    blog_content_lines.append(line)
        
        # If we didn't find a title with ###, try to extract based on content patterns
        if not title_found:
            # Look for any header that might be the title
            for i, line in enumerate(lines):
                line_stripped = line.strip()
                if (line_stripped.startswith('#') and 
                    len(line_stripped) > 5 and 
                    len(line_stripped) < 200 and
                    'VLSI UNIVERSE' not in line_stripped):
                    
                    # Collect content from this point
                    for j in range(i, len(lines)):
                        content_line = lines[j].strip()
                        if any(footer_phrase in content_line for footer_phrase in [
                            'Email ThisBlogThis',
                            'Newer Posts',
                            'Subscribe to:',
                            'Popular Posts',
                            'Powered by Blogger'
                        ]):
                            break
                        if content_line:
                            blog_content_lines.append(lines[j])
                    break
        
        return '\n'.join(blog_content_lines)
    
    def is_valid_blog_content(self, content):
        """Check if the scraped content is actual blog content, not just navigation"""
        if not content or len(content.strip()) < 50:
            return False
        
        # Check if content has substantial text (not just links/navigation)
        lines = content.split('\n')
        substantial_lines = []
        
        for line in lines:
            line_stripped = line.strip()
            # Count lines that have meaningful content
            if (len(line_stripped) > 20 and 
                not line_stripped.startswith('[') and 
                not line_stripped.startswith('|') and
                not line_stripped.startswith('#####') and  # Skip deep headers
                'Original text' not in line_stripped and
                'Rate this translation' not in line_stripped):
                substantial_lines.append(line_stripped)
        
        # Must have at least 2 substantial lines of content
        return len(substantial_lines) >= 2
    
    def extract_title_from_result(self, result, content):
        """Extract title from scrape result"""
        # Try to get from metadata
        if hasattr(result, 'metadata') and hasattr(result.metadata, 'title'):
            title = result.metadata.title
            # Clean common suffixes
            title = title.replace(' - VLSI UNIVERSE', '').replace('VLSI UNIVERSE: ', '')
            return title.strip()
        
        # Extract from content
        return self.extract_title_from_content(content)
    
    def extract_title_from_content(self, content):
        """Extract title from content"""
        if not content:
            return 'Untitled'
        
        lines = content.split('\n')
        for line in lines[:10]:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
            elif line and not line.startswith('#') and len(line) > 10 and len(line) < 200:
                # First substantial line might be the title
                return line
        
        return 'Untitled'
    
    def extract_date_from_url(self, url):
        """Extract date from Blogspot URL"""
        # URLs are like: /2025/04/why-clock-gating...
        date_match = re.search(r'/(\d{4})/(\d{2})/', url)
        if date_match:
            year = date_match.group(1)
            month = date_match.group(2)
            return f"{year}-{month}"
        return "Date not found"
    
    def extract_year_from_url(self, url):
        """Extract year from URL"""
        year_match = re.search(r'/(\d{4})/', url)
        if year_match:
            return year_match.group(1)
        return "Unknown"
    

    
    def save_markdown_results(self):
        """Save results to markdown file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'vlsi_universe_all_blogs_{timestamp}.md'
        
        if not self.results:
            print("\n⚠️ No blog posts found")
            return None
        
        # Sort by year and date
        self.results.sort(key=lambda x: (x['year'], x['date']), reverse=True)
        
        self.create_markdown_file(filename)
        
        print(f"\n✅ Extraction completed successfully!")
        print(f"📄 Saved to: {filename}")
        print(f"📊 Total blog posts extracted: {len(self.results)}")
        
        return filename
    
    def create_markdown_file(self, filename):
        """Create markdown file with results grouped by year"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# VLSI Universe - Complete Blog Archive\n\n")
            f.write(f"**Source:** {self.base_url}\n")
            f.write(f"**Extracted on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Total Posts:** {len(self.results)}\n\n")
            f.write("---\n\n")
            
            # Group by year
            posts_by_year = {}
            for post in self.results:
                year = post['year']
                if year not in posts_by_year:
                    posts_by_year[year] = []
                posts_by_year[year].append(post)
            
            # Write table of contents
            f.write("## 📚 Table of Contents\n\n")
            for year in sorted(posts_by_year.keys(), reverse=True):
                count = len(posts_by_year[year])
                f.write(f"- [{year} ({count} posts)](#{year})\n")
            
            f.write("\n---\n\n")
            
            # Write posts grouped by year only (no categories)
            for year in sorted(posts_by_year.keys(), reverse=True):
                f.write(f"## {year}\n\n")
                
                for i, post in enumerate(posts_by_year[year], 1):
                    f.write(f"### {i}. {post['title']}\n\n")
                    f.write(f"**Date:** {post['date']}\n")
                    f.write(f"**URL:** [{post['url']}]({post['url']})\n\n")
                    
                    # Write content
                    f.write(post['content'])
                    f.write("\n\n---\n\n")

# Main execution
if __name__ == "__main__":
    # Make sure you have the correct import at the top!
    print("Checking Firecrawl installation...")
    try:
        from firecrawl import FirecrawlApp
        print("✅ FirecrawlApp imported successfully")
    except ImportError:
        print("❌ Could not import FirecrawlApp")
        print("Try: pip install firecrawl-py --upgrade")
        exit(1)
    
    crawler = VLSIUniverseCrawler()
    
    try:
        markdown_file = crawler.extract_vlsi_blogs()
        
    except Exception as e:
        print(f"\n❌ Extraction failed: {str(e)}")
        import traceback
        traceback.print_exc()