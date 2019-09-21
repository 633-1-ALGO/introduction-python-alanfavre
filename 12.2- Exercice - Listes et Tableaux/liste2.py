# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

max_value = 0
index_n = 0
index_m = 0

for i in range(0, len(tab)):
    for y in range(0, len(tab[i])):
        if tab[i][y] > max_value:
            max_value = tab[i][y]
            index_n = i
            index_m = y

print("La valeur maximum est : " + str(max_value) + " et elle se trouve à l'indice : [" + str(index_n) + "][" + str(index_m) + "].")


