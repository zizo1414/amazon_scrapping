# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:14:36 2024

@author: zeyad
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
number_ofpage = input("please enter the number of page: ")
url = f'https://www.amazon.eg/-/en/s?k=playstation+5&page={number_ofpage}&crid=1ZZ1Z3ABLLU67&qid=1725113905&sprefix=plays%2Caps%2C142&ref=sr_pg_{number_ofpage}'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'accept_language': 'en-US, en;q=0.5'}

productname = []
price = []
ship_date = []
cost_ship = []

web_page = requests.get(url, headers=HEADERS)
src = web_page.content
soup = BeautifulSoup(src, 'lxml')

# Find all product names, prices, and shipment info
product_names = soup.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
product_prices = soup.find_all('span', {'class': 'a-price-whole'})
shippments = soup.find_all('div', {'class': 'a-row s-align-children-center'})
cost_shipping = soup.find_all('div', {'class': 'a-row a-size-base a-color-secondary s-align-children-center'})

# Ensure all lists are of the same length
length = min(len(product_names), len(product_prices), len(shippments), len(cost_shipping))

for i in range(length):
    pname = product_names[i].text.strip() if len(product_names[i].text.strip()) > 1 else '^^^^'
    pprice = product_prices[i].text.strip().replace('.', '') if len(product_prices[i].text.strip()) > 1 else '^^^^^^'
    sdate = shippments[i].text.strip() if len(shippments[i].text.strip()) > 1 else '^^^^'
    ship = cost_shipping[i].text.strip() if len(cost_shipping[i].text.strip()) > 1 else '^^^^'
    productname.append(pname)
    price.append(pprice)
    ship_date.append(sdate)
    cost_ship.append(ship)

data= list(zip(productname,price,ship_date,cost_ship))

with open(r"C:\Users\zeyad\OneDrive\Desktop\amazon_scrapping.csv" , mode='w', newline='' ,encoding='utf-8')as amazon_file : 
    
    wr=csv.writer(amazon_file)
    wr.writerow(['product' , 'price' , 'shipping_date' , 'cost'])
    wr.writerows(data)
    

df= pd.DataFrame({'product' : productname , 'price' : price , 'date' : ship_date , 'cost' : cost_ship})
print(df)



