# **Application de QCM en Python**

## **Introduction**

L'application de QCM en Python est une solution interactive et conviviale pour permettre aux utilisateurs de tester leurs connaissances sur différents sujets. Elle offre une gestion efficace des utilisateurs, 
un suivi des performances, et des fonctionnalités avancées comme un chronomètre et l'exportation des résultats.

## **Fonctionnalités**

### 1. **Gestion des utilisateurs**

- Création de profils utilisateur avec enregistrement des scores et historiques.
- Affichage de l'historique complet des QCM pour chaque utilisateur, incluant les scores et les dates des tests.

### 2. **Gestion des questions**

- Chargement des questions à partir d'un fichier JSON structuré.
- Organisation des questions par catégories, avec possibilité de choisir une catégorie avant de commencer le test.

### 3. **Évaluation et feedback**

- Vérification des réponses utilisateur et calcul du score final.
- Feedback immédiat pour chaque question, avec indication de la bonne réponse en cas d'erreur.

### 4. **Fonctionnalités avancées**

- Chronomètre limitant le temps de réponse à 10 secondes par question.
- Exportation des résultats dans un fichier CSV pour consultation ultérieure.

## **Structure des fichiers**

### 1. **qcm.py**

Le fichier principal contenant le code source de l'application.

### 2. **questions.json**

Un fichier JSON structuré contenant les questions et réponses, organisées par catégories.

### 3. **utilisateurs.json**

Un fichier JSON pour stocker les informations des utilisateurs, leurs historiques de scores et les dates des tests.

### 4. **Fichiers CSV générés**

Pour chaque utilisateur, un fichier CSV est créé afin d'enregistrer les résultats des QCM, avec les colonnes suivantes :

- **Utilisateur** : Nom de l'utilisateur.
- **Score** : Score obtenu.
- **Date** : Date du test.

## **Prérequis**

- **Python** : Version 3.6 ou supérieure.
- **Bibliothèques intégrées** :
  - `json`
  - `csv`
  - `os`
  - `datetime`

## **Installation**

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/Yasminebouzegzi/final-work-python
   ```
2. Assurez-vous que les fichiers suivants sont présents dans le répertoire :
   - `qcm.py`
   - `questions.json`

## **Utilisation**

1. Lancez le programme avec Python :
   ```bash
   python qcm.py
   ```
2. Suivez les instructions affichées dans la console :
   Utilisation:
   
Étape 1 : Entrez votre nom d'utilisateur
Lors du lancement de l'application, saisissez votre nom d'utilisateur lorsqu'il vous est demandé.
Si vous êtes un nouvel utilisateur, un profil sera créé pour vous dans le fichier utilisateurs.json.
Si vous êtes un utilisateur existant, votre historique de scores et les dates de vos précédents tests seront chargés et affichés.

Étape 2 : Choisissez une catégorie
Une liste de catégories disponibles sera affichée. Sélectionnez une catégorie en entrant le numéro correspondant.
Chaque catégorie contient des questions spécifiques, adaptées au thème choisi.

Étape 3 : Répondez aux questions dans le temps imparti
Une série de questions à choix multiples (QCM) sera affichée.
Chaque question propose plusieurs choix (par exemple : 1, 2, 3, etc.).
Vous devez entrer le numéro correspondant à votre réponse.
Un chronomètre de 10 secondes limite le temps de réponse pour chaque question. Si vous ne répondez pas dans ce délai, la réponse sera considérée comme incorrecte.

Étape 4 : Consultez votre score final et votre historique
Une fois le test terminé, l'application affiche :
Votre score final (par exemple, 8/10).
Les réponses correctes et incorrectes pour chaque question.
Une mise à jour de votre historique dans le fichier utilisateurs.json, incluant la date et le score du test.

## **Exemple d'exécution**

```
Cas nouvel utilisateur :
Entrez votre nom d&#39;utilisateur : sarah
------------------------------------------------------------------
| Bienvenue, sarah! Un nouveau profil a été créé.|
------------------------------------------------------------------
Catégories disponibles :
1. Python
2. Algorithme
3. Reseau
Choisissez une catégorie : 3
Vous avez choisi la catégorie : Reseau. Bonne chance !
------------------------------------------------------------------------------------------------------------------------------
| ATTENTION : CHAQUE QUESTION DOIT ETRE REPONDUE EN MOINS DE 10 SECONDES, SINON LA
REPONSE NE SERA PAS PRISE EN COMPTE |
--------------------------------------------------------------------------------------------------------------------------------

Quel dispositif est utilise pour connecter plusieurs appareils sur un reseau local ?
1. Un Switch
2. Un pare-feu
3. Un Modem
Votre réponse : 1
Bonne réponse !
Quel protocole est utilise pour envoyer des courriels ?
1. HTTP
2. SMTP
3. FTP
Votre réponse : 1
Réponse incorrecte ! La bonne réponse était : SMTP
-------------------------------------------------------
| En plus vous avez dépassé 10 secondes|
------------------------------------------------------

Quiz terminé !

voulez_vous consulter votre score (o/n) ?! :o

[&#39;Utilisateur&#39;, &#39;Score&#39;, &#39;Date&#39;]
[&#39;sarah&#39;, &#39;1&#39;, &#39;2025-01-22 20:51:58&#39;]


Cas un utilisateur ayant déjà joué :

Entrez votre nom d'utilisateur : sarah
---------------------------------------------------------------
Bienvenue de retour, sarah! Voici votre historique :
- [La Date: 2025-01-22 20:52:01, Votre Score: 1
Catégories disponibles :
1. Python
2. Algorithme
3. Reseau
Choisissez une catégorie : 3
Vous avez choisi la catégorie : Reseau. Bonne chance !
-----------------------------------------------------------------------------------------------------------------------------
| ATTENTION : CHAQUE QUESTION DOIT ETRE REPONDUE EN MOINS DE 10 SECONDES, SINON LA
REPONSE NE SERA PAS PRISE EN COMPTE |
-------------------------------------------------------------------------------------------------------------------------------

Quel dispositif est utilise pour connecter plusieurs appareils sur un reseau local ?
1. Un Switch
2. Un pare-feu
3. Un Modem
Votre réponse : 1
Bonne réponse !
Quel protocole est utilise pour envoyer des courriels ?
1. HTTP
2. SMTP

3. FTP
Votre réponse : 1
Réponse incorrecte ! La bonne réponse était : SMTP
Quiz terminé !

voulez_vous consulter votre score (o/n) ?! :o

[&#39;Utilisateur&#39;, &#39;Score&#39;, &#39;Date&#39;]
[&#39;sarah&#39;, &#39;1&#39;, &#39;2025-01-22 20:51:58&#39;]
[&#39;sarah&#39;, &#39;1&#39;, &#39;2025-01-22 20:55:15&#39;]
```

## **Auteurs**

Ce projet a été développé par l'équipe **ENG-3 Cybersécurité**, sous la supervision de **M. Mouhoun Said**.


