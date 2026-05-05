from flask import Flask, request, render_template, make_response, jsonify
from pony.orm import Database, Required, Set, db_session

app = Flask(__name__)

db = Database()

class Artikl(db.Entity):
    naziv = Required(str)
    cijena = Required(float)
    kolicina = Required(int)
    kategorija = Required(str)

db.bind(provider='sqlite', filename='Artikli.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodaj_artikle', methods=['POST'])
def dodaj():
    return render_template('index.html')

@app.route('/ukloni_artikle', methods=['DELETE'])
def ukloni():
    return render_template('index.html')

@app.route('/uredi_artikle', methods=['PUT'])
def uredi():
    return render_template('index.html')

@app.route('/analiziraj_artikle', methods=['GET'])
def analiziraj():
    return render_template('index.html')

@app.route('/pregled_artikle', methods=['GET'])
def pregled():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)