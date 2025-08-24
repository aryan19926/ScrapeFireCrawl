import os
import re
import time
import json
import signal
import sys
import threading
from datetime import datetime
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
from typing import List, Dict, Optional
import hashlib

class VLSIExpertScraper:
    def __init__(self, debug=False):
        load_dotenv()
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.results = []
        self.state_file = "vlsi_expert_scrape_state.json"
        self.partial_file = "vlsi_expert_partial_content.md"
        self.save_interval = 10  # Save every 10 articles
        self.interrupted = False
        self.debug = debug
        self.timeout = 30  # 30 seconds timeout per article
        
        # VLSI-specific categories and keywords
        self.vlsi_categories = {
            'physical-design': ['floorplan', 'placement', 'routing', 'cts', 'clock tree'],
            'sta': ['setup', 'hold', 'timing', 'delay', 'slack', 'propagation'],
            'parasitic': ['spef', 'dspf', 'extraction', 'rc', 'capacitance'],
            'dft': ['scan', 'atpg', 'test', 'fault', 'coverage'],
            'low-power': ['power', 'leakage', 'dynamic', 'upf', 'cpf'],
            'analog': ['layout', 'matching', 'drc', 'lvs', 'antenna'],
            'digital-design': ['verilog', 'vhdl', 'rtl', 'synthesis', 'fsm'],
            'verification': ['systemverilog', 'uvm', 'assertion', 'testbench']
        }
        
        # Set up signal handlers for graceful interruption
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Handle interruption signals gracefully"""
        print(f"\n\n⚠️ Interruption signal received (Signal {signum})")
        print("🔄 Saving partial results...")
        self.save_partial_results()
        print("✅ Partial results saved. Exiting gracefully.")
        sys.exit(0)
    
    def save_partial_results(self):
        """Save partial results to markdown file"""
        if not self.results:
            print("📝 No results to save yet.")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'vlsi_expert_partial_{timestamp}.md'
        
        print(f"💾 Saving partial results to: {filename}")
        print(f"📄 Articles saved so far: {len(self.results)}")
        
        with open(filename, 'w', encoding='utf-8') as f:
            # Header
            f.write("# VLSI-Expert.com Technical Content (PARTIAL)\n\n")
            f.write(f"**Extracted on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Articles:** {len(self.results)} (PARTIAL - Scraping was interrupted)\n\n")
            f.write("⚠️ **Note:** This is a partial result. The scraping process was interrupted.\n\n")
            
            # Category summary
            categories = {}
            for article in self.results:
                cat = article['category']
                categories[cat] = categories.get(cat, 0) + 1
            
            f.write("## 📊 Content Summary (Partial)\n\n")
            for cat, count in sorted(categories.items()):
                f.write(f"- **{cat.replace('-', ' ').title()}**: {count} articles\n")
            
            f.write("\n---\n\n")
            
            # Table of Contents
            f.write("## 📚 Table of Contents (Partial)\n\n")
            
            # Group by category
            articles_by_category = {}
            for article in self.results:
                cat = article['category']
                if cat not in articles_by_category:
                    articles_by_category[cat] = []
                articles_by_category[cat].append(article)
            
            # Write TOC
            for cat in sorted(articles_by_category.keys()):
                anchor = cat.lower().replace(' ', '-')
                count = len(articles_by_category[cat])
                f.write(f"- [{cat.replace('-', ' ').title()} ({count})](##{anchor})\n")
            
            f.write("\n---\n\n")
            
            # Write articles by category
            for cat in sorted(articles_by_category.keys()):
                f.write(f"## {cat.replace('-', ' ').title()}\n\n")
                
                # Sort articles by date (newest first)
                articles = sorted(articles_by_category[cat], 
                                key=lambda x: x.get('date', ''), 
                                reverse=True)
                
                for i, article in enumerate(articles, 1):
                    f.write(f"### {i}. {article['title']}\n\n")
                    f.write(f"**URL:** {article['url']}\n")
                    f.write(f"**Date:** {article['date']}\n")
                    if article['tags']:
                        f.write(f"**Tags:** {', '.join(article['tags'])}\n")
                    f.write("\n")
                    
                    # Write content
                    f.write(article['content'])
                    f.write("\n\n---\n\n")
        
        # Also save state
        self.save_state()
        
        print(f"✅ Partial results saved to: {os.path.abspath(filename)}")
        return filename
    
    def extract_vlsi_content(self):
        """Main extraction method for vlsi-expert.com"""
        print("🚀 Starting VLSI-Expert.com extraction...")
        print("📝 Output: Markdown file only")
        print("=" * 60)
        
        # Phase 1: Get content index
        print("\n📑 Phase 1: Fetching content index...")
        content_map = self.get_content_index()
        
        # Phase 2: Use targeted scraping (more reliable)
        print("\n🌐 Phase 2: Using targeted scraping approach...")
        crawl_results = self.targeted_scraping()
        
        # Phase 3: Process and categorize
        print("\n🔍 Phase 3: Processing and categorizing content...")
        self.process_results(crawl_results)
        
        # Phase 4: Save results
        print("\n💾 Phase 4: Saving results...")
        return self.save_results()
    
    def get_content_index(self):
        """Scrape the main content index page with improved link extraction"""
        try:
            print("🔗 Fetching: https://www.vlsi-expert.com/p/content.html")
            result = self.app.scrape(
                'https://www.vlsi-expert.com/p/content.html',
                only_main_content=False
            )
            
            if result:
                # Handle different result formats
                if hasattr(result, 'markdown'):
                    content = result.markdown
                elif isinstance(result, dict) and 'content' in result:
                    content = result['content']
                else:
                    content = str(result)
                
                # Extract all article links from content page
                links = self.extract_links_from_content(content)
                
                # Also extract chapter links from tables
                chapter_links = self.extract_chapter_links_from_tables(content)
                
                # Combine and deduplicate
                all_links = list(set(links + chapter_links))
                
                print(f"✅ Found {len(links)} regular links + {len(chapter_links)} chapter links = {len(all_links)} total")
                return all_links
            
        except Exception as e:
            print(f"⚠️ Could not fetch content index: {str(e)}")
            
        return []
    
    def crawl_vlsi_site(self):
        """Crawl the entire site with optimal configuration"""
        try:
            print("Starting comprehensive crawl...")
            crawl_result = self.app.crawl(
                'https://www.vlsi-expert.com',
                limit=500,
                max_discovery_depth=3,
                include_paths=['/p/*', '/20*/*', '/content/*'],
                exclude_paths=['/search/*', '/feeds/*', '/archive/*', '/*m=1', '/*showComment*'],
                scrape_options={
                    'only_main_content': True,
                    'include_html': True
                }
            )
            
            if crawl_result:
                # Handle CrawlJob object - get the results
                if hasattr(crawl_result, 'result'):
                    pages = crawl_result.result
                    print(f"✅ Crawl completed! Found {len(pages)} pages")
                    return pages
                else:
                    print(f"✅ Crawl completed! Found {crawl_result} pages")
                    return crawl_result
                
        except Exception as e:
            print(f"❌ Crawl failed: {str(e)}")
            print("Falling back to targeted scraping approach...")
            return self.targeted_scraping()
    
    def targeted_scraping(self):
        """Alternative approach: Scrape specific sections with improved link extraction"""
        all_results = []
        visited_urls = set()  # Track visited URLs to avoid duplicates
        
        # First, get all links from the content index
        print("📑 Getting links from content index...")
        content_links = self.get_content_index()
        print(f"   Found {len(content_links)} links in content index")
        
        # Extract chapter links from content index (we need to get the content first)
        print("📋 Extracting chapter links from content index...")
        try:
            result = self.app.scrape('https://www.vlsi-expert.com/p/content.html', only_main_content=False)
            if result:
                if hasattr(result, 'markdown'):
                    content = result.markdown
                elif isinstance(result, dict) and 'content' in result:
                    content = result['content']
                else:
                    content = str(result)
                
                chapter_links = self.extract_chapter_links_from_tables(content)
                print(f"   Found {len(chapter_links)} chapter links")
            else:
                chapter_links = []
                print(f"   Found 0 chapter links (no content)")
        except Exception as e:
            chapter_links = []
            print(f"   Found 0 chapter links (error: {str(e)})")
        
        # Combine all links
        all_links = list(set(content_links + chapter_links))
        print(f"   Total unique links to process: {len(all_links)}")
        
        # Scrape each article from the combined links
        print("\n📄 Scraping articles from all sources...")
        successful_scrapes = 0
        failed_scrapes = 0
        skipped_duplicates = 0
        
        for i, link in enumerate(all_links, 1):
            if link not in visited_urls and self.is_vlsi_article_url(link):
                visited_urls.add(link)
                print(f"\n🔗 [{i}/{len(all_links)}] Scraping: {link}")
                print(f"   📄 Article: {link.split('/')[-1][:50]}...")
                print(f"   ⏱️  Started at: {datetime.now().strftime('%H:%M:%S')}")
                
                try:
                    article = self.scrape_article(link)
                except Exception as e:
                    print(f"   ❌ EXCEPTION: {str(e)}")
                    failed_scrapes += 1
                    continue
                if article:
                    # Check for duplicate content
                    content_hash = article['content_hash']
                    is_duplicate = any(r['content_hash'] == content_hash for r in all_results)
                    
                    if is_duplicate:
                        skipped_duplicates += 1
                        print(f"   ⚠️ SKIPPED - Duplicate content")
                    else:
                        all_results.append(article)
                        successful_scrapes += 1
                        print(f"   ✅ SUCCESS - Added to results")
                        
                        # Save partial results periodically
                        if successful_scrapes % self.save_interval == 0:
                            print(f"   💾 Auto-saving partial results ({successful_scrapes} articles so far)...")
                            # Update the main results list for saving
                            self.results = all_results.copy()
                            self.save_partial_results()
                else:
                    failed_scrapes += 1
                    print(f"   ❌ FAILED - No content extracted")
                
                time.sleep(0.5)  # Rate limiting
            else:
                skipped_duplicates += 1
                print(f"\n🔗 [{i}/{len(all_links)}] Skipping duplicate: {link}")
                
        print(f"\n📊 Content Index Results:")
        print(f"   ✅ Successful scrapes: {successful_scrapes}")
        print(f"   ❌ Failed scrapes: {failed_scrapes}")
        print(f"   ⚠️ Skipped duplicates: {skipped_duplicates}")
        print(f"   📄 Total articles found: {len(all_results)}")
                
        # Also scrape recent posts from blog archive
        print("\n📅 Scraping recent blog posts...")
        recent_posts = self.scrape_recent_posts(visited_urls)
        all_results.extend(recent_posts)
        
        # Update the main results list
        self.results = all_results
        return all_results
    
    def scrape_section_with_subsections(self, section_url, section_name):
        """Scrape a section page and all its subsections/chapters"""
        print(f"\n📂 Processing {section_name} section...")
        all_articles = []
        
        try:
            # First, scrape the main section page
            result = self.app.scrape(section_url, only_main_content=False)
            
            if result:
                # Handle different result formats
                if hasattr(result, 'markdown'):
                    content = result.markdown
                elif isinstance(result, dict) and 'content' in result:
                    content = result['content']
                else:
                    content = str(result)
                
                # Extract all links from this section
                links = self.extract_links_from_content(content)
                print(f"   Found {len(links)} links in {section_name}")
                
                # Also look for chapter structure (based on the screenshot)
                chapters = self.extract_chapters_from_content(content)
                if chapters:
                    print(f"   Found {len(chapters)} chapters/subsections")
                
                # Process each link
                for link in links:
                    if self.is_vlsi_article_url(link) and link != section_url:
                        print(f"   📄 Scraping: {link.split('/')[-1][:40]}...")
                        article = self.scrape_article(link)
                        if article:
                            article['section'] = section_name
                            all_articles.append(article)
                        time.sleep(0.5)  # Rate limiting
                        
        except Exception as e:
            print(f"   ❌ Error processing {section_name}: {str(e)}")
        
        return all_articles
    
    def extract_chapters_from_content(self, content):
        """Extract chapter information from section pages"""
        chapters = []
        
        # Look for chapter patterns in the HTML
        # Based on the screenshot, chapters seem to be in table format
        chapter_patterns = [
            r'Chapter\s*\d+[:\s]*([^<]+)',
            r'<td[^>]*>Chapter\d+</td>\s*<td[^>]*>([^<]+)</td>',
            r'href="([^"]+)"[^>]*>Chapter\s*\d+',
        ]
        
        for pattern in chapter_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            chapters.extend(matches)
        
        return list(set(chapters))  # Remove duplicates
    

    
    def scrape_section_with_subsections(self, section_url, section_name, visited_urls):
        """Scrape a section page and all its subsections/chapters"""
        print(f"\n📂 Processing {section_name} section...")
        section_articles = []
        
        try:
            # Scrape the main section page
            result = self.app.scrape(section_url, only_main_content=False)
            
            if result:
                # Handle different result formats
                if hasattr(result, 'markdown'):
                    content = result.markdown
                elif isinstance(result, dict) and 'content' in result:
                    content = result['content']
                else:
                    content = str(result)
                
                # Extract all links from this section
                all_links = self.extract_all_chapter_links(content, section_url)
                print(f"   Found {len(all_links)} total links in {section_name}")
                
                # Process each link
                for link in all_links:
                    if link not in visited_urls and self.is_vlsi_article_url(link):
                        visited_urls.add(link)
                        
                        # Check if this is a subsection page or an article
                        if self.is_section_index_page(link):
                            # Recursively process subsection
                            subsection_name = f"{section_name} - {link.split('/')[-1].replace('.html', '')}"
                            sub_articles = self.scrape_section_with_subsections(
                                link, subsection_name, visited_urls
                            )
                            section_articles.extend(sub_articles)
                        else:
                            # Scrape as article
                            print(f"   📄 Scraping: {link.split('/')[-1][:40]}...")
                            article = self.scrape_article(link)
                            if article:
                                article['section'] = section_name
                                section_articles.append(article)
                            time.sleep(0.5)  # Rate limiting
                        
        except Exception as e:
            print(f"   ❌ Error processing {section_name}: {str(e)}")
        
        return section_articles
    
    def extract_all_chapter_links(self, content, base_url):
        """Extract all chapter and article links from section content"""
        links = set()
        
        # Multiple patterns to catch different link formats
        link_patterns = [
            # Standard href links
            r'href="(https://www\.vlsi-expert\.com/[^"]+)"',
            r'href="(/[^"]+)"',
            # Links in chapter tables (based on screenshot structure)
            r'<a[^>]+href="([^"]+)"[^>]*>(?:Chapter\s*\d+|[^<]+)</a>',
            # Links with onclick or other attributes
            r'(?:href|src)=["\']((?:https://www\.vlsi-expert\.com)?/[^"\']+\.html)["\']'
        ]
        
        for pattern in link_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                # Convert relative URLs to absolute
                if match.startswith('/'):
                    match = f"https://www.vlsi-expert.com{match}"
                elif not match.startswith('http'):
                    # Handle relative paths
                    base_path = '/'.join(base_url.split('/')[:-1])
                    match = f"{base_path}/{match}"
                
                # Clean up URL
                match = match.replace('&amp;', '&')
                links.add(match)
        
        return list(links)
    
    def is_section_index_page(self, url):
        """Check if URL is a section index page rather than an article"""
        # Section index pages typically have certain patterns
        index_patterns = [
            '/p/content',
            '/p/index',
            r'chapter\d+-index',
            r'-contents\.html',
            r'-index\.html'
        ]
        
        url_lower = url.lower()
        return any(pattern in url_lower for pattern in index_patterns)
    
    def scrape_article(self, url):
        """Scrape individual VLSI article with improved content filtering and timeout protection"""
        try:
            if self.debug:
                print(f"      🔍 Debug: Scraping URL: {url}")
            
            result = self.scrape_with_timeout(url)
            
            if result:
                if self.debug:
                    print(f"      🔍 Debug: Got result, type: {type(result)}")
                
                # Handle different result formats
                if hasattr(result, 'markdown'):
                    content = result.markdown
                    if self.debug:
                        print(f"      🔍 Debug: Using result.markdown")
                elif isinstance(result, dict) and 'content' in result:
                    content = result.get('markdown', result.get('content', ''))
                    if self.debug:
                        print(f"      🔍 Debug: Using result['content']")
                else:
                    content = str(result)
                    if self.debug:
                        print(f"      🔍 Debug: Using str(result)")
                
                # Clean content by removing unwanted elements
                content = self.clean_content(content)
                
                # Debug: Print content length and first 200 chars
                print(f"      📏 Content length: {len(content)} chars")
                if len(content) > 0:
                    preview = content[:200].replace(chr(10), ' ').replace(chr(13), ' ')
                    print(f"      📄 Preview: {preview}...")
                else:
                    print(f"      ⚠️ No content after cleaning")
                    return None
                
                # Check if it's technical VLSI content
                if self.is_technical_vlsi_content(content):
                    article_data = {
                        'url': url,
                        'title': self.extract_title(result, content),
                        'content': content,
                        'category': self.categorize_content(content),
                        'date': self.extract_date(content, url),
                        'author': self.extract_author(result),
                        'tags': self.extract_tags(content),
                        'content_hash': hashlib.md5(content.encode()).hexdigest(),
                        'scraped_at': datetime.now().isoformat()
                    }
                    
                    # Extract code snippets if present
                    code_snippets = self.extract_code_snippets(content)
                    if code_snippets:
                        article_data['code_snippets'] = code_snippets
                    
                    return article_data
                else:
                    print(f"      ⚠️ Content filtered out - not technical VLSI content")
                    
            else:
                if self.debug:
                    print(f"      🔍 Debug: No result returned from scrape")
                print(f"      ❌ No content returned from scrape")
                    
        except Exception as e:
            print(f"      ❌ Error: {str(e)}")
            if self.debug:
                import traceback
                traceback.print_exc()
            
        return None
    
    def is_vlsi_article_url(self, url):
        """Check if URL is likely a VLSI technical article - More lenient approach"""
        # Exclude non-article URLs
        exclude_patterns = [
            'search', 'archive', 'feeds', 'label',
            'showComment', 'atom.xml', 'rss', 'comment-form',
            'blogger.com', 'google.com', 'translate',
            'facebook.com', 'twitter.com', 'netvibes.com',
            'yahoo.com', 'whatsapp', 'mailto:', 'javascript:',
            'feeds/posts', 'feeds/comments', 'feeds/default',
            'widgets', 'resources.blogblog.com', 'gstatic.com',
            'branding', 'googlelogo', 'icon_feed', 'arrow_dropdown',
            'atom', 'rss', 'feed', 'comment-form', 'showcomment'
        ]
        
        url_lower = url.lower()
        
        # Exclude if any exclude pattern matches
        if any(pattern in url_lower for pattern in exclude_patterns):
            return False
        
        # More lenient inclusion - just check if it's from vlsi-expert.com and not excluded
        if 'vlsi-expert.com' in url_lower:
            # Exclude obvious non-article patterns
            if any(pattern in url_lower for pattern in ['/feeds/', '/search', '/archive']):
                return False
            return True
        
        return False
    
    def is_technical_vlsi_content(self, content):
        """Determine if content is technical VLSI material - More lenient approach"""
        if not content or len(content) < 100:  # Reduced minimum length
            return False
        
        content_lower = content.lower()
        
        # Exclude unwanted content patterns (but be more specific)
        exclude_patterns = [
            'blogger.com', 'google translate', 'subscribe to',
            'follow us', 'share with', 'report abuse',
            'create blog', 'sign in', 'powered by',
            'employee awards', 'boost morale', 'workplace',
            'whatsapp number', 'contact me', 'drop a mail',
            'resources.blogblog.com', 'widgets', 'arrow_dropdown',
            'icon_feed', 'googlelogo', 'branding', 'gstatic.com',
            'netvibes', 'yahoo', 'facebook', 'twitter',
            'more share by email', 'share with facebook',
            'share with twitter', 'report abuse'
        ]
        
        # Check for unwanted content - but only if it's a significant portion
        unwanted_count = sum(1 for pattern in exclude_patterns if pattern in content_lower)
        if unwanted_count > 5:  # Only exclude if too many unwanted patterns
            return False
        
        # Must have technical VLSI keywords - but be more lenient
        technical_keywords = [
            'timing', 'setup', 'hold', 'propagation', 'delay',
            'floorplan', 'placement', 'routing', 'synthesis',
            'verilog', 'vhdl', 'rtl', 'netlist', 'spef',
            'parasitic', 'extraction', 'drc', 'lvs', 'antenna',
            'clock', 'skew', 'transition', 'capacitance',
            'power', 'leakage', 'dynamic', 'static',
            'signal integrity', 'crosstalk', 'ir drop',
            'electromigration', 'process variation', 'corner',
            'dielectric', 'conformal', 'manufacturing effects',
            'interconnect', 'rc corner', 'timing analysis',
            'static timing', 'hold check', 'setup check',
            # Add more general VLSI terms
            'vlsi', 'chip', 'semiconductor', 'circuit', 'design',
            'layout', 'physical', 'digital', 'analog', 'mixed signal',
            'asic', 'fpga', 'soc', 'ip', 'block', 'module',
            'cell', 'library', 'technology', 'process', 'node',
            'nm', 'micron', 'fabrication', 'foundry', 'tapeout',
            'design rule', 'constraint', 'optimization', 'analysis'
        ]
        
        keyword_count = sum(1 for keyword in technical_keywords if keyword in content_lower)
        
        # Require at least 2 technical keywords (reduced from 3)
        return keyword_count >= 2
    
    def categorize_content(self, content):
        """Categorize content based on VLSI topics"""
        content_lower = content.lower()
        category_scores = {}
        
        # Score each category based on keyword matches
        for category, keywords in self.vlsi_categories.items():
            score = sum(content_lower.count(keyword) for keyword in keywords)
            if score > 0:
                category_scores[category] = score
        
        # Return category with highest score
        if category_scores:
            return max(category_scores, key=category_scores.get)
        
        return 'general-vlsi'
    
    def extract_title(self, result, content):
        """Extract article title"""
        # Try metadata first
        if 'metadata' in result and 'title' in result['metadata']:
            title = result['metadata']['title']
            # Clean common suffixes
            title = re.sub(r'\s*[\|:]?\s*VLSI Concepts?$', '', title)
            return title
        
        # Extract from content
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        
        # Extract from first line
        first_line = content.split('\n')[0].strip()
        if first_line and len(first_line) < 200:
            return first_line
        
        return 'Untitled'
    
    def extract_date(self, content, url):
        """Extract publication date from content or URL"""
        # Try to extract from URL first (YYYY/MM pattern)
        url_date_match = re.search(r'/(\d{4})/(\d{2})/', url)
        if url_date_match:
            year, month = url_date_match.groups()
            return f"{year}-{month}"
        
        # Look for date in content
        date_patterns = [
            r'(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})',
            r'(\d{4}-\d{2}-\d{2})',
            r'(\d{1,2}/\d{1,2}/\d{4})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1)
        
        return 'Unknown'
    
    def extract_author(self, result):
        """Extract author information"""
        if 'metadata' in result and 'author' in result['metadata']:
            return result['metadata']['author']
        
        # Default author for vlsi-expert.com
        return 'VLSI Expert'
    
    def extract_tags(self, content):
        """Extract relevant tags from content"""
        tags = set()
        content_lower = content.lower()
        
        # Add category-based tags
        for category, keywords in self.vlsi_categories.items():
            if any(keyword in content_lower for keyword in keywords):
                tags.add(category)
        
        # Add specific technology tags
        tech_tags = {
            'cmos': 'CMOS',
            'finfet': 'FinFET',
            'esd': 'ESD',
            'crosstalk': 'Crosstalk',
            'ir drop': 'IR-Drop',
            'electromigration': 'EM',
            'opc': 'OPC',
            'cmp': 'CMP'
        }
        
        for keyword, tag in tech_tags.items():
            if keyword in content_lower:
                tags.add(tag)
        
        return list(tags)
    
    def extract_code_snippets(self, content):
        """Extract code blocks from content"""
        code_snippets = []
        
        # Match code blocks
        code_pattern = r'```(?:\w+)?\n(.*?)```'
        matches = re.findall(code_pattern, content, re.DOTALL)
        
        for match in matches:
            code_snippets.append({
                'code': match.strip(),
                'language': self.detect_code_language(match)
            })
        
        return code_snippets
    
    def detect_code_language(self, code):
        """Detect programming language of code snippet"""
        if 'module' in code or 'always' in code or 'reg' in code:
            return 'verilog'
        elif 'entity' in code or 'architecture' in code:
            return 'vhdl'
        elif 'class' in code and 'endclass' in code:
            return 'systemverilog'
        elif 'proc' in code or 'set' in code:
            return 'tcl'
        elif 'def' in code and 'import' in code:
            return 'python'
        else:
            return 'unknown'
    
    def process_results(self, crawl_results):
        """Process crawl results and extract VLSI content"""
        if isinstance(crawl_results, list):
            for result in crawl_results:
                if isinstance(result, dict):
                    # Handle different result formats
                    if hasattr(result, 'markdown'):
                        content = result.markdown
                    elif 'markdown' in result:
                        content = result['markdown']
                    elif 'content' in result:
                        content = result['content']
                    else:
                        content = str(result)
                    
                    url = result.get('url', '')
                    
                    if content and self.is_technical_vlsi_content(content):
                        processed = {
                            'url': url,
                            'title': self.extract_title(result, content),
                            'content': content,
                            'category': self.categorize_content(content),
                            'date': self.extract_date(content, url),
                            'tags': self.extract_tags(content),
                            'content_hash': hashlib.md5(content.encode()).hexdigest()
                        }
                        self.results.append(processed)
    
    def save_results(self):
        """Save results to markdown file only"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'vlsi_expert_content_{timestamp}.md'
        
        print(f"\n💾 Saving results to: {filename}")
        print(f"📄 Total articles to save: {len(self.results)}")
        
        with open(filename, 'w', encoding='utf-8') as f:
            # Header
            f.write("# VLSI-Expert.com Technical Content\n\n")
            f.write(f"**Extracted on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Articles:** {len(self.results)}\n\n")
            
            # Category summary
            categories = {}
            for article in self.results:
                cat = article['category']
                categories[cat] = categories.get(cat, 0) + 1
            
            f.write("## 📊 Content Summary\n\n")
            for cat, count in sorted(categories.items()):
                f.write(f"- **{cat.replace('-', ' ').title()}**: {count} articles\n")
            
            f.write("\n---\n\n")
            
            # Table of Contents
            f.write("## 📚 Table of Contents\n\n")
            
            # Group by category
            articles_by_category = {}
            for article in self.results:
                cat = article['category']
                if cat not in articles_by_category:
                    articles_by_category[cat] = []
                articles_by_category[cat].append(article)
            
            # Write TOC
            for cat in sorted(articles_by_category.keys()):
                anchor = cat.lower().replace(' ', '-')
                count = len(articles_by_category[cat])
                f.write(f"- [{cat.replace('-', ' ').title()} ({count})](##{anchor})\n")
            
            f.write("\n---\n\n")
            
            # Write articles by category
            for cat in sorted(articles_by_category.keys()):
                f.write(f"## {cat.replace('-', ' ').title()}\n\n")
                
                # Sort articles by date (newest first)
                articles = sorted(articles_by_category[cat], 
                                key=lambda x: x.get('date', ''), 
                                reverse=True)
                
                for i, article in enumerate(articles, 1):
                    f.write(f"### {i}. {article['title']}\n\n")
                    f.write(f"**URL:** {article['url']}\n")
                    f.write(f"**Date:** {article['date']}\n")
                    if article['tags']:
                        f.write(f"**Tags:** {', '.join(article['tags'])}\n")
                    f.write("\n")
                    
                    # Write content
                    f.write(article['content'])
                    f.write("\n\n---\n\n")
        
        # Save state for incremental updates
        self.save_state()
        
        print(f"✅ Successfully saved {len(self.results)} articles to {filename}")
        print(f"📁 File location: {os.path.abspath(filename)}")
        return filename
    
    def save_state(self):
        """Save scraping state for incremental updates"""
        state = {
            'last_scrape': datetime.now().isoformat(),
            'total_articles': len(self.results),
            'content_hashes': [r['content_hash'] for r in self.results],
            'urls_scraped': [r['url'] for r in self.results]
        }
        
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self):
        """Load previous scraping state"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return None
    
    def find_partial_files(self):
        """Find existing partial result files"""
        partial_files = []
        for file in os.listdir('.'):
            if file.startswith('vlsi_expert_partial_') and file.endswith('.md'):
                partial_files.append(file)
        return sorted(partial_files, reverse=True)  # Most recent first

    def clean_content(self, content):
        """Clean content by removing unwanted HTML elements and text"""
        if not content:
            return content
        
        # Remove Blogger navigation tables and widgets more aggressively
        # Remove entire table structures that contain Blogger navigation
        content = re.sub(r'\|.*?\|.*?\|.*?\|.*?\|.*?\n\|.*?---.*?\|.*?---.*?\|.*?---.*?\|.*?---.*?\|.*?\n.*?blogger\.com.*?\n', '', content, flags=re.DOTALL)
        
        # Remove Blogger navigation links
        content = re.sub(r'\[.*?\]\(https://www\.blogger\.com[^)]*\)', '', content)
        content = re.sub(r'\[.*?\]\(https://draft\.blogger\.com[^)]*\)', '', content)
        content = re.sub(r'\[.*?\]\(https://www\.google\.com[^)]*\)', '', content)
        
        # Remove Blogger widgets and navigation
        content = re.sub(r'\|.*?\|.*?\|.*?\|.*?\|.*?\n\|.*?---.*?\|.*?---.*?\|.*?---.*?\|.*?---.*?\|.*?\n.*?onboarding.*?\n', '', content, flags=re.DOTALL)
        
        # Remove unwanted HTML elements
        unwanted_patterns = [
            r'<script[^>]*>.*?</script>',
            r'<style[^>]*>.*?</style>',
            r'<iframe[^>]*>.*?</iframe>',
            r'<div[^>]*class="[^"]*(?:widget|sidebar|navigation|menu|footer|header)[^"]*"[^>]*>.*?</div>',
            r'<div[^>]*id="[^"]*(?:widget|sidebar|navigation|menu|footer|header)[^"]*"[^>]*>.*?</div>',
            r'<table[^>]*class="[^"]*(?:widget|sidebar|navigation|menu)[^"]*"[^>]*>.*?</table>',
            r'<ul[^>]*class="[^"]*(?:widget|sidebar|navigation|menu)[^"]*"[^>]*>.*?</ul>',
            r'<a[^>]*href="[^"]*(?:blogger\.com|google\.com|facebook\.com|twitter\.com|whatsapp|mailto:)[^"]*"[^>]*>.*?</a>',
            r'<img[^>]*src="[^"]*(?:blogblog\.com|gstatic\.com|googlelogo)[^"]*"[^>]*>',
            r'<div[^>]*>.*?(?:Subscribe To|Follow Us|Share with|Report Abuse|Create Blog|Sign In|Powered by).*?</div>',
            r'<div[^>]*>.*?(?:Employee Awards|Boost Morale|Workplace|WhatsApp number|Contact me|Drop a mail).*?</div>',
        ]
        
        for pattern in unwanted_patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Remove unwanted text patterns
        unwanted_text = [
            'Subscribe To VLSI EXPERT',
            'Follow Us:',
            'Share with Facebook',
            'Share with Twitter',
            'Report Abuse',
            'Create Blog',
            'Sign In',
            'Powered by',
            'Employee Awards To Boost Morale At The Workplace',
            'WhatsApp number: 9740033323',
            'Contact me on my personal WhatsApp number',
            'Drop a mail at following mail-id',
            'I always try my best to respond asap',
            'Go to Blogger.com',
            'MoreShare by email',
            'Share by email',
            'Atom',
            'Posts',
            'Comments',
            'Newer Posts',
            'Older Posts',
            'permanent link',
            'comment-form',
            'Create a Link',
            'Subscribe to: Post Comments (Atom)',
            'Subscribe to: Posts (Atom)',
            'Subscribe to: Posts (RSS)',
            'Subscribe to: Post Comments (RSS)',
            'onboarding',
            'draft.blogger.com',
        ]
        
        for text in unwanted_text:
            content = content.replace(text, '')
        
        # Remove empty table rows and excessive whitespace
        content = re.sub(r'\|.*?\|.*?\|.*?\|.*?\|.*?\n', '', content)  # Remove empty table rows
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        content = re.sub(r' +', ' ', content)
        content = content.strip()
        
        return content
    
    def extract_links_from_content(self, content):
        """Extract all article links from HTML content with improved filtering"""
        links = set()
        
        # Pattern for vlsi-expert.com article URLs (Blogger format)
        patterns = [
            r'href="(https://www\.vlsi-expert\.com/\d{4}/\d{2}/[^"]+\.html)"',
            r'href="(https://www\.vlsi-expert\.com/p/[^"]+\.html)"',
            r'href="(https://www\.vlsi-expert\.com/\d{4}/\d{2}/[^"]+)"',
            r'href="(https://www\.vlsi-expert\.com/p/[^"]+)"',
            r'href="(/\d{4}/\d{2}/[^"]+\.html)"',
            r'href="(/p/[^"]+\.html)"',
            r'href="(/\d{4}/\d{2}/[^"]+)"',
            r'href="(/p/[^"]+)"',
            # Also look for links in markdown format
            r'\[([^\]]+)\]\((https://www\.vlsi-expert\.com/[^)]+)\)',
            r'\[([^\]]+)\]\((/[^)]+)\)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                if isinstance(match, tuple):
                    # Handle markdown links
                    link = match[1]
                else:
                    link = match
                
                if link.startswith('/'):
                    link = f"https://www.vlsi-expert.com{link}"
                
                # Clean up URL
                link = link.replace('&amp;', '&')
                
                # Additional filtering for unwanted links
                if self.is_vlsi_article_url(link):
                    links.add(link)
        
        return list(links)
    
    def extract_chapter_links_from_tables(self, content):
        """Extract chapter links from table structures in content"""
        chapter_links = set()
        
        # Look for chapter table patterns
        table_patterns = [
            # Pattern for chapter tables with links
            r'<a[^>]+href="([^"]+)"[^>]*>(?:Chapter\s*\d+|[^<]+)</a>',
            # Pattern for table rows with chapter links
            r'<td[^>]*><a[^>]+href="([^"]+)"[^>]*>([^<]+)</a></td>',
            # Pattern for chapter navigation
            r'href="([^"]+)"[^>]*>(?:Introduction|Static Timing|Clock|Advance STA|Signal Integrity|EDA Tools|Timing Models|Other Topics)',
            r'href="([^"]+)"[^>]*>(?:Parasitic Interconnect|Manufacturing Effects|Dielectric Layer|Process Variation|Other Topic)',
            # Pattern for specific VLSI topics
            r'href="([^"]+)"[^>]*>(?:Timing Analysis|Setup|Hold|Skew|Propagation|Delay|Floorplan|Placement|Routing|Synthesis|Verilog|VHDL|RTL|SPEF|Parasitic|Extraction|DRC|LVS|Antenna|Clock|Power|Leakage|Dynamic|Static)',
        ]
        
        for pattern in table_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    link = match[0]
                else:
                    link = match
                
                if link.startswith('/'):
                    link = f"https://www.vlsi-expert.com{link}"
                elif not link.startswith('http'):
                    link = f"https://www.vlsi-expert.com/{link}"
                
                # Clean up URL
                link = link.replace('&amp;', '&')
                
                if self.is_vlsi_article_url(link):
                    chapter_links.add(link)
        
        return list(chapter_links)
    
    def scrape_recent_posts(self, visited_urls=None):
        """Scrape recent blog posts from archive pages"""
        if visited_urls is None:
            visited_urls = set()
            
        recent_posts = []
        current_year = datetime.now().year
        successful_scrapes = 0
        failed_scrapes = 0
        
        # Check last 3 years of posts
        for year in range(current_year, current_year - 3, -1):
            year_url = f"https://www.vlsi-expert.com/{year}/"
            
            try:
                print(f"\n📅 Checking posts from {year}...")
                print(f"🔗 Fetching: {year_url}")
                result = self.app.scrape(year_url, only_main_content=False)
                
                if result:
                    # Handle different result formats
                    if hasattr(result, 'markdown'):
                        content = result.markdown
                    elif isinstance(result, dict) and 'content' in result:
                        content = result['content']
                    else:
                        content = str(result)
                    
                    links = self.extract_links_from_content(content)
                    print(f"   Found {len(links)} links in {year}")
                    
                    for i, link in enumerate(links, 1):
                        if link not in visited_urls and self.is_vlsi_article_url(link):
                            visited_urls.add(link)
                            print(f"   🔗 [{i}/{len(links)}] Scraping: {link}")
                            print(f"      📄 Article: {link.split('/')[-1][:40]}...")
                            
                            article = self.scrape_article(link)
                            if article:
                                article['section'] = 'Blog Posts'
                                recent_posts.append(article)
                                successful_scrapes += 1
                                print(f"      ✅ SUCCESS - Added to results")
                                
                                # Save partial results periodically
                                if successful_scrapes % self.save_interval == 0:
                                    print(f"      💾 Auto-saving partial results ({successful_scrapes} articles so far)...")
                                    # Update the main results list for saving
                                    self.results = all_results.copy()
                                    self.save_partial_results()
                            else:
                                failed_scrapes += 1
                                print(f"      ❌ FAILED - No content extracted")
                            time.sleep(0.5)
                            
            except Exception as e:
                print(f"   ❌ Could not fetch {year} archive: {str(e)}")
                
        print(f"\n📊 Blog Archive Results:")
        print(f"   ✅ Successful scrapes: {successful_scrapes}")
        print(f"   ❌ Failed scrapes: {failed_scrapes}")
        print(f"   📄 Total blog posts found: {len(recent_posts)}")
                
        return recent_posts

    def scrape_with_timeout(self, url):
        """Scrape with timeout protection"""
        result = None
        error = None
        
        def scrape_worker():
            nonlocal result, error
            try:
                result = self.app.scrape(url, only_main_content=False)
            except Exception as e:
                error = e
        
        # Start scraping in a separate thread
        thread = threading.Thread(target=scrape_worker)
        thread.daemon = True
        thread.start()
        
        # Wait for completion or timeout
        thread.join(timeout=self.timeout)
        
        if thread.is_alive():
            print(f"      ⏰ TIMEOUT - Scraping took longer than {self.timeout} seconds")
            return None
        
        if error:
            raise error
        
        return result

# Main execution
if __name__ == "__main__":
    print("🔧 VLSI-Expert.com Technical Content Scraper")
    print("📝 Output Format: Markdown (.md) file only")
    print("=" * 60)
    
    # Load environment variables first
    load_dotenv()
    
    # Check for API key
    if not os.getenv("FIRECRAWL_API_KEY"):
        print("❌ Please set FIRECRAWL_API_KEY in .env file")
        exit(1)
    
    # Enable debug mode to see what's happening
    debug_mode = input("Enable debug mode? (y/n): ").lower() == 'y'
    scraper = VLSIExpertScraper(debug=debug_mode)
    
    # Check for previous state
    state = scraper.load_state()
    if state:
        print(f"📌 Previous scrape: {state['last_scrape']}")
        print(f"📌 Articles scraped: {state['total_articles']}")
    
    # Check for partial files
    partial_files = scraper.find_partial_files()
    if partial_files:
        print(f"\n📁 Found {len(partial_files)} partial result file(s):")
        for i, file in enumerate(partial_files[:3], 1):  # Show first 3
            print(f"   {i}. {file}")
        if len(partial_files) > 3:
            print(f"   ... and {len(partial_files) - 3} more")
        
        response = input("\nContinue with new scrape? (y/n): ")
        if response.lower() != 'y':
            print("Exiting. You can manually check the partial files.")
            exit(0)
    
    try:
        print("\n🚀 Starting scraping process...")
        print("📊 Console will show:")
        print("   🔗 Each URL being scraped")
        print("   ✅ Success status for each article")
        print("   ❌ Failure status for each article")
        print("   📄 Final markdown file location")
        print("   💾 Auto-save every 10 articles")
        print("\n⚠️  Interruption handling:")
        print("   Press Ctrl+C to stop gracefully")
        print("   Partial results will be saved automatically")
        print("\n" + "=" * 60)
        
        markdown_file = scraper.extract_vlsi_content()
        print("\n🎉 Extraction completed successfully!")
        print(f"📁 Final output: {os.path.abspath(markdown_file)}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Scraping interrupted by user (Ctrl+C)")
        print("✅ Partial results have been saved.")
        print("📁 Check for files starting with 'vlsi_expert_partial_'")
        
    except Exception as e:
        print(f"\n❌ Extraction failed: {str(e)}")
        import traceback
        traceback.print_exc()