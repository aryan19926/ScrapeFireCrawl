import os
from datetime import datetime
from dotenv import load_dotenv
import time
import re

# CORRECT IMPORT - Make sure you're using this:
from firecrawl import FirecrawlApp  # NOT from firecrawl import Firecrawl

class ChipEdgeVLSICrawler:
    def __init__(self):
        load_dotenv()
        # CORRECT INITIALIZATION - Use FirecrawlApp, not Firecrawl
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.results = []
        
        # Define relevant VLSI categories
        self.vlsi_categories = {
            'analog-layout': 'Analog Layout',
            'asic-design-flow': 'ASIC Design Flow', 
            'design-for-test': 'Design for Test (DFT)',
            'design-verification': 'Design Verification',
            'fpga': 'FPGA',
            'physical-design': 'Physical Design',
            'risc-v': 'RISC-V',
            'rtl-design': 'RTL Design - Lint & CDC',
            'soc-design': 'SOC Design',
            'synthesis-sta': 'Synthesis & STA'
        }
    
    def test_connection(self):
        """Test if Firecrawl is properly initialized"""
        print("Testing Firecrawl connection...")
        try:
            # Test with a simple scrape
            result = self.app.scrape(
                'https://chipedge.com',
                only_main_content=True
            )
            if result:
                print("✅ Firecrawl connection successful!")
                return True
        except Exception as e:
            print(f"❌ Firecrawl connection failed: {str(e)}")
            return False
    
    def extract_vlsi_blogs(self):
        """Extract all VLSI technical blog posts and save as markdown"""
        
        print("Starting ChipEdge VLSI blog extraction...")
        
        # Test connection first
        if not self.test_connection():
            print("Please check your FIRECRAWL_API_KEY in .env file")
            return None
        
        # Since crawl might not work, let's go directly to scraping approach
        return self.scrape_categories_individually()
    
    def scrape_categories_individually(self):
        """Scrape each category page individually"""
        all_results = []
        
        # List of category pages to scrape
        category_urls = [
            'https://chipedge.com/resources/category/physical-design/',
            'https://chipedge.com/resources/category/design-verification/',
            'https://chipedge.com/resources/category/design-for-test/',
            'https://chipedge.com/resources/category/rtl-design-lint-cdc/',
            'https://chipedge.com/resources/category/analog-layout/',
            'https://chipedge.com/resources/category/synthesis-sta/',
            'https://chipedge.com/resources/category/asic-design-flow/',
            'https://chipedge.com/resources/category/soc-design/',
            'https://chipedge.com/resources/category/fpga/',
            'https://chipedge.com/resources/category/risc-v/'
        ]
        
        # First, let's try to get the main blog page to find all posts
        print("\n📁 Fetching main blog page...")
        try:
            main_result = self.app.scrape(
                'https://chipedge.com/resources/blogs/',
                only_main_content=True
            )
            
            # Handle Document object from Firecrawl
            if hasattr(main_result, 'markdown'):
                content = main_result.markdown
                print(f"✅ Main page scraped successfully")
                
                # Extract all blog post links from markdown
                all_post_links = self.extract_all_post_links_from_markdown(content)
                print(f"Found {len(all_post_links)} total blog posts")
                
                # Filter for technical posts
                technical_posts = [url for url in all_post_links if self.is_technical_post_url(url)]
                print(f"Filtered to {len(technical_posts)} potential technical posts")
                
                # Scrape each technical post
                for i, post_url in enumerate(technical_posts[:50], 1):  # Limit to first 50 for testing
                    print(f"\n[{i}/{len(technical_posts[:50])}] Scraping: {post_url.split('/')[-2][:40]}...")
                    post_data = self.scrape_individual_post(post_url)
                    if post_data:
                        all_results.append(post_data)
                        print(f"   ✅ Added: {post_data['title'][:50]}...")
                    else:
                        print(f"   ❌ No technical content found in this post")
                    time.sleep(0.5)  # Rate limiting
                    
                # If we didn't find enough technical posts, try category pages
                if len(all_results) < 5:
                    print(f"\n📁 Found only {len(all_results)} technical posts, trying category pages...")
                    category_results = self.scrape_category_pages(category_urls)
                    all_results.extend(category_results)
                    
        except Exception as e:
            print(f"❌ Error fetching main page: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # Fallback to category approach
            category_results = self.scrape_category_pages(category_urls)
            all_results.extend(category_results)
        
        # Save results
        self.results = all_results
        return self.save_markdown_results()
    
    def scrape_category_pages(self, category_urls):
        """Scrape posts from individual category pages with rate limit handling"""
        category_results = []
        
        for url in category_urls:
            category_name = url.split('/')[-2]
            print(f"\n📁 Scraping category: {category_name}")
            
            # Retry for category page scraping
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    # Add delay between category requests
                    time.sleep(2)
                    result = self.app.scrape(url)
                    
                    if hasattr(result, 'markdown'):
                        content = result.markdown
                        post_links = self.extract_all_post_links_from_markdown(content)
                        print(f"   Found {len(post_links)} posts")
                        
                        for post_url in post_links[:5]:  # Increased limit per category
                            if self.is_technical_post_url(post_url):
                                # Add delay between post requests
                                time.sleep(1)
                                post_data = self.scrape_individual_post(post_url)
                                if post_data:
                                    category_results.append(post_data)
                                    print(f"   ✅ Added: {post_data['title'][:50]}...")
                    break  # Success, exit retry loop
                                
                except Exception as e:
                    if "Rate Limit" in str(e):
                        print(f"   ⏳ Rate limit hit for category (attempt {attempt + 1}/{max_retries}), waiting 60 seconds...")
                        time.sleep(60)
                        continue
                    else:
                        print(f"   ❌ Error: {str(e)}")
                        break
                
        return category_results
    
    def extract_all_post_links_from_markdown(self, markdown_content):
        """Extract all blog post URLs from markdown content"""
        links = set()
        
        # Pattern to find all markdown links pointing to resources
        markdown_link_pattern = r'\[([^\]]*)\]\((https://chipedge\.com/resources/[^)]+)\)'
        matches = re.findall(markdown_link_pattern, markdown_content)
        
        for title, url in matches:
            links.add(url)
        
        # Also try to find plain URLs in the markdown
        url_pattern = r'https://chipedge\.com/resources/[^\s\)]+'
        url_matches = re.findall(url_pattern, markdown_content)
        links.update(url_matches)
        
        # Filter out category pages and other non-post pages
        post_links = []
        for link in links:
            if not any(x in link for x in ['category/', 'courses/', 'training/', 'placements/', 'wp-content/']):
                post_links.append(link)
        
        return sorted(list(set(post_links)))
    
    def extract_all_post_links(self, html_content):
        """Extract all blog post URLs from HTML content"""
        links = set()
        
        # Pattern to find all hrefs pointing to resources
        href_pattern = r'href="(https://chipedge\.com/resources/[^"]+/)"'
        matches = re.findall(href_pattern, html_content)
        links.update(matches)
        
        # Also try relative URLs
        rel_pattern = r'href="(/resources/[^"]+/)"'
        rel_matches = re.findall(rel_pattern, html_content)
        for match in rel_matches:
            links.add(f"https://chipedge.com{match}")
        
        # Filter out category pages and other non-post pages
        post_links = []
        for link in links:
            if not any(x in link for x in ['category/', 'courses/', 'training/', 'placements/']):
                post_links.append(link)
        
        return sorted(list(set(post_links)))
    
    def scrape_individual_post(self, url, max_retries=3):
        """Scrape an individual blog post with rate limit handling"""
        for attempt in range(max_retries):
            try:
                result = self.app.scrape(url)
                
                # Handle Document object from Firecrawl
                if hasattr(result, 'markdown'):
                    content = result.markdown
                    
                    # Check if it's technical content
                    if self.is_technical_content(content):
                        return {
                            'url': url,
                            'title': self.extract_title_from_result(result, content),
                            'category': self.determine_category(url, content),
                            'date': self.extract_date(content),
                            'content': content
                        }
                elif isinstance(result, dict) and 'content' in result:
                    # Fallback for old format
                    content = result.get('markdown', '')
                    if not content:
                        # Convert HTML to text if no markdown
                        content = self.html_to_text(result['content'])
                    
                    # Check if it's technical content
                    if self.is_technical_content(content):
                        return {
                            'url': url,
                            'title': self.extract_title_from_result(result, content),
                            'category': self.determine_category(url, content),
                            'date': self.extract_date(content),
                            'content': content
                        }
                
            except Exception as e:
                if "Rate Limit" in str(e):
                    print(f"      ⏳ Rate limit hit (attempt {attempt + 1}/{max_retries}), waiting 60 seconds...")
                    time.sleep(60)
                    continue
                else:
                    print(f"      ❌ Error: {str(e)}")
                    break
                
        return None
    
    def html_to_text(self, html):
        """Simple HTML to text conversion"""
        # Remove script and style elements
        html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)
        
        # Replace headers with markdown-style headers
        html = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', html)
        html = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', html)
        html = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', html)
        
        # Replace paragraphs and breaks
        html = re.sub(r'<p[^>]*>', '\n', html)
        html = re.sub(r'</p>', '\n', html)
        html = re.sub(r'<br[^>]*>', '\n', html)
        
        # Remove remaining HTML tags
        html = re.sub(r'<[^>]+>', '', html)
        
        # Clean up whitespace
        lines = [line.strip() for line in html.split('\n')]
        return '\n'.join(line for line in lines if line)
    
    def is_technical_post_url(self, url):
        """Check if URL is likely a technical post"""
        exclude_patterns = [
            'career', 'internship', 'job', 'placement', 
            'certification-course', 'online-vs-offline',
            'courses', 'training', 'category', 'wp-content',
            'blogs#', 'blogs/', 'blogs$'
        ]
        
        url_lower = url.lower()
        
        # Exclude URLs that are clearly not blog posts
        if any(pattern in url_lower for pattern in exclude_patterns):
            return False
            
        # Must be a proper blog post URL (not just the main page)
        if not url_lower.endswith('/') or 'resources/' not in url_lower:
            return False
            
        return True
    
    def extract_title_from_result(self, result, content):
        """Extract title from scrape result"""
        # Try to get from metadata
        if hasattr(result, 'metadata') and hasattr(result.metadata, 'title'):
            title = result.metadata.title
            # Clean common suffixes
            title = title.replace(' - ChipEdge', '').replace(' | ChipEdge', '')
            return title
        elif isinstance(result, dict) and 'metadata' in result and 'title' in result['metadata']:
            title = result['metadata']['title']
            # Clean common suffixes
            title = title.replace(' - ChipEdge', '').replace(' | ChipEdge', '')
            return title
        
        # Extract from content
        return self.extract_title(content)
    
    def is_technical_content(self, content):
        """Filter for technical VLSI content only"""
        if not content or len(content) < 200:
            return False
            
        technical_keywords = [
            'verilog', 'systemverilog', 'rtl', 'synthesis', 'physical design',
            'verification', 'uvm', 'dft', 'scan', 'atpg', 'sta', 'timing',
            'floorplan', 'placement', 'routing', 'fpga', 'asic', 'soc',
            'risc-v', 'lint', 'cdc', 'clock domain', 'reset', 'fifo',
            'fsm', 'state machine', 'testbench', 'assertion', 'coverage',
            'python', 'tcl', 'skill', 'design rule', 'drc', 'lvs', 'vlsi',
            'design', 'chip', 'circuit', 'semiconductor', 'layout', 'netlist'
        ]
        
        content_lower = content.lower()
        
        # Only exclude very obvious non-technical content (commented out for more inclusive results)
        # exclude_keywords = [
        #     'job opening', 'internship opportunity', 'placement details', 
        #     'hiring', 'recruitment', 'job posting'
        # ]
        # if any(keyword in content_lower for keyword in exclude_keywords):
        #     return False
            
        # Must contain at least 1 technical keyword
        keyword_count = sum(1 for keyword in technical_keywords if keyword in content_lower)
        return keyword_count >= 1
    
    def determine_category(self, url, content):
        """Determine category from URL and content"""
        url_lower = url.lower()
        content_lower = content.lower()
        
        # Check URL patterns first
        for slug, category_name in self.vlsi_categories.items():
            if f'/category/{slug}' in url_lower:
                return category_name
        
        # Check content for category indicators
        if 'physical design' in content_lower or 'floorplan' in content_lower:
            return 'Physical Design'
        elif 'dft' in content_lower or 'design for test' in content_lower:
            return 'Design for Test (DFT)'
        elif 'verification' in content_lower and ('uvm' in content_lower or 'systemverilog' in content_lower):
            return 'Design Verification'
        elif 'fpga' in content_lower:
            return 'FPGA'
        elif 'rtl' in content_lower and ('lint' in content_lower or 'cdc' in content_lower):
            return 'RTL Design - Lint & CDC'
        elif 'synthesis' in content_lower or 'sta' in content_lower:
            return 'Synthesis & STA'
        elif 'analog' in content_lower and 'layout' in content_lower:
            return 'Analog Layout'
        elif 'asic' in content_lower and 'flow' in content_lower:
            return 'ASIC Design Flow'
        elif 'soc' in content_lower:
            return 'SOC Design'
        elif 'risc-v' in content_lower or 'riscv' in content_lower:
            return 'RISC-V'
        else:
            return 'VLSI Technical'
    
    def extract_title(self, content):
        """Extract title from content"""
        if not content:
            return 'Untitled'
            
        lines = content.split('\n')
        for line in lines[:10]:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
            elif line and not line.startswith('#') and len(line) > 10:
                return line[:100]
        
        return 'Untitled'
    
    def extract_date(self, content):
        """Extract publication date from content"""
        if not content:
            return 'Date not found'
            
        date_patterns = [
            r'(\d{1,2}/\d{1,2}/\d{4})',
            r'(\d{1,2}-\d{1,2}-\d{4})',
            r'(\d{4}-\d{2}-\d{2})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, content[:500])  # Check only beginning
            if match:
                return match.group(1)
        
        return 'Date not found'
    
    def save_markdown_results(self):
        """Save results to markdown file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'chipedge_vlsi_blogs_{timestamp}.md'
        
        if not self.results:
            print("\n⚠️ No technical VLSI content found")
            return None
            
        self.create_markdown_file(filename)
        
        print(f"\n✅ Extraction completed successfully!")
        print(f"📄 Saved to: {filename}")
        print(f"📊 Total technical blogs extracted: {len(self.results)}")
        
        return filename
    
    def create_markdown_file(self, filename):
        """Create markdown file with results"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# ChipEdge VLSI Technical Blogs\n\n")
            f.write(f"**Extracted on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Technical Blogs:** {len(self.results)}\n\n")
            f.write("---\n\n")
            
            # Group by category
            blogs_by_category = {}
            for blog in self.results:
                category = blog['category']
                if category not in blogs_by_category:
                    blogs_by_category[category] = []
                blogs_by_category[category].append(blog)
            
            # Write TOC
            f.write("## 📚 Table of Contents\n\n")
            for i, category in enumerate(sorted(blogs_by_category.keys()), 1):
                count = len(blogs_by_category[category])
                anchor = category.lower().replace(' ', '-').replace('(', '').replace(')', '')
                f.write(f"{i}. [{category} ({count} posts)](#{anchor})\n")
            
            f.write("\n---\n\n")
            
            # Write blogs
            for category in sorted(blogs_by_category.keys()):
                anchor = category.lower().replace(' ', '-').replace('(', '').replace(')', '')
                f.write(f"## {category}\n\n")
                
                for i, blog in enumerate(blogs_by_category[category], 1):
                    f.write(f"### {i}. {blog['title']}\n\n")
                    f.write(f"**URL:** {blog['url']}\n")
                    f.write(f"**Date:** {blog['date']}\n\n")
                    f.write(blog['content'])
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
    
    crawler = ChipEdgeVLSICrawler()
    
    try:
        markdown_file = crawler.extract_vlsi_blogs()
        
    except Exception as e:
        print(f"\n❌ Extraction failed: {str(e)}")
        import traceback
        traceback.print_exc()