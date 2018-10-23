import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def play_quote_game(quotes):
    print("Welcome to our quote guessing game. Do you want to play? y(yes) / n(no)")
    answer = input(">>>")
    while answer.lower() in ("yes", "y"):
        random_dict = choice(quotes)
        print(random_dict["text"])
        about = random_dict["bio-link"][1:]
        res = requests.get(f"{BASE_URL}{about}")
        soup = BeautifulSoup(res.text, "html.parser")
        date = soup.find(class_="author-born-date").get_text()
        city = soup.find(class_="author-born-location").get_text()
        author = random_dict["author"]
        first_initial = author.split()[0][0]
        last_initial = author.split()[1][0]
        additional_info = [f"This person was born on {date} {city}",
                           f"Her/His first name starts on letter {first_initial}",
                           f"Her/His last name starts on letter {last_initial}",
                           f"You lost. It was said by {author}"]
        print("Who said this? You've got 4 chances.")
        for i in range(4):
            answer = input(">>> ")
            if answer.lower() != random_dict["author"].lower():
                print(f"Guesses remaining: {3-i}")
                print(additional_info[i])
            else:
                print("You won!")
        return play_quote_game(quotes)
quotes = read_quotes("quotes.csv")
play_quote_game(quotes)
