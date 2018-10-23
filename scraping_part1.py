import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from csv import writer, DictWriter

BASE_URL = "http://quotes.toscrape.com/"

def get_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
            "text" : quote.find(class_="text").get_text(),
            "author" : quote.find(class_="author").get_text(),
            "bio-link" : quote.find("a")["href"]
            })

        new_page = soup.find(class_="next")
        url = new_page.find("a")["href"] if new_page else None
        sleep(2)
    return all_quotes


def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = get_quotes()
write_quotes(quotes)
