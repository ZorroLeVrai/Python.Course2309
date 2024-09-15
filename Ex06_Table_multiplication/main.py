print("Affichage d'une table de multiplication de 1 à N")
table_size = int(input("Saisir N: "))
nb_padding_chars = 5

# imprimer l'entête
for num in range(1, 11):
    print(f"{num:{nb_padding_chars}}", end='')

print()
# imprimer une ligne de séparation
print("-"*10*nb_padding_chars)

# imprimer la table de multiplication
for i in range(1, table_size + 1):
    for j in range(1, 11):
        print(f"{i*j:{nb_padding_chars}}", end='')
    print()
