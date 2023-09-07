file_name = "fizzBuzz.txt"

def fizz_buzz(n):
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result if result else str(n)

def create_fb_list(debut, fin):
    #return list(map(lambda n:fizz_buzz(n),range(debut, fin+1)))
    return [fizz_buzz(el) for el in range(debut, fin+1)]

def print_in_file(text, file_name):
    with open(file_name, "wt") as file:
        file.write(text)

def input_int(message):
    while True:
        try:
            return int(input(f"{message} "))
        except:
            print("Vous devez saisir un entier\n")


nb_depart = input_int("Saisissez le nombre de départ:")
nb_fin = input_int("Saisissez le nombre de fin:")
fizzBuzz_list = create_fb_list(nb_depart, nb_fin)
print_in_file("\n".join(fizzBuzz_list), file_name)
