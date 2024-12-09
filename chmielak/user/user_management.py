import json
import random
import re
import os
from datetime import datetime

# Funkcja dodawania użytkownika
def add_user():
    user_data = {}

    # Wprowadzenie danych przez użytkownika
    user_data['id'] = int(input("Podaj ID użytkownika: "))
    user_data['name'] = input("Podaj imię i nazwisko użytkownika: ")
    user_data['nip'] = input("Podaj numer NIP: ")
    user_data['pesel'] = input("Podaj numer PESEL: ")
    user_data['regon'] = input("Podaj numer REGON: ")
    user_data['email'] = input("Podaj adres email: ")

    # Walidacja NIP, PESEL, REGON
    if not validate_nip(user_data.get('nip')):
        return "NIP jest niepoprawny"
    if not validate_pesel(user_data.get('pesel')):
        return "PESEL jest niepoprawny"
    if not validate_regon(user_data.get('regon')):
        return "REGON jest niepoprawny"
    
    # Odczytanie istniejących użytkowników z pliku
    users = load_users()
    
    # Dodanie nowego użytkownika
    users.append(user_data)
    
    # Zapisanie danych do pliku
    save_users(users)
    return "Użytkownik został dodany"

# Funkcja edytowania użytkownika
def edit_user(user_id, updated_data):
    # Odczytanie użytkowników
    users = load_users()
    
    # Znalezienie użytkownika i aktualizacja danych
    for user in users:
        if user['id'] == user_id:
            user.update(updated_data)
            break
    
    # Zapisanie zmodyfikowanych danych
    save_users(users)
    return "Dane użytkownika zostały zaktualizowane"

# Funkcja usuwania użytkownika
def remove_user(user_id):
    # Odczytanie użytkowników
    users = load_users()
    
    # Usunięcie użytkownika
    users = [user for user in users if user['id'] != user_id]
    
    # Zapisanie zmodyfikowanych danych
    save_users(users)
    return "Użytkownik został usunięty"

# Funkcja wczytywania użytkowników z pliku
def load_users():
    if not os.path.exists('data/users.json'):
        # Jeśli plik nie istnieje, utwórz go
        save_users([])
        return []
    
    with open('data/users.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Funkcja zapisywania użytkowników do pliku
def save_users(users):
    if not os.path.exists('data'):
        os.makedirs('data')  # Tworzy katalog 'data' jeśli nie istnieje
    with open('data/users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

# Funkcja walidacji NIP
def validate_nip(nip):
    if len(nip) != 10 or not nip.isdigit():
        return False
    
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    check_sum = sum(int(nip[i]) * weights[i] for i in range(9))
    control_digit = check_sum % 11
    return control_digit == int(nip[-1])

# Funkcja walidacji PESEL
def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    
    # Sprawdzanie daty urodzenia
    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    
    # Data urodzenia powinna być poprawna
    try:
        datetime(year=year, month=month, day=day)
    except ValueError:
        return False
    
    # Walidacja sumy kontrolnej
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    check_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = 10 - (check_sum % 10) if check_sum % 10 != 0 else 0
    return control_digit == int(pesel[-1])

# Funkcja walidacji REGON
def validate_regon(regon):
    if len(regon) not in [9, 14] or not regon.isdigit():
        return False
    
    # Wagi do obliczeń sumy kontrolnej
    if len(regon) == 9:
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
    else:  # REGON 14-cyfrowy
        weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7]
    
    check_sum = sum(int(regon[i]) * weights[i] for i in range(len(regon) - 1))
    control_digit = check_sum % 11
    return control_digit == int(regon[-1])

# Funkcja generująca silne hasło
def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;:,.<>?"
    password = ''.join(random.choice(characters) for i in range(12))
    return password

# Funkcja walidująca siłę hasła
def validate_password(password):
    if len(password) < 12:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Przykład użycia
if __name__ == "__main__":
    print("Wybierz akcję:")
    print("1. Dodaj użytkownika")
    print("2. Edytuj użytkownika")
    print("3. Usuń użytkownika")

    choice = input("Wybierz numer akcji: ")

    if choice == "1":
        print(add_user())  # Dodanie użytkownika
    elif choice == "2":
        user_id = int(input("Podaj ID użytkownika do edycji: "))
        updated_data = {
            'name': input("Podaj nowe imię i nazwisko użytkownika: "),
            'email': input("Podaj nowy adres email: ")
        }
        print(edit_user(user_id, updated_data))  # Edytowanie użytkownika
    elif choice == "3":
        user_id = int(input("Podaj ID użytkownika do usunięcia: "))
        print(remove_user(user_id))  # Usuwanie użytkownika
    else:
        print("Nieprawidłowa akcja.")
