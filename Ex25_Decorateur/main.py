def decorer_fonction(func):
    def fonction_locale():
        print("Je décore la fonction!")
        func()

    return fonction_locale

@decorer_fonction
def fonction_base():
    print("Je suis la fonction de base")

fonction_base()