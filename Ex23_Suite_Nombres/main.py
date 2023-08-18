message_error_nombre_saisi = "Le nombre saisi doit être un entier positif"

def creer_chaine_caracteres(*args):
    arg_list = map(lambda x: str(x), args)
    return "-".join(arg_list)

def run():
    num_list = []
    while True:
        num_str = input("Entrez un nombre entier positif (une chaine vide permet de générer la chaine de caractères): ")
        if num_str == "":
            print(creer_chaine_caracteres(*num_list))
            return
        
        try:
            num = int(num_str)
            if num < 0:
                print(message_error_nombre_saisi)
                continue
        except ValueError:
            print(message_error_nombre_saisi)
            continue

        num_list.append(num)

run()