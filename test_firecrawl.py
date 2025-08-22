import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

def test_firecrawl():
    load_dotenv()
    api_key = os.getenv("FIRECRAWL_API_KEY")
    
    if not api_key:
        print("❌ No API key found in .env file")
        return
    
    print(f"🔑 API Key: {api_key[:10]}...")
    
    try:
        app = FirecrawlApp(api_key=api_key)
        print("✅ FirecrawlApp initialized successfully")
        
        # Test with a simple, fast website
        print("🌐 Testing with a simple website...")
        result = app.scrape(
            'https://httpbin.org/html',
            only_main_content=True,
            timeout=30
        )
        
        if result:
            print("✅ Scrape successful!")
            print(f"📄 Content length: {len(str(result))} characters")
            return True
        else:
            print("❌ No result returned")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_firecrawl()
