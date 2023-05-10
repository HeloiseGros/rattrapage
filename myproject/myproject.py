# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

# Liste des questions
questions = {
    "Git": "Qu'est-ce qu'un commit ?",
    "Git2": "Comment creer un repository git ?",
    "Git3": "Comment enregistre un fichier avec git ?",
    "Git4": "Comment sauvegarder notre travail avec git ?",
    "Git5": "Quelle est la commande pour copier un distant repository ?",
    "Git6": "Quelle est la commande pour envoyer un objet a un distant repository ?",
    "Git7": "Pourquoi utiliser git branche ?",
    "Git8": "Comment lister toute les branches du repository local ?",
    "Git9": "Comment creer une branche v1.2 et commencer a travailler dessus ?",
    "Python": "Qu'est-ce que PEP 8 ?",
    "Python1": "Quel est le package manager de Python ?",
    "Python2": "Quel est l'outil qui permet de creer un environnement virtuel avec Python ?",
    "Python3": "Quelle language utiliser si vous souhaitez que votre code tourne sous windows et linux ?",
    "Python4": "Quel est le package python qui permet de generer un nombre aleatoire ?",
    "Python5": "Quel est le package python qui permet de creer des web framework ?",
    "Linux": "Comment lister les fichiers d'un répertoire en ligne de commande ?",
    "Linux1": "What are the 3 Operating systems ?",
    "Linux2": "How do you change directory ?",
    "Linux3": "How do you print your working directory ?",
    "Linux4": "How do you list all files in a path including hidden files ?"
}

# Dictionnaire des réponses attendues pour chaque question
reponses = {
    "Qu'est-ce qu'un commit ?": ["un enregistrement de modifications dans le dépôt Git", "une version d'un projet"],
    "Qu'est-ce que PEP 8 ?": ["un guide de style pour le code Python", "un package Python"],
    "Comment lister les fichiers d'un répertoire en ligne de commande ?": ["ls", "dir"],
    "What are the 3 Operating systems ?": ["Windows, Linux et macOs"],
    "How do you change directory ?": ["cd"],
    "How do you print your working directory ?": ["pwd"],
    "How do you list all files in a path including hidden files ?": ["ls -a"],
    "Comment creer un repository git ?": ["git init"],
    "Comment enregistre un fichier avec git ?": ["git add"],
    "Comment sauvegarder notre travail avec git ?": ["git commit"],
    "Quelle est la commande pour copier un distant repository ?": ["git clone"],
    "Quelle est la commande pour envoyer un objet a un distant repository ?": ["git push"],
    "Pourquoi utiliser git branche ?": ["essayer de nouvelles idées","travailler de sur son ordinateur tout en enregistrant sur le serveur commun"],
    "Comment lister toute les branches du repository local ?": ["git branch"],
    "Comment creer une branche v1.2 et commencer a travailler dessus ?": ["git checkout -b v1.2"],
    "Quel est le package manager de Python ?": ["pip"],
    "Quel est l'outil qui permet de creer un environnement virtuel avec Python ?": ["virtualenv"],
    "Quelle language utiliser si vous souhaitez que votre code tourne sous windows et linux ?": ["Python"],
    "Quel est le package python qui permet de generer un nombre aleatoire ?": ["random"],
    "Quel est le package python qui permet de creer des web framework ?": ["Flask","Django"] 
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
