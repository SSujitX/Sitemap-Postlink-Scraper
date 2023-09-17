import httpx
from selectolax.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import asyncio
import os,sys

root_path = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(root_path)

async def fetch_sitemap(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
        except httpx.RequestError as e:
            print(f"Request error: {e}")
            return None

def parse_sitemap(xml_content):
    parser = HTMLParser(xml_content)
    links = []
    for element in parser.css("loc"):
        links.append(element.text())
    return links

async def check_and_save_sitemap_links(website_link):
    post_sitemap_url = urljoin(website_link, "post-sitemap.xml")
    sitemap_content = await fetch_sitemap(post_sitemap_url)
    
    if sitemap_content:
        links = parse_sitemap(sitemap_content)
        if links:
            website_name = urlparse(website_link).netloc
            with open(f"{website_name}_sitemap_links.txt", "w") as f:
                for link in links:
                    f.write(link + "\n")
            print("Sitemap links saved to sitemap_links.txt")
        else:
            print("Sitemap is empty.")
    else:
        print("No sitemap found.")

async def main():
    website_link = input('Enter Website Link:')
    await check_and_save_sitemap_links(website_link)

if __name__ == "__main__":
    asyncio.run(main())
