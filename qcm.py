import json
import csv
import os
from datetime import datetime # pour date et heure
# Gestion des Utilisateurs
utilis_fichier = "utilisateurs.json"
question_fichier ="questions.json"
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
        print("-------------------------------------------------")
        print(f"Bienvenue de retour, {username}! Voici votre historique :")
        for his in utilisateur[username]["history"]:
            print(f"- [La Date: {his['date']}, Votre Score: {his['score']}")
    else:  
        print("--------------------------------------------------")
        print(f"| Bienvenue, {username}! Un nouveau profil a été créé.|")
        print("-------------------------------------------------")
      
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


#fonction qui sert a convertir le temps en secondes pour le chronometre
def convertir_time_en_seconde(time):
    heure = time.hour
    minute = time.minute
    seconde = time.second
    return heure * 3600 + minute * 60 + seconde
#afficher le score depuis le fichier csv de l'utilisateur
def afficher_score(username):
    with open(f"{username}.csv","r") as fichier:
        lire_fichier_csv = csv.reader(fichier)
        for i in lire_fichier_csv:
            print(i)

import os
import csv

def remplir_csv(username, Score, Date):
    fichier_utilisateur = f"{username}.csv"

    with open(fichier_utilisateur, 'a', newline='') as fichier:
        head = ['Utilisateur', 'Score', 'Date']
        writer = csv.DictWriter(fichier, fieldnames=head)

        # Vérifier si le fichier est vide pour ajouter le head (utilisateur,score,date)
        if os.stat(fichier_utilisateur).st_size == 0:
            writer.writeheader()

        # ajouter les infos que ca soit vide ou non
        writer.writerow({'Utilisateur': username, 'Score': Score, 'Date': Date})



def jouer_quiz(questions, categorie):
    score = 0
    print(f"Vous avez choisi la catégorie : {categorie}. Bonne chance !")
    print(" ---------------------------------------------------------------------------------------------------------------------")
    print("| ATTENTION : CHAQUE QUESTION DOIT ETRE REPONDUE EN MOINS DE 10 SECONDES, SINON LA REPONSE NE SERA PAS PRISE EN COMPTE |")
    print(" ----------------------------------------------------------------------------------------------------------------------\n")
    
    # Enregistre l'heure de début
    
    
    for question in questions[categorie]:
      
    
            print(question["question"])
            time_debut = datetime.now()
            TD = convertir_time_en_seconde(time_debut)
            for i, option in enumerate(question["options"]):
                print(f"{i + 1}. {option}")
                
            
            while True:
                try:
                    # Demande de réponse utilisateur
                    reponses = int(input("Votre réponse : ")) - 1
                    
                    if 0 <= reponses < len(question["options"]):
                        
                        if question["options"][reponses] == question["repense"]:
                            print("Bonne réponse !")
                            if (convertir_time_en_seconde(datetime.now()) > TD + 10):
                             print('---------------------------------------------------------------')
                             print("| Mais vous avez dépassé 10 sec votre réponse n'est pas compté |")
                             print("---------------------------------------------------------------\n")
                             break
                            else:
                                score += 1
                            break
                        else:
                            print(f"Réponse incorrecte ! La bonne réponse était : {question['repense']}")
                            if (convertir_time_en_seconde(datetime.now()) > TD + 10):
                              print('---------------------------------------')
                              print("| En plus vous avez dépassé 10 secondes|")
                              print("---------------------------------------")
                              break
                        break
                 
                             
                    else:
                        print("Choix invalide. Veuillez entrer un numéro valide.")
                except ValueError:
                   print("Veuillez entrer un numéro valide.")              
       

    print("Quiz terminé !\n")
    
    
    return score
# Mise à jour de l'historique de l'utilisateur

def mise_a_jour_historique(utilisateur, username, score):
    utilisateur[username]["history"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score
        
    })
    
    sauvegarde_utilisateur(utilisateur)

#### le main
def main():
    username, utilisateur = recup_creer_user()
    
    questions = recup_questions()

    if not questions:
        print("Aucune question disponible. Terminaison du programme.")
        return

    categorie = selection_categorie(questions)
    score= jouer_quiz(questions, categorie)
    remplir_csv(username,score,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    consulation = input("voulez_vous consulter votre score (o/n) ?! :")
    if consulation == "o":
         print()
         afficher_score(username)
    mise_a_jour_historique(utilisateur, username, score)
ArithmeticError

if __name__ == "__main__":
   main()





