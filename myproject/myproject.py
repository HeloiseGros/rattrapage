# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

# Liste des questions
questions = {
    "Git": "Qu'est-ce qu'un commit ?",
    "Python": "Qu'est-ce que PEP 8 ?",
    "Linux": "Comment lister les fichiers d'un répertoire en ligne de commande ?"
}

# Dictionnaire des réponses attendues pour chaque question
reponses = {
    "Qu'est-ce qu'un commit ?": ["un enregistrement de modifications dans le dépôt Git", "une version d'un projet"],
    "Qu'est-ce que PEP 8 ?": ["un guide de style pour le code Python", "un package Python"],
    "Comment lister les fichiers d'un répertoire en ligne de commande ?": ["ls", "dir"]
}

# Page d'accueil
@app.route('/')
def index():
    # Sélectionne une question aléatoire
    question = random.choice(list(questions.values()))
    # Affiche la page HTML avec la question
    return render_template('index.html', question=question)

# Évaluation de la réponse
@app.route('/evaluate', methods=['POST'])
def evaluate():
    # Récupère la réponse de l'utilisateur
    user_answer = request.form['answer']
    # Récupère la question correspondante à la réponse
    question = request.form['question']
    # Récupère la réponse attendue
    expected_answers = reponses.get(question, [])
    # Vérifie si la réponse est valide
    if user_answer.lower() in [answer.lower() for answer in expected_answers]:
        result = 'Réponse correcte !'
    else:
        result = 'Réponse incorrecte. Veuillez réessayer.'
    # Affiche la page HTML avec le résultat
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
