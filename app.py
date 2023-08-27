from rich import print
from random import randint
from os import system

# TODO: dodać zaciąganie słowek z pliku
# dwuwymiarowa tablica ze słówkami
file_with_words = "words.txt"
# cards = [
#     ["accident", "wypadek"],
#     ["across", "przez"],
#     ["adventure", "przygoda"],
#     ["advice", "rada"],
#     ["almost", "prawie"],
#     ["alone", "sam"],
#     ["along", "wzdłóż"],
#     ["among", "pośród"],
#     ["arrive", "przybyć"],
#     ["become", "stać się"],
#     ["belong", "należeć"],
#     ["bill", "rachunek"],
#     ["blanket", "koc"],
#     ["bowl", "miska"],
#     ["broken", "złamany"]
# ]


def file_to_list(filename):
    file_name = filename
    words = open(file_name, "r")
    words_list = words.readlines()
    cards = []
    for line in words_list:
        nline = line.replace("\n", "")
        pair = nline.split(";")
        cards.append(pair)
    return cards

# lista z parami słówek
cards = file_to_list(file_with_words)

# zmienne zliczania odpowiedzi
correct = 0
incorrect = 0
if_continue = "t"

while if_continue == "t":
    for i in range(10):
        rand_card_no = randint(0, len(cards)-1)
        prompt = cards[rand_card_no][0] + " -> "
        answer = input(prompt)
        if answer == cards[rand_card_no][1]:
            print("[green]Dobrze !!!")
            correct += 1
        else:
            print("[magenta]Źle...[/magenta]")
            incorrect += 1
    
    system("clear")
    print("Prawidłowych odpowiedzi: " + str(correct))
    print("Nieprawidłowych odpowiedzi: " + str(incorrect))
    if_continue = input("Czy kontynuujemy?[t/n]: ")
    if if_continue == "n":
        break

