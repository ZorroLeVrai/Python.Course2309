def decorateur(fruit):
    def decorateur_interne(func):
        def fonction_locale(*args, **kwargs):
            print("Dans la fonction interne")
            print(f"J'aime ce fruit: {fruit}")
            func(*args, **kwargs)
        
        return fonction_locale
    return decorateur_interne

@decorateur(fruit="Fraise")
@decorateur(fruit="Banane")
def my_func(message):
    print(message)

my_func("Dans la fonction de base")