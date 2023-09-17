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

Usage
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/website-sitemap-scraper.git
Navigate to the project directory:

bash
Copy code
cd website-sitemap-scraper
Run the script:

bash
Copy code
python sitemap_scraper.py
Follow the on-screen instructions to provide the URL of the website you want to scrape.

If a sitemap is found on the website, the script will fetch and save the sitemap links to a text file named <website-name>_sitemap_links.txt.

Getting Started
To get started with this project, follow the usage instructions above. Feel free to customize and enhance the script to meet your specific requirements.

Contributing
Contributions are welcome! If you have any ideas, bug fixes, or improvements, please open an issue or create a pull request. Follow these steps to contribute:

Fork the repository.
Create your feature branch: git checkout -b feature/my-feature.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/my-feature.
Submit a pull request.

