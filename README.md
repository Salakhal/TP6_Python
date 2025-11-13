# TP 6 : Dataclasses :

# Exercice 1 : Classe Livre

## Objectif pédagogique
- Comprendre l’usage du décorateur `@dataclass` pour simplifier la définition de classes.  
- Créer des objets immuables et optimisés (`frozen=True`, `slots=True`).  
- Sérialiser des objets en JSON avec `asdict()`.  
- Comparer et manipuler des objets facilement.

## Sortie attendue (JSON)
```
{"titre": "1984", "auteur": "George Orwell", "annee": 1949, "prix": 7.9}
{"titre": "1984", "auteur": "George Orwell", "annee": 1949, "prix": 9.9}
{"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee": 1943, "prix": 12.5}
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="1338" height="113" alt="image" src="https://github.com/user-attachments/assets/50257037-aa44-41ed-936b-c546d1dadec8" />

# Exercice 2 : Classe Film

## Objectif pédagogique
- Approfondir l’utilisation des `dataclasses` pour modéliser des entités métier réelles.  
- Créer des objets immuables et optimisés (`frozen=True`, `slots=True`).  
- Sérialiser des objets en JSON et les recharger facilement.  
- Comparer et trier des objets selon un attribut spécifique (note).  

## Classe Film (spécifications)
- Champs :  
  - `titre` : str  
  - `realisateur` : str  
  - `annee` : int  
  - `note` : float (0 à 10)  
- Méthodes :  
  - `to_json()` : retourne la représentation JSON complète du film.  
  - `est_classique()` : retourne `True` si l’année < 2000.  
  - `from_json(str)` : crée un objet Film depuis une chaîne JSON.  
- Options dataclass : `frozen=True`, `slots=True`.  

## Extensions suggérées
- Comparer les films par note (ordre croissant).  
- Créer et sérialiser une liste de films favoris en JSON.  
- Implémenter des tests unitaires couvrant tous les cas limites (valeurs nulles, types invalides, etc.).  

## Organisation des fichiers
- `film.py` → contient la classe `Film` et ses méthodes.  
- `test_film.py` → contient les tests unitaires (pytest ou unittest).  


## Sortie attendue (JSON)
```
{"titre": "Matrix", "realisateur": "Wachowski", "annee": 1999, "note": 8.7}
{"titre": "Le Seigneur des Anneaux", "realisateur": "Peter Jackson", "annee": 2001, "note": 8.8}
{"titre": "Inception", "realisateur": "Christopher Nolan", "annee": 2010, "note": 9.0}

```

##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="1363" height="105" alt="image" src="https://github.com/user-attachments/assets/16799055-ffa3-4ec8-9236-0c437d609082" />


<img width="212" height="100" alt="image" src="https://github.com/user-attachments/assets/f7560f0c-4755-41e0-9129-f0f178e8956d" />
