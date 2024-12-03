## Explication du Code Python

1. **Importation du Module `re`** :
   - Le module `re` est importé pour permettre l'utilisation d'expressions régulières, qui sont utiles pour rechercher et manipuler des chaînes de caractères.

2. **Compilation des Expressions Régulières** :
   - `R1` : Cette expression régulière est utilisée pour trouver toutes les occurrences d'instructions `mul(a, b)`, où `a` et `b` sont des nombres. Les parenthèses capturent ces nombres pour une utilisation ultérieure.
   - `R2` : Cette expression régulière capture toute instruction commençant par `don't(` et se terminant par `do(`, en incluant tout le contenu entre les deux. L'option `re.DOTALL` permet à l'expression de capturer également les nouvelles lignes.

3. **Fonction `part1`** :
   - Cette fonction prend une chaîne de caractères `data` en entrée.
   - Elle utilise `R1.findall(data)` pour trouver toutes les paires `(a, b)` dans les instructions `mul`.
   - Pour chaque paire trouvée, elle calcule le produit de `a` et `b`, puis retourne la somme totale.

4. **Fonction `part2`** :
   - Cette fonction prend également une chaîne de caractères `data` en entrée.
   - Elle utilise `R2.sub("", data + "do()")` pour supprimer toutes les instructions `don't ... do` du texte, tout en ajoutant une instruction vide `do()` à la fin. Cela évite d'avoir une chaîne vide qui pourrait causer une erreur lors de l'analyse.
   - Ensuite, elle appelle la fonction `part1` sur le texte modifié pour obtenir la somme des produits.

5. **Lecture du Fichier d'Entrée** :
   - Le fichier nommé `03_input.txt` est ouvert et son contenu est lu dans la variable `data`.

6. **Affichage des Résultats** :
   - Les résultats des fonctions `part1(data)` et `part2(data)` sont imprimés, affichant respectivement la somme des produits trouvés dans le texte original et après suppression des instructions indésirables.
