from bs4 import BeautifulSoup
import requests 

def get_prices_individual_oils(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    list_oils = soup.find_all('a',class_='title')
    for oil in list_oils:
        print(oil.text)


# Main
url = 'https://www.doterra.com/CO/es_CO/pl/single-oils?q=%3Aname-asc&page=0&sort=name-asc'
get_prices_individual_oils(url)
