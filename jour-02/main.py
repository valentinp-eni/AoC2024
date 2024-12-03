# Chargement des données depuis le fichier "data02.txt"
# Chaque ligne est lue, divisée en nombres, et convertie en entier.
data = [[int(n) for n in line.split()] for line in open("02_input.txt").read().splitlines()]

# Fonction qui calcule les écarts entre les éléments consécutifs d'une ligne
def gaps(line):
    return [a - b for a, b in zip(line, line[1:])]

# Fonction qui vérifie si tous les écarts sont dans la plage de sécurité pour une augmentation
def safe_increase(line):
    return all(0 < g < 4 for g in gaps(line))

# Fonction qui vérifie si tous les écarts sont dans la plage de sécurité pour une diminution
def safe_decrease(line):
    return all(0 > g > -4 for g in gaps(line))

# Fonction qui détermine si une ligne est "sûre", c'est-à-dire si elle est soit en augmentation soit en diminution
def is_safe(line):
    return safe_increase(line) or safe_decrease(line)

# Calcul et affichage de la somme des lignes sûres pour la partie 1
print("Part 1:", sum(is_safe(line) for line in data))

# Fonction qui génère toutes les versions "tronquées" d'une ligne
def trimmed(line):
    return [line[:i] + line[i+1:] for i in range(len(line))]

# Calcul et affichage de la somme des lignes sûres pour la partie 2,
# en vérifiant également toutes les versions tronquées de chaque ligne
print("Part 2:", sum(any(is_safe(c) for c in [line, *trimmed(line)]) for line in data))
