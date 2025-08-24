import os
from datetime import datetime
from dotenv import load_dotenv
import time
import re
import json
from urllib.parse import urljoin, urlparse

# Import FirecrawlApp
from firecrawl import FirecrawlApp

class VLSISystemDesignScraper:
    def __init__(self):
        load_dotenv()
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.results = []
        self.base_url = "https://www.vlsisystemdesign.com"
        self.blogs_url = "https://www.vlsisystemdesign.com/blogs/"
        self.seen_urls = set()
        
    def test_connection(self):
        """Test if Firecrawl is properly initialized"""
        print("Testing Firecrawl connection...")
        try:
            # Test with the main blogs page
            result = self.app.scrape(
                self.blogs_url,
                only_main_content=False
            )
            if result:
                print("✅ Firecrawl connection successful!")
                return True
        except Exception as e:
            print(f"❌ Firecrawl connection failed: {str(e)}")
            return False
    
    def extract_vlsi_blogs(self):
        """Main extraction method"""
        print("Starting VLSI System Design blog extraction...")
        
        # Test connection first
        if not self.test_connection():
            print("Please check your FIRECRAWL_API_KEY in .env file")
            return None
        
        # Start scraping process
        return self.scrape_all_blogs()
    
    def scrape_all_blogs(self):
        """Scrape all blog posts from the site"""
        all_results = []
        
        print("\n📁 Starting blog extraction from VLSI System Design...")
        
        # Step 1: Get all blog listing pages
        blog_listing_urls = self.get_all_blog_listing_pages()
        print(f"Found {len(blog_listing_urls)} blog listing pages")
        
        # Step 2: Extract individual post URLs from each listing page
        all_post_urls = []
        for i, listing_url in enumerate(blog_listing_urls, 1):
            print(f"\n📂 Processing listing page {i}/{len(blog_listing_urls)}: {listing_url}")
            post_urls = self.extract_post_urls_from_listing(listing_url)
            all_post_urls.extend(post_urls)
            time.sleep(2)  # Rate limiting
        
        # Remove duplicates
        unique_post_urls = list(set(all_post_urls))
        print(f"\n📊 Total unique blog posts found: {len(unique_post_urls)}")
        
        # Step 3: Scrape each individual blog post
        for i, post_url in enumerate(unique_post_urls, 1):
            if post_url in self.seen_urls:
                continue
                
            print(f"\n📝 [{i}/{len(unique_post_urls)}] Scraping: {post_url}")
            post_data = self.scrape_individual_post(post_url)
            
            if post_data:
                all_results.append(post_data)
                self.seen_urls.add(post_url)
                print(f"   ✅ Successfully scraped: {post_data['title'][:50]}...")
            else:
                print(f"   ⚠️ Failed to scrape post")
            
            # Rate limiting
            time.sleep(3)
        
        self.results = all_results
        return self.save_results()
    
    def get_all_blog_listing_pages(self):
        """Get all blog listing pages (pagination)"""
        listing_pages = [self.blogs_url]
        
        # Start with the main blogs page
        print("\n🔍 Discovering blog listing pages...")
        
        try:
            # Scrape the first page to find pagination
            result = self.app.scrape(
                self.blogs_url,
                only_main_content=False
            )
            
            if hasattr(result, 'markdown'):
                content = result.markdown
                
                # Look for pagination links
                # WordPress typically uses /page/2/, /page/3/, etc.
                max_page = self.find_max_page_number(content)
                
                # Generate all page URLs
                for page_num in range(2, max_page + 1):
                    page_url = f"{self.blogs_url}page/{page_num}/"
                    listing_pages.append(page_url)
                
                print(f"   Found {max_page} total pages")
                
        except Exception as e:
            print(f"   ❌ Error discovering pages: {str(e)}")
        
        return listing_pages
    
    def find_max_page_number(self, content):
        """Find the maximum page number from pagination"""
        # Look for pagination patterns
        # Common patterns: /page/10/, "Page 1 of 10", etc.
        
        # Pattern 1: /page/X/ URLs
        page_pattern = r'/page/(\d+)/'
        page_matches = re.findall(page_pattern, content)
        
        if page_matches:
            max_found = max(int(p) for p in page_matches)
            # Limit to 3 pages maximum
            return min(max_found, 3)
        
        # Pattern 2: "Page X of Y"
        page_of_pattern = r'Page \d+ of (\d+)'
        page_of_match = re.search(page_of_pattern, content)
        
        if page_of_match:
            max_found = int(page_of_match.group(1))
            # Limit to 3 pages maximum
            return min(max_found, 3)
        
        # Default to checking first 3 pages if pattern not found
        return 3
    
    def extract_post_urls_from_listing(self, listing_url):
        """Extract individual blog post URLs from a listing page"""
        post_urls = []
        
        try:
            result = self.app.scrape(
                listing_url,
                only_main_content=False
            )
            
            if hasattr(result, 'markdown'):
                content = result.markdown
                
                # Look for blog post URLs
                # Pattern: https://www.vlsisystemdesign.com/some-blog-title/
                post_pattern = r'https://www\.vlsisystemdesign\.com/([^/\s"\'\#]+)/$'
                matches = re.findall(post_pattern, content)
                
                for match in matches:
                    full_url = f"https://www.vlsisystemdesign.com/{match}/"
                    
                    # Filter out non-blog URLs
                    if self.is_valid_blog_url(full_url):
                        post_urls.append(full_url)
                
                # Also look for markdown links
                md_link_pattern = r'\[([^\]]+)\]\((https://www\.vlsisystemdesign\.com/[^/\)]+/)\)'
                md_matches = re.findall(md_link_pattern, content)
                
                for title, url in md_matches:
                    if self.is_valid_blog_url(url):
                        post_urls.append(url)
                
                print(f"   Found {len(post_urls)} blog posts on this page")
                
        except Exception as e:
            print(f"   ❌ Error extracting posts from {listing_url}: {str(e)}")
        
        return list(set(post_urls))  # Remove duplicates
    
    def is_valid_blog_url(self, url):
        """Check if URL is a valid blog post URL"""
        # Exclude common non-blog pages
        exclude_patterns = [
            '/wp-', '/category/', '/tag/', '/author/', '/page/',
            '/search/', '/contact/', '/about/', '/privacy/',
            '/terms/', '/feed/', '/rss/', '/sitemap/',
            '/blogs/$', '/blogs/page/', '/#', '/comment',
            '/wp-content/', '/wp-admin/', '/wp-includes/',
            '/cart/', '/checkout/', '/my-account/', '/shop/',
            '/product/', '/portfolio/', '/gallery/'
        ]
        
        url_lower = url.lower()
        
        # Check if URL contains any exclude pattern
        for pattern in exclude_patterns:
            if pattern in url_lower:
                return False
        
        # Check if it's under the main domain
        if not url.startswith(self.base_url):
            return False
        
        # Should have a slug after the domain
        path = urlparse(url).path
        if path == '/' or path == '':
            return False
        
        return True
    
    def scrape_individual_post(self, url, max_retries=3):
        """Scrape an individual blog post"""
        for attempt in range(max_retries):
            try:
                # Use longer wait time for JavaScript rendering
                result = self.app.scrape(
                    url,
                    only_main_content=True
                )
                
                if hasattr(result, 'markdown'):
                    content = result.markdown
                    
                    # Extract and clean the content
                    cleaned_content = self.clean_blog_content(content)
                    
                    # Only process if we have substantial content
                    if len(cleaned_content) > 200:
                        # Extract metadata
                        title = self.extract_title(result, content, url)
                        date = self.extract_date(content, url)
                        author = self.extract_author(content)
                        
                        return {
                            'url': url,
                            'title': title,
                            'date': date,
                            'author': author,
                            'content': cleaned_content,
                            'word_count': len(cleaned_content.split())
                        }
                    else:
                        print(f"      ⚠️ Content too short ({len(cleaned_content)} chars)")
                        
                        # Try alternative scraping method
                        if attempt < max_retries - 1:
                            print(f"      🔄 Retrying with different parameters...")
                            time.sleep(5)
                            continue
                
            except Exception as e:
                if "rate limit" in str(e).lower():
                    print(f"      ⏳ Rate limit hit, waiting 60 seconds...")
                    time.sleep(60)
                else:
                    print(f"      ❌ Error (attempt {attempt + 1}): {str(e)[:100]}...")
                    if attempt < max_retries - 1:
                        time.sleep(5)
        
        return None
    
    def clean_blog_content(self, content):
        """Clean and extract the actual blog content"""
        if not content:
            return ""
        
        lines = content.split('\n')
        cleaned_lines = []
        
        # Skip navigation and header elements
        skip_patterns = [
            'skip to content',
            'menu',
            'search',
            'share this',
            'related posts',
            'previous post',
            'next post',
            'leave a comment',
            'your email',
            'subscribe',
            'follow us',
            'copyright',
            'all rights reserved',
            'privacy policy',
            'terms of service',
            'cookie policy'
        ]
        
        in_content = False
        content_started = False
        
        for line in lines:
            line_stripped = line.strip()
            line_lower = line_stripped.lower()
            
            # Skip empty lines at the beginning
            if not content_started and not line_stripped:
                continue
            
            # Skip lines with skip patterns
            if any(pattern in line_lower for pattern in skip_patterns):
                continue
            
            # Detect start of main content (usually after title/date)
            if not in_content and len(line_stripped) > 50:
                in_content = True
                content_started = True
            
            # Add line if it's part of content
            if in_content and line_stripped:
                # Skip very short lines that might be UI elements
                if len(line_stripped) > 3 or line_stripped.startswith('#'):
                    cleaned_lines.append(line)
            
            # Stop at comment section or footer
            if any(footer in line_lower for footer in ['leave a reply', 'post navigation', 'related posts']):
                break
        
        return '\n'.join(cleaned_lines).strip()
    
    def extract_title(self, result, content, url):
        """Extract the blog post title"""
        # Try to get from metadata first
        if hasattr(result, 'metadata') and hasattr(result.metadata, 'title'):
            title = result.metadata.title
            # Clean common suffixes
            title = re.sub(r'\s*[-–—|]\s*VLSI System Design.*$', '', title)
            title = re.sub(r'\s*[-–—|]\s*VSD.*$', '', title)
            return title.strip()
        
        # Try to extract from content
        lines = content.split('\n')
        for line in lines[:10]:
            line_stripped = line.strip()
            if line_stripped.startswith('# ') and len(line_stripped) > 10:
                return line_stripped[2:].strip()
        
        # Fallback to URL slug
        path = urlparse(url).path
        slug = path.strip('/').split('/')[-1]
        title = slug.replace('-', ' ').title()
        return title
    
    def extract_date(self, content, url):
        """Extract the publication date"""
        # Common date patterns
        date_patterns = [
            r'(\w+ \d{1,2}, \d{4})',  # January 15, 2024
            r'(\d{1,2} \w+ \d{4})',    # 15 January 2024
            r'(\d{4}-\d{2}-\d{2})',    # 2024-01-15
            r'(\d{1,2}/\d{1,2}/\d{4})', # 01/15/2024
        ]
        
        # Look for date in first 20 lines
        lines = content.split('\n')[:20]
        for line in lines:
            for pattern in date_patterns:
                match = re.search(pattern, line)
                if match:
                    return match.group(1)
        
        return "Date not found"
    
    def extract_author(self, content):
        """Extract the author name"""
        # Common author patterns
        author_patterns = [
            r'[Bb]y\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'[Aa]uthor:\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'[Ww]ritten\s+by\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
        ]
        
        # Look in first 15 lines
        lines = content.split('\n')[:15]
        for line in lines:
            for pattern in author_patterns:
                match = re.search(pattern, line)
                if match:
                    author = match.group(1)
                    # Validate it's a reasonable author name
                    if 2 <= len(author.split()) <= 4 and len(author) < 50:
                        return author
        
        return "Unknown"
    
    def save_results(self):
        """Save the scraped results to files"""
        if not self.results:
            print("\n⚠️ No blog posts were successfully scraped")
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save as Markdown
        md_filename = f'vlsi_system_design_blogs_{timestamp}.md'
        self.save_as_markdown(md_filename)
        
        # Save as JSON
        json_filename = f'vlsi_system_design_blogs_{timestamp}.json'
        self.save_as_json(json_filename)
        
        print(f"\n✅ Extraction completed successfully!")
        print(f"📄 Markdown file: {md_filename}")
        print(f"📄 JSON file: {json_filename}")
        print(f"📊 Total blog posts extracted: {len(self.results)}")
        print(f"📊 Total words: {sum(post['word_count'] for post in self.results):,}")
        
        return md_filename
    
    def save_as_markdown(self, filename):
        """Save results as a markdown file"""
        # Sort by date (if available) or by title
        self.results.sort(key=lambda x: (x['date'], x['title']))
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# VLSI System Design - Blog Archive\n\n")
            f.write(f"**Source:** {self.base_url}\n")
            f.write(f"**Extracted on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Total Posts:** {len(self.results)}\n")
            f.write(f"**Total Words:** {sum(post['word_count'] for post in self.results):,}\n\n")
            f.write("---\n\n")
            
            # Table of Contents
            f.write("## 📚 Table of Contents\n\n")
            for i, post in enumerate(self.results, 1):
                # Create anchor-friendly title
                anchor = re.sub(r'[^a-zA-Z0-9\s-]', '', post['title'].lower())
                anchor = re.sub(r'\s+', '-', anchor)
                f.write(f"{i}. [{post['title']}](#{anchor})\n")
            
            f.write("\n---\n\n")
            
            # Write each blog post
            for i, post in enumerate(self.results, 1):
                # Create anchor-friendly title
                anchor = re.sub(r'[^a-zA-Z0-9\s-]', '', post['title'].lower())
                anchor = re.sub(r'\s+', '-', anchor)
                
                f.write(f"## {i}. {post['title']} {{#{anchor}}}\n\n")
                f.write(f"**Date:** {post['date']}\n")
                f.write(f"**Author:** {post['author']}\n")
                f.write(f"**URL:** [{post['url']}]({post['url']})\n")
                f.write(f"**Word Count:** {post['word_count']:,}\n\n")
                
                f.write(post['content'])
                f.write("\n\n---\n\n")
    
    def save_as_json(self, filename):
        """Save results as a JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'metadata': {
                    'source': self.base_url,
                    'extracted_on': datetime.now().isoformat(),
                    'total_posts': len(self.results),
                    'total_words': sum(post['word_count'] for post in self.results)
                },
                'posts': self.results
            }, f, indent=2, ensure_ascii=False)


# Main execution
if __name__ == "__main__":
    print("🚀 VLSI System Design Blog Scraper\n")
    print("ℹ️  This scraper is designed to handle JavaScript-rendered content")
    print("ℹ️  It may take some time due to rate limiting and page rendering\n")
    
    # Check for API key
    load_dotenv()
    if not os.getenv("FIRECRAWL_API_KEY"):
        print("❌ FIRECRAWL_API_KEY not found in .env file")
        print("Please add your Firecrawl API key to the .env file")
        exit(1)
    
    scraper = VLSISystemDesignScraper()
    
    try:
        result_file = scraper.extract_vlsi_blogs()
        
        if result_file:
            print(f"\n✨ Scraping completed! Check {result_file} for the results.")
        else:
            print("\n❌ Scraping failed. Please check the errors above.")
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Scraping interrupted by user")
        print(f"📊 Partial results: {len(scraper.results)} posts scraped")
        
        if scraper.results:
            # Save partial results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            partial_file = f'vlsi_system_design_blogs_partial_{timestamp}.md'
            scraper.save_as_markdown(partial_file)
            print(f"📄 Partial results saved to: {partial_file}")
            
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()