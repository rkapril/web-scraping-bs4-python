import bs4
import requests


def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(
        '#price')
    return elems[0].text

price = getAmazonPrice(
    'https://www.amazon.sg/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is ' + price)
