import json
import os 
import re
import random

# Function that validates PESEl, NIP, REGON
def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_control = sum(int(pesel[i]) * weights[i] for i in range(10))
    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    return sum_control % 10 == 0

def validate_nip(nip):
    if len(nip) != 10 or not nip.isdigit():
        return False

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    sum_control = sum(int(nip[i]) * weights[i] for i in range(9))
    
    return sum_control % 11 == int(nip[9]) % 11

def validate_regon(regon):
    if len(regon) == 9:
        weights = [8, 7, 3, 9, 1, 6, 5, 4, 3]
        sum_control = sum(int(regon[i]) * weights[i] for i in range(9))
        return sum_control % 11 == 0
    elif len(regon) == 14:
        weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7]
        sum_control = sum(int(regon[i]) * weights[i] for i in range(14))
        return sum_control % 10 == 0
    return False
def add_user(user_data):
    file_path = 'data/users.json'

    