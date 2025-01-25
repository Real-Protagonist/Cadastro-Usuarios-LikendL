from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def get_all_users(self):
        usuarios = []
        current = self.head
        while current:
            usuarios.append(current.data)
            current = current.next
        return usuarios
    
    def email_verify(self, email):
        current = self.head
        while current:
            if current.data['email'] == email:
                return True
            current = current.next
        return False
    
list_usuarios = LinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        
        if list_usuarios.email_verify(email):
            return render_template('index.html', message="Email já cadastrado!", lista_usuarios=list_usuarios.get_all_users())
        
        list_usuarios.append({'name': name, 'email': email})

        return render_template('index.html', message="Usuario cadastrado com sucesso!", lista_usuarios=list_usuarios.get_all_users())
    
if __name__ == "__main__":
    app.run(debug=True)