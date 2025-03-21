from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/', methods=['POST'])
def decrypt():
    data = request.get_json()
    if not data or 'encrypted_text' not in data:
        return jsonify({'error': 'Donnée manquante'}), 400
    
    decrypted_text = decrypt_value(data['encrypted_text'])
    return jsonify({'decrypted_text': decrypted_text})
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
