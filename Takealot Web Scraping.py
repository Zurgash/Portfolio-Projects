from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os

def find_primary_image(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Set up the Chrome driver service
    service = Service(r'C:\Users\jaunv\Downloads\chromedriver-win64\chromedriver.exe')

    # Initialize the Chrome webdriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Load the URL
    driver.get(url)

    # Get the page source
    page_source = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the image element
    primary_image = soup.find("div", class_="image-box")

    # Extract the image URL
    if primary_image:
        image_url = primary_image.find("img")["src"]
    else:
        image_url = None

    # Close the webdriver
    driver.quit()

    return image_url

def download_image(image_url, output_folder):
    # Get the image filename
    filename = os.path.basename(image_url)
    
    # Download the image
    response = requests.get(image_url)
    
    # Save the image
    with open(os.path.join(output_folder, filename), 'wb') as f:
        f.write(response.content)

# List of URLs
urls = [ "https://www.takealot.com/x/PLID40687415"
# A list of 5000 URLS were in the original code, However due to the sensitivity 
# I will not be sharing it here.
# Here is a random product URL form Takealot for example use.
 
]

# Output folder to save the images
output_folder = "C:\\Users\\jaunv\\Downloads\\images"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through the URLs
for url in urls:
    # Get the primary image URL
    primary_image_url = find_primary_image(url)
    
    if primary_image_url:
        # Download and save the image
        download_image(primary_image_url, output_folder)
        print(f"Image downloaded from {url} and saved successfully.")
    else:
        print(f"No image found on {url}.")