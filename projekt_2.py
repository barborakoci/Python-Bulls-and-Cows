"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Kočí
email: barbora.koci@email.cz
discord: barca6493
"""
"""
import random

def generate_secret_number():
    while True:
        secret_number = ''.join(random.sample('123456789', 4))
        if secret_number[0] != '0':
            return secret_number

def count_bulls_and_cows(secret_number, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def main():
    print("Welcome to Bulls and Cows!")
    secret_number = generate_secret_number()
    attempts = 0
    
    while True:
        guess = input("Enter your guess (4-digit number with non-repeating digits): ")
        
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4 or guess[0] == '0':
            print("Invalid input. Please enter a 4-digit number with non-repeating digits that doesn't start with 0.")
            continue
        
        attempts += 1
        bulls, cows = count_bulls_and_cows(secret_number, guess)
        
        if bulls == 4:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        else:
            print(f"{bulls} bulls, {cows} cows")

if __name__ == "__main__":
    main()
"""  
import random

def generuj_cislo():
    while True:
        cislo = ''.join(random.sample('0123456789', 4))
        if cislo[0] != '0':
            return cislo

def vyhodnot_pokus(cislo, pokus):
    bulls = sum(cislo[i] == pokus[i] for i in range(4))
    cows = sum(cislo.count(pokus[i]) for i in range(4)) - bulls
    return bulls, cows

def over_platnost_pokusu(pokus):
    if len(pokus) != 4 or not pokus.isdigit():
        return False
    if pokus[0] == '0' or len(set(pokus)) < 4:
        return False
    return True

def spust_hru():
    cislo = generuj_cislo()
    pocet_pokusu = 0
    print("Vítej ve hře Bulls and Cows!")
    print("Hádej 4místné číslo.") 
    print("Pravidla: Číslice se neopakují. První číslice není 0.")
    
    while True:
        pokus = input("Zadej 4místné číslo: ")
        if not over_platnost_pokusu(pokus):
            print("Neplatný pokus. Zadej číslo podle pravidel.")
            continue
        
        pocet_pokusu += 1
        bulls, cows = vyhodnot_pokus(cislo, pokus)
        if bulls == 4:
            print(f"Výborně! Číslo {cislo} je správně. Počet pokusů: {pocet_pokusu}.")
            break
        else:
            if bulls != 1 and cows != 1:
                print(f"{bulls} Bulls, {cows} Cows")
            elif bulls == 1 and cows != 1:
                print(f"{bulls} Bull, {cows} Cows")
            elif bulls != 1 and cows == 1:
                print(f"{bulls} Bulls, {cows} Cow")
            elif bulls == 1 and cows == 1:
                print(f"{bulls} Bull, {cows} Cow")

if __name__ == "__main__":
    spust_hru()
