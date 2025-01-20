import json
import csv
import os
from datetime import datetime # pour date et heure

# Gestion des Utilisateurs
utilis_fichier = "utilisateurs.json"
question_fichier = "questions.json"

#recuperer les users de json  et retourner ces donnes 
def recup_utilisateur():
    if os.path.exists(utilis_fichier):  #Verifie si le fichier utilisateurs.json existe
        with open(utilis_fichier, "r") as file:
            return json.load(file)  # convertir des fichiers JSON en objets Python recuperer les donner de json en python
    return {}

#écrire les données dans le fichier utilisateurs.json
def sauvegarde_utilisateur(utilisateur):
    with open(utilis_fichier, "w") as file: #Si le fichier utilisateurs.json n'existe pas encore, Python le cree automatiquement en mode ecriture ("w") sinon l'ouvrire seulement en mode ecriture
        json.dump(utilisateur, file) # convertir un utilisateur de Python en JSON et l'écrire directement dans fichier utilisateurs.json.



def recup_creer_user():
    utilisateur = recup_utilisateur()
    username = input("Entrez votre nom d'utilisateur : ")

    if username in utilisateur: #si usernaame existe dans fichier utilisateurs.json in affiche son historique(date+score)
        print(f"Bienvenue de retour, {username}! Voici votre historique :")
        for his in utilisateur[username]["history"]:
            print(f"- [La Date: {his['date']}, Votre Score: {his['score']}")
    else:  
        print(f"Bienvenue, {username}! Un nouveau profil a été créé.")
        utilisateur[username] = {"history": []}
        sauvegarde_utilisateur(utilisateur)

    return username, utilisateur

###############################
# Gestion des Questions

def recup_questions():
    if os.path.exists(question_fichier):
        with open(question_fichier, "r") as file:
            return json.load(file)
    else:
      print("Le fichier de questions est introuvable !")


def selection_categorie(questions):
    print("Catégories disponibles :")
    categories = list(questions.keys())
    
    # Afficher les catégories avec un numéro
    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")
    
    # Demander à l'utilisateur de choisir une catégorie
    while True:
        try:
            choice = int(input("Choisissez une catégorie : ")) - 1
            if 0 <= choice < len(categories):
                return categories[choice]
            else:
                print("Choix invalide. Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

#######################################3



def main():
    print("Bienvenue au QCM Informatique !")
    username, users = recup_creer_user()

    try:
        questions_data = recup_questions()
        category = selection_categorie(questions_data)
        questions = questions_data[category]
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()