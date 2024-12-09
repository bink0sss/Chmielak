import json
import os
import random
import re
# --- Menu ---
def menu():
    while True:
        print("\nSystem Zarządzania Użytkownikami")
        print("1. Dodaj użytkownika")
        print("2. Edytuj użytkownika")
        print("3. Usuń użytkownika")
        print("4. Wyświetl użytkowników")
        print("5. Wygeneruj hasło")
        print("6. Wyjście")
        choice = input("Wybierz opcję: ")

        try:
            if choice == '1':
                user_data = {
                    'name': input("Imię: "),
                    'surname': input("Nazwisko: "),
                    'pesel': input("PESEL: "),
                    'nip': input("NIP: "),
                    'regon': input("REGON: ")
                }
                add_user(user_data)
                print("Użytkownik został dodany.")
            elif choice == '2':
                user_id = int(input("Podaj ID użytkownika: "))
                updated_data = {}
                if input("Zmień imię? (t/n): ") == 't':
                    updated_data['name'] = input("Nowe imię: ")
                if input("Zmień nazwisko? (t/n): ") == 't':
                    updated_data['surname'] = input("Nowe nazwisko: ")
                edit_user(user_id, updated_data)
                print("Dane użytkownika zostały zaktualizowane.")
            elif choice == '3':
                user_id = int(input("Podaj ID użytkownika: "))
                remove_user(user_id)
                print("Użytkownik został usunięty.")
            elif choice == '4':
                users = load_users()
                print("Lista użytkowników:")
                for user in users:
                    print(user)
            elif choice == '5':
                print("Wygenerowane hasło:", generate_password())
            elif choice == '6':
                print("Zamykanie programu.")
                break
            else:
                print("Nieprawidłowy wybór.")
        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    menu()
# --- Walidacje ---
def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_control = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (sum_control % 10)) % 10
    return control_digit == int(pesel[-1])

def validate_nip(nip):
    if len(nip) != 10 or not nip.isdigit():
        return False
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    sum_control = sum(int(nip[i]) * weights[i] for i in range(9))
    control_digit = sum_control % 11
    return control_digit == int(nip[9])

def validate_regon(regon):
    if len(regon) == 9:
        weights = [8, 7, 3, 9, 1, 6, 5, 4, 3]
        sum_control = sum(int(regon[i]) * weights[i] for i in range(9))
        control_digit = sum_control % 11
        return control_digit == int(regon[-1])
    elif len(regon) == 14:
        weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7]
        sum_control = sum(int(regon[i]) * weights[i] for i in range(14))
        control_digit = sum_control % 10
        return control_digit == int(regon[-1])
    return False

# --- Zarządzanie użytkownikami ---
def load_users():
    file_path = 'data/users.json'
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)

def save_users(users):
    os.makedirs('data', exist_ok=True)
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)

def add_user(user_data):
    if not validate_pesel(user_data.get('pesel', '')):
        raise ValueError("Niepoprawny PESEL.")
    if not validate_nip(user_data.get('nip', '')):
        raise ValueError("Niepoprawny NIP.")
    if not validate_regon(user_data.get('regon', '')):
        raise ValueError("Niepoprawny REGON.")
    users = load_users()
    user_data['id'] = random.randint(0, 9999)
    users.append(user_data)
    save_users(users)

def edit_user(user_id, updated_data):
    users = load_users()
    for user in users:
        if user.get("id") == user_id:
            user.update(updated_data)
            save_users(users)
            return
    raise ValueError("Nie znaleziono użytkownika o podanym ID.")

def remove_user(user_id):
    users = load_users()
    updated_users = [user for user in users if user.get("id") != user_id]
    if len(users) == len(updated_users):
        raise ValueError("Nie znaleziono użytkownika o podanym ID.")
    save_users(updated_users)

# --- Hasła ---
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    return ''.join(random.choice(chars) for _ in range(12))

def validate_password(password):
    if len(password) < 12:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*()_+]', password):
        return False
    return True

