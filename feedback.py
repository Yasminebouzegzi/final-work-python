# Fonction principale du quiz
def jouer_quiz(questions, categorie):
    score = 0
    print(f"Vous avez choisi la catégorie : {categorie}. Bonne chance !\n")

    for question in questions[categorie]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")
        
        while True:
            try:
                # Demande de réponse utilisateur
                reponses = int(input("Votre réponse : ")) - 1
                if 0 <= reponses < len(question["options"]):
                    # Vérification de la réponse
                    if question["options"][reponses] == question["repense"]:
                        print("Bonne réponse !\n")
                        score += 1
                    else:
                        print(f"Réponse incorrecte ! La bonne réponse était : {question['repense']}\n")
                    break  # Passe à la question suivante
                else:
                    print("Choix invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")
    
    # Affichage du score final
    print(f"Quiz terminé ! Votre score final est de {score}/{len(questions[categorie])}.\n")
    return score


# Mise à jour de l'historique de l'utilisateur
def mise_a_jour_historique(utilisateur, username, score):
    utilisateur[username]["history"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "score": score
    })
    sauvegarde_utilisateur(utilisateur)
