# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import requests
from bs4 import BeautifulSoup


def print_hi():
    soup = None
    a = random.randint(1, 603)
    while a % 2 == 0:
        a = random.randint(1, 603)
    # Use a breakpoint in the code line below to debug your script.
    try:
        page = requests.get(f"https://www.aviny.com/استخاره/{a}")
        soup = BeautifulSoup(page.text, 'html.parser').find('div', {
            "class": "field field--name-field-natije field--type-string-long field--label-inline clearfix"})
    except NameError:
        print(f"cant access aviny because {NameError}")
    print(f'Hi, {a}')  # Press ⌘F8 to toggle the breakpoint.
    if soup is not None:
        print(soup.text.rstrip())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
