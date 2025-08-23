import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from VlsiUniverse import VLSIUniverseCrawler

load_dotenv()

def test_single_post():
    # Test the new scraper logic
    crawler = VLSIUniverseCrawler()
    
    # Test with an actual individual blog post URL
    test_url = "https://vlsiuniverse.blogspot.com/2020/06/why-is-sum-of-setup-time-and-hold-time.html"
    
    print(f"Testing URL with new scraper logic: {test_url}")
    
    try:
        post_data = crawler.scrape_individual_post(test_url)
        
        if post_data:
            print("\n✅ Successfully extracted blog post!")
            print(f"Title: {post_data['title']}")
            print(f"Date: {post_data['date']}")
            print(f"Year: {post_data['year']}")
            print(f"Content length: {len(post_data['content'])}")
            print(f"\nFirst 500 characters of content:")
            print("=" * 50)
            print(post_data['content'][:500])
            print("=" * 50)
        else:
            print("❌ Failed to extract blog post content")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_single_post()
