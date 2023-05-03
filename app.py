from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_answer', methods=['POST'])
def check_answer():
    # Récupérer la réponse de l'utilisateur à partir du formulaire
    user_answer = request.form['answer']
    
    # Comparer la réponse de l'utilisateur avec la réponse attendue
    if user_answer.lower() == 'réponse attendue':
        result = 'Correct !'
    else:
        result = 'Incorrect.'
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
