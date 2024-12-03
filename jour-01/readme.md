## Explication du Code Python

### Importation de NumPy

```python
import numpy as np
```
Cette ligne importe la bibliothèque NumPy, qui est essentielle pour le traitement efficace des tableaux et des opérations mathématiques en Python.

### Partie 01-A

1. **Chargement des données**
   ```python
   d = np.loadtxt("01_input.txt")
   ```
   - Cette ligne charge les données à partir d'un fichier texte nommé `01_input.txt` et les stocke dans un tableau NumPy `d`. Chaque ligne du fichier devient un enregistrement dans le tableau.

2. **Tri de la première colonne**
   ```python
   d1 = np.sort(d[:,0])
   ```
   - Ici, la première colonne de `d` est extraite (tous les éléments de la première colonne) et triée. Le résultat trié est stocké dans `d1`.

3. **Tri de la deuxième colonne**
   ```python
   d2 = np.sort(d[:,1])
   ```
   - De manière similaire, cette ligne extrait et trie la deuxième colonne de `d`, stockant le résultat dans `d2`.

4. **Calcul de la différence absolue**
   ```python
   d_diff = np.abs(d1 - d2)
   ```
   - Cette ligne calcule la différence absolue entre les éléments correspondants de `d1` et `d2`. Le résultat est un tableau contenant les différences absolues.

5. **Somme des différences**
   ```python
   result_1 = sum(d_diff)
   ```
   - Ici, toutes les différences absolues sont additionnées pour obtenir un seul résultat, `result_1`, qui représente la somme totale des différences.

6. **Affichage du résultat**
   ```python
   print(result_1)
   ```
   - Cette ligne affiche le résultat final de la somme des différences.

### Résumé de la Partie 01-A

Cette section calcule la somme des différences absolues entre les éléments triés des deux colonnes du fichier d'entrée.

---

### Partie 01-B

1. **Initialisation du résultat**
   ```python
   result_2 = 0
   ```
   - Une variable `result_2` est initialisée à zéro pour stocker le résultat final de cette partie.

2. **Boucle à travers les éléments de `d1`**
   ```python
   for x in d1:
   ```
   - Cette boucle parcourt chaque élément `x` dans le tableau trié `d1`.

3. **Calcul du produit avec occurrences**
   ```python
   result_2 += sum(x == d2) * x
   ```
   - Pour chaque élément `x`, cette ligne :
     - Compte combien de fois `x` apparaît dans `d2` (avec `sum(x == d2)`)
     - Multiplie ce compte par la valeur de `x`
     - Ajoute le produit à `result_2`

4. **Affichage du résultat final**
   ```python
   print(result_2)
   ```
   - Cette ligne affiche le résultat final, qui est la somme des produits entre chaque élément de `d1` et son nombre d'occurrences dans `d2`.

### Résumé de la Partie 01-B

Cette section calcule une somme pondérée où chaque élément de `d1` est multiplié par le nombre de fois qu'il apparaît dans `d2`.
