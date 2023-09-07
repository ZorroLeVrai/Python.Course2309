eleves = { 
    "John": (15, "Math"),
    "Kevin": (9, "IT"),
    "Georges": (13, "Anglais"),
    "Bob": (18, "IT"),
    "Sarah": (12, "Math"),
    "Johnny": (8, "IT"),
    "Alison": (13, "IT"),
    "Cindy": (12, "Sport"),
    "Jane": (15, "Anglais"),
    "Tom": (8, "IT")
}

# for elem in eleves.items():
#     print(elem)
#     print("elem[0]", elem[0])
#     print("elem[1]", elem[1])
#     print("elem[1][0]", elem[1][0])
#     print("elem[1][1]", elem[1][1])
#     print("\n"*2)

resultat = filter(lambda elem: elem[1][0] >= 12 and elem[1][1] == "IT", eleves.items())
resultat = map(lambda item:item[0], resultat)
print(list(resultat))