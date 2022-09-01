from random import *
import json

films = []


def save():
    with open("films.Json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("FilmBase saved successfully in Films.json")


def load():
    with open("films.Json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("FilmBase loaded successfully.")


try:
    with open("films.Json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("FilmBase loaded successfully.")
except:
    films.append("Maxtix")
    films.append("Sollaris")
    films.append("Lord of the Rings")
    films.append("Chainsaw from Texxas")
    films.append("Santa Barbara")

while True:
    command = input("Input command ")
    if command == "/start":
        print("FilmBot started")
    elif command == "/stop":
        print("Stopping FilmBot. Waiting for you!")
        break
    elif command == "/all":
        print("Films list: ")
        print(films)
    elif command == "/add":
        f = input("Input Film name ")
        films.append(f)
        print("Film added successfully")
    elif command == "/help":
        print("Manual should be here")
    elif command == "/del":
        f = input("Input Film name for removal ")
        if f in films:
            films.remove(f)
            print("Film removed successfully")
        else:
            print("No such film in database")
    elif command == "/random":
        # rnd=randint(0, len(films)-1)
        # print("Random film: " + films[rnd])
        print("Random film: " + choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Unknown command. Please review manual via /help")
