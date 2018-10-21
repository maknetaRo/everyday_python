import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep


all_quotes = []
base_url = "http://quotes.toscrape.com/"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
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

one_time = []
for elem in all_quotes:
    for key, value in elem.items():
        if elem["author"] not in one_time:
            one_time.append(elem["author"])
print(one_time)

print("Welcome to our quote guessing game. Do you want to play? y(yes) / n(no)")
answer = input(">>>")
while answer.lower() in ("yes", "y"):
    random_dict = choice(all_quotes)
    print(random_dict["text"])
    about = random_dict["bio-link"][1:]
    res = requests.get(f"{base_url}{about}")
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
            print(" Do you want to play again? y(yes) / n(no)")
            answer = input(">>>")
            if answer.lower in ('no', 'n'):
                break
