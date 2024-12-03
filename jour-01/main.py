import numpy as np

"""
01-A ------------------------------------
"""
# Charge les données depuis le fichier '01_input.txt'
d = np.loadtxt("01_input.txt")

# Trie la première colonne des données
d1 = np.sort(d[:,0])

# Trie la deuxième colonne des données
d2 = np.sort(d[:,1])

# Calcule la différence absolue entre les deux colonnes triées
d_diff = np.abs(d1 - d2)

# Somme toutes les différences absolues
result_1 = sum(d_diff)

# Affiche le résultat
print(result_1)

"""
01-B ------------------------------------
"""
# Initialise le résultat à 0
result_2 = 0

# Pour chaque élément x dans la première colonne triée
for x in d1:
    # Ajoute à result_2 le produit de x par le nombre de fois où x apparaît dans d2
    result_2 += sum(x == d2) * x

# Affiche le résultat final
print(result_2)
