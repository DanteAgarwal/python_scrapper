# Web Scraping Project

## Overview
This project focuses on web scraping using Python's Beautiful Soup library to extract information from a website. The script retrieves data about books listed on a specific webpage and saves it to a CSV file.

## Prerequisites
- Python 3.x
- Necessary Python libraries: `requests`, `beautifulsoup4`

## Installation
1. Clone the repository or download the project files.
2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
## Usage
Open the web_scraper.py file.
Set the url variable to the URL of the webpage you want to scrape.
Run the web_scraper.py script.
The extracted data will be stored in a CSV file named scraped_data.csv in the project directory.
## Project Structure
```bash
Copy code
- web_scraper.py         # Python script for web scraping
- README.md              # Project documentation (you're reading it!)
- scraped_data.csv       # CSV file containing extracted data
```
## Script Details
### web_scraper.py:
Imports necessary libraries: requests, BeautifulSoup, csv, re.
Fetches HTML content from a specified URL.
Scrapes book information (title, price, availability) using Beautiful Soup.
Cleans the extracted data for consistency and stores it in a CSV file.
Includes error handling for HTTP requests and exceptions.
### Error Handling
The script employs a try-except block to catch various exceptions:
requests.exceptions.HTTPError: Handles HTTP errors (4xx or 5xx status codes).
requests.exceptions.RequestException: Catches general request exceptions.
Exception: Provides a catch-all for any other unexpected errors.
## Contributing
Contributions to improve or extend this project are welcome! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Disclaimer
This project was created for educational purposes. Respect the terms of service and permissions of the websites you scrape.

## Contact
For any questions or suggestions, feel free to contact the project maintainer at Akshatgoyal292@gamil.com.
