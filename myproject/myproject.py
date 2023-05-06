# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# liste de questions clés
questions = {
    "Git": "Qu'est-ce qu'un commit ?",
    "Python": "Qu'est-ce que PEP 8 ?",
    "Linux": "Comment lister les fichiers d'un répertoire en ligne de commande ?"
}

# dictionnaire de réponses attendues pour chaque question
reponses = {
    "Qu'est-ce qu'un commit ?": ["un enregistrement de modifications dans le dépôt Git", "une version d'un projet"],
    "Qu'est-ce que PEP 8 ?": ["un guide de style pour le code Python", "un package Python"],
    "Comment lister les fichiers d'un répertoire en ligne de commande ?": ["ls", "dir"]
}

# fonction pour vérifier si une réponse est similaire à une réponse attendue
def check_answer(reponse_utilisateur, reponse_attendue):
    # transformer les réponses en minuscules et enlever les espaces en début et fin
    reponse_utilisateur = reponse_utilisateur.lower().strip()
    reponse_attendue = [r.lower().strip() for r in reponse_attendue]
    
    # vérifier si la réponse de l'utilisateur est exactement la réponse attendue
    if reponse_utilisateur in reponse_attendue:
        return True
    
    # vérifier si la réponse de l'utilisateur est suffisamment similaire à la réponse attendue
    for r in reponse_attendue:
        if r.startswith(reponse_utilisateur) or reponse_utilisateur.startswith(r):
            return True
    
    # si aucune des conditions n'est remplie, retourner False
    return False

@app.route('/')
def home():
    # sélectionner une question aléatoire
    question = random.choice(list(questions.values()))
    
    # afficher la page HTML avec la question et le bouton "Random Question"
    return render_template('index.html', question=question)

@app.route('/', methods=['POST'])
def evaluate_answer():
    # récupérer la réponse de l'utilisateur et la question actuelle
    reponse_utilisateur = request.form['reponse']
    question = request.form['question']
    
    # récupérer la réponse attendue correspondante à la question
    reponse_attendue = reponses[question]
    
    # vérifier si la réponse de l'utilisateur est valide et afficher le résultat correspondant
    if check_answer(reponse_utilisateur, reponse_attendue):
        resultat = "Bonne réponse !"
    else:
        resultat = "Mauvaise réponse. Essayez encore."
    
    # afficher la page HTML avec le résultat
    return render_template('result.html', resultat=resultat)

if __name__ == '__main__':
    app.run()

