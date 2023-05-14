#import the necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#assigned user agent for scraper
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

#creating empty array
carList = []

#creating for loop which will define URL, scrape the intended variables, push the variables back to the array 
def myCars(page):
    url = f'https://www.cars.com/shopping/results/?page={page}&page_size=100&list_price_max=&makes[]=&maximum_distance=100&models[]=&stock_type=all&zip=75287'    
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    cars = soup.find_all('div', {'class': 'vehicle-card'})
    for item in cars:
        car = {    
        'monthly': item.find('span', {'class': 'js-estimated-monthly-payment-formatted-value-with-abr'}),    
        'title': item.find('h2', {'class': 'title'}).text,
        'price': item.find('span', {'class': 'primary-price'}).text,
        'miles': item.find('div', {'class': 'miles-from'}),
        'mileage': item.find('div', {'class': 'mileage'}),
        'oneOwner': item.find('a', {'class': 'sds-link--ext'})
        }
        carList.append(car)
    return carList

#defining the pages on cars.com which need to be scraped
for x in range(196,210):
    myCars(x)

#creating dataframe to export scraped results
df = pd.DataFrame(carList)   
df.to_csv('carsList16.csv', index=False)

