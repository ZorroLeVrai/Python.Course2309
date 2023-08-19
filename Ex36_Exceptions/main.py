import re

class LoginBadFormatException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PasswordBadFormatException(Exception):
    def __init__(self, message):
        super().__init__(message)

def saisir_lettre_minuscules():
    text = input("Veuillez entrer un login SVP (celui-ci ne doit posséder que des lettres minuscules): ")
    min_ascii_code = ord('a')
    max_ascii_code = ord('z')
    condition = len(text) > 0 and all(map(lambda l: min_ascii_code <= ord(l) <= max_ascii_code, text))
    if not condition:
        raise LoginBadFormatException("Le login ne doit contenir que des minuscules et ne doit pas être vide")
    return text

def saisir_lettre_minuscules2():
    text = input("Veuillez entrer un login SVP (celui-ci ne doit posséder que des lettres minuscules): ")
    condition = bool(re.match("^[a-z]+$", text))
    if not condition:
        raise LoginBadFormatException("Le login ne doit contenir que des minuscules et ne doit pas être vide")
    return text
    
def saisir_chiffres():
    text = input("Veuillez entrer un mot de passe SVP (celui-ci ne devra comporter que des chiffres): ")
    if not text.isdigit():
        raise PasswordBadFormatException("Le mot de passe ne doit contenir que des chiffres")
    return text

login = ""
password = ""
while True:
    try:
        login = saisir_lettre_minuscules2()
        password = saisir_chiffres()
    except Exception as ex:
        print(f"Exception: {ex}")
        print()
    else:
        print("Saisie correcte")
        print(f"Login: {login}")
        print(f"Password: {password}")
        break
