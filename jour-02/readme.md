## Explication du Code Python

1. **Chargement des données** :
   ```python
   data = [[int(n) for n in line.split()] for line in open("data02.txt").read().splitlines()]
   ```
   - Cette ligne ouvre le fichier `data02.txt`, lit son contenu, et le divise en lignes. Chaque ligne est ensuite divisée en nombres (sous forme de chaînes), convertie en entier, et stockée dans une liste de listes appelée `data`.

2. **Fonction `gaps`** :
   ```python
   def gaps(line):
       return [a - b for a, b in zip(line, line[1:])]
   ```
   - Cette fonction calcule les écarts entre chaque paire d'éléments consécutifs dans une ligne donnée. Elle utilise `zip` pour créer des paires d'éléments consécutifs et retourne une liste des différences.

3. **Fonction `safe_increase`** :
   ```python
   def safe_increase(line):
       return all(0 < g < 4 for g in gaps(line))
   ```
   - Cette fonction vérifie si tous les écarts calculés par `gaps` sont compris entre 0 et 4 (exclus). Cela signifie que la ligne est considérée comme "sûre" dans le cas d'une augmentation.

4. **Fonction `safe_decrease`** :
   ```python
   def safe_decrease(line):
       return all(0 > g > -4 for g in gaps(line))
   ```
   - De manière similaire à `safe_increase`, cette fonction vérifie si tous les écarts sont compris entre -4 et 0 (exclus), indiquant que la ligne est "sûre" dans le cas d'une diminution.

5. **Fonction `is_safe`** :
   ```python
   def is_safe(line):
       return safe_increase(line) or safe_decrease(line)
   ```
   - Cette fonction détermine si une ligne est "sûre" en vérifiant si elle répond à l'une ou l'autre des conditions de sécurité définies par `safe_increase` ou `safe_decrease`.

6. **Calcul de la somme des lignes sûres (Partie 1)** :
   ```python
   print("Part 1:", sum(is_safe(line) for line in data))
   ```
   - Ici, on utilise la fonction `is_safe` pour chaque ligne de `data`, puis on somme le nombre de lignes considérées comme sûres. Le résultat est affiché.

7. **Fonction `trimmed`** :
   ```python
   def trimmed(line):
       return [line[:i] + line[i+1:] for i in range(len(line))]
   ```
   - Cette fonction génère toutes les versions possibles d'une ligne en retirant un élément à la fois. Elle crée une nouvelle liste contenant ces lignes tronquées.

8. **Calcul de la somme des lignes sûres (Partie 2)** :
   ```python
   print("Part 2:", sum(any(is_safe(c) for c in [line, *trimmed(line)]) for line in data))
   ```
   - Pour chaque ligne dans `data`, cette partie vérifie si la ligne originale ou l'une de ses versions tronquées est sûre. La somme des lignes qui remplissent cette condition est calculée et affichée.
