import re  # Importation du module 're' pour les expressions régulières

# Compilation des expressions régulières pour les instructions 'mul' et 'don't ... do'
R1 = re.compile(r"mul\((\d+),(\d+)\)")  # R1 correspond à l'instruction 'mul(a, b)' où a et b sont des nombres
R2 = re.compile(r"don't\(\).*?do\(\)", re.DOTALL)  # R2 correspond à 'don't(...) do(...)', capturant tout entre les deux

def part1(data):
    """
    Calcule la somme des produits pour toutes les instructions 'mul' présentes dans les données.
    
    Args:
        data (str): Les données d'entrée sous forme de chaîne de caractères.
        
    Returns:
        int: La somme des produits des paires de nombres trouvées dans les instructions 'mul'.
    """
    return sum(int(a) * int(b) for a, b in R1.findall(data))  # Trouve toutes les paires (a, b) et calcule leur produit

def part2(data):
    """
    Calcule la somme des produits pour toutes les instructions 'mul' après avoir supprimé
    les instructions 'don't ... do' de l'entrée.
    
    Args:
        data (str): Les données d'entrée sous forme de chaîne de caractères.
        
    Returns:
        int: La somme des produits des paires de nombres trouvées dans les instructions 'mul'
              après suppression des instructions 'don't ... do'.
    """
    return part1(R2.sub("", data + "do()"))  # Supprime les instructions 'don't ... do' et ajoute 'do()' pour éviter une erreur

# Lecture du fichier d'entrée et stockage du contenu dans la variable 'data'
data = open('03_input.txt').read()

# Affichage des résultats pour la partie 1 et la partie 2
print(part1(data), part2(data))
