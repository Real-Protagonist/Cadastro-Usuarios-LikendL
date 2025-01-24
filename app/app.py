from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        
        usuarios.append({'name': name, 'email': email})
        
        return render_template('index.html', message="Usuario cadastrado com sucesso!", lista_usuario=usuarios)
    
if __name__ == "__main__":
    app.run(debug=True)