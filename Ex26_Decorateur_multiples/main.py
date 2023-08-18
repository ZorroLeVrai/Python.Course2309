def message(message = ""):
    def decorateur_interne(func):
        def fonction_locale(*args, **kwargs):
            if (message == ""):
                print("Je décore la fonction !")
            else:
                print(f"J'écris un message personnalisé: {message}")
            func(*args, **kwargs)
        
        return fonction_locale
    return decorateur_interne

@message()
@message("Message perso")
def function_base():
    print("Je suis la fonction de base")

function_base()