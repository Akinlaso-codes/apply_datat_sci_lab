import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

listings = []

for i in range(1, 50):
  url = f'https://www.propertypro.ng/property-for-rent?page={i}'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  cards = soup.find_all('div', class_="single-room-sale listings-property")

  for card in cards:
    description = card.find("h4", class_="listings-property-title").get_text()
    type_ = card.find("h3", class_="listings-property-title2").get_text()
    price = card.find("h3", class_="listings-price").get_text().split("/")[0].replace("₦", "")
    location = card.find_all("h4")[-2].get_text()
    
    listings.append([description, type_, price, location])

    
df = pd.DataFrame(listings, columns=['Description', 'Type', 'Price', 'Location'])
print(df.head())

df.to_csv(r"C:\Users\USER\Desktop\DISCORD DATA CLASSES\propertpro1_data.csv", index=False)
