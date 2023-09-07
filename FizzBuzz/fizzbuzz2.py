file_name = "fizzBuzz.txt"

def fizz_buzz(n):
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    #return result if result else n
    if result == "":
        return n
    else:
        return result
    
def fizz_buzz2(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

def create_fb_list(debut, fin):
    #return [fizz_buzz(el) for el in range(debut, fin+1)]
    result = []
    for el in range(debut, fin+1):
        result.append(fizz_buzz2(el))
    return result

def print_in_file(lst, file_name):
    with open(file_name, "wt") as file:
        for item in lst:
            file.write(str(item) + "\n")

def input_int(message):
    while True:
        try:
            return int(input(f"{message} "))
        except:
            print("Vous devez saisir un entier\n")

if __name__ == "__main__":
    nb_depart = input_int("Saisissez le nombre de départ:")
    nb_fin = input_int("Saisissez le nombre de fin:")
    fizzBuzz_list = create_fb_list(nb_depart, nb_fin)
    print_in_file(fizzBuzz_list, file_name)
