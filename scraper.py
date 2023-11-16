# Import necessary libraries
import requests
from bs4 import BeautifulSoup 
import re
import csv

# The URL of the website you want to scrape
url = "http://books.toscrape.com/"

# Send a GET request to the website
response = requests.get(url) 
# Check if the request was successful
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx errors

    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('article', class_='product_pod')
    
    with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability'])  # Writing headers
        
        for product in products:
            title = product.find('h3').find('a')['title'].strip()
            price = re.sub(r'[^\d.]', '', product.find('p', class_='price_color').text)
            availability = product.find('p', class_='instock availability').text.strip().split(' ')[-1]
            
            writer.writerow([title, f'£{price}', availability])
            print(f"Title: {title}")
            print(f"Price: £{price}")
            print(f"Availability: {availability}")
            print("--------------------------")

except requests.exceptions.HTTPError as err_http:
    print(f"HTTP error occurred: {err_http}")
except requests.exceptions.RequestException as err_req:
    print(f"Request exception occurred: {err_req}")
except Exception as e:
    print(f"An error occurred: {e}")