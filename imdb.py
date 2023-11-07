# -*- coding: utf-8 -*-
# Created on Thu Oct 19 14:39:33 2023

#@author: zeyad


'''
import requests 
import csv
from bs4 import BeautifulSoup

url= r'https://twitter.com/DrLoupis/status/1714724578797515077'
page= requests.get(url)
src=page.content
soup=BeautifulSoup(src,'lxml')


job_title=soup.find_all('span', {'class':"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
 
print(job_title)
 '''




 
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver executable
url = 'https://twitter.com/DrLoupis/status/1714724578797515077'
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust the sleep duration as needed

# Get the page source
src = driver.page_source

# Close the Selenium WebDriver
driver.quit()

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(src, 'lxml')

# Find the desired elements using BeautifulSoup
job_titles = soup.find_all('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

# Print the job titles
for job_title in job_titles:
    print(job_title.get_text(strip=True))
    
'''
import requests
import selenium

from bs4 import BeautifulSoup

# Make a request to the Wikipedia article on Egypt
response = requests.get('https://en.wikipedia.org/wiki/Egypt')

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text from the article body
article_text = soup.find('div', class_='mw-parser-output').text

        driver.get.find_element_path()

# Print the article text
print(article_text)



 





















    
    
    
    
    
    