import random
import string

def generate_unique_email():
    """
    Генерирует уникальный email в формате: sergei_platonov_42_3цифры@yandex.ru
    """
    first_name = "sergei"
    last_name = "platonov"
    cohort = "42"
    digits = ''.join(random.choices(string.digits, k=4)) #добавил 4 цифры, т.к. 3 мало
    domain = "yandex.ru"
    
    email = f"{first_name}_{last_name}_{cohort}_{digits}@{domain}"
    return email

def generate_password(length=6):
    """
    Генерирует пароль указанной длины
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password
