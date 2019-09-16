# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

texte = texte.replace("est", "représente")

word = "exemple"
count = texte.count(word)


print("Texte : " + texte + " Nombre d'occurences de exemple : " + str(count))


