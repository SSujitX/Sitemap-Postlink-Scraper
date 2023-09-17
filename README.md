# Website Sitemap Scraper

The Website Sitemap Scraper is a Python script that allows you to fetch and extract sitemap links from a website. This tool is useful for collecting information about a website's structure and content.

## Features

- Fetches sitemap links from a specified website.
- Saves the sitemap links to a text file for future reference.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your system.
- The following Python libraries installed:
  - `httpx`: Used for making asynchronous HTTP requests.
  - `selectolax`: Used for parsing HTML/XML content.
  
You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage
Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/Sitemap-Postlink-Scraper.git

Navigate to the project directory:

```bash
cd website-sitemap-scraper

Run the script:
```bash
python sitemap_scraper.py

Follow the on-screen instructions to provide the URL of the website you want to scrape.

If a sitemap is found on the website, the script will fetch and save the sitemap links to a text file named <website-name>_sitemap_links.txt.









