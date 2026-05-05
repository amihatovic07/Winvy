from flask import Flask, request, render_template, make_response, jsonify, redirect
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
    with db_session:
        artikli = list(Artikl.select())[:]
        lista = [{"naziv": a.naziv, "cijena": a.cijena, "kolicina": a.kolicina, "kategorija": a.kategorija} for a in artikli]
    return render_template("index.html", artikli=lista)

@app.route('/dodaj_artikle', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'POST':
        data = request.form
        with db_session:
            Artikl(naziv=data['naziv'], cijena=float(data['cijena']), kolicina=int(data['kolicina']), kategorija=data['kategorija'])
        return redirect('/')
    return render_template('dodaj.html')

@app.route('/ukloni_artikle', methods=['GET', 'POST'])
def ukloni():
    if request.method == 'POST':
        naziv = request.form['naziv']
        with db_session:
            artikl = Artikl.get(naziv=naziv)
            if artikl:
                artikl.delete()
        return redirect('/')
    return render_template('ukloni.html')

@app.route('/uredi_artikle', methods=['GET', 'POST'])
def uredi():
    if request.method == 'POST':
        naziv = request.form['naziv']
        with db_session:
            artikl = Artikl.get(naziv=naziv)
            if artikl:
                artikl.cijena = float(request.form['cijena'])
                artikl.kolicina = int(request.form['kolicina'])
                artikl.kategorija = request.form['kategorija']
            return redirect('/')
    return render_template('uredi.html')

@app.route('/analiziraj_artikle', methods=['GET'])
def analiziraj():
    return render_template('index.html')

@app.route('/pregledaj_artikle', methods=['GET'])
def pregled():
    with db_session:
        artikli = list(Artikl.select())[:]
        lista = [{"naziv": a.naziv, "cijena": a.cijena, "kolicina": a.kolicina, "kategorija": a.kategorija} for a in artikli]
    return make_response(jsonify(lista), 200)

if __name__ == '__main__':
    app.run(debug=True, port=8080)