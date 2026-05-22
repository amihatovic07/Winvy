from flask import Flask, request, render_template, make_response, jsonify, redirect
from pony.orm import Database, Required, Set, db_session, PrimaryKey

app = Flask(__name__)

db = Database()

class Artikl(db.Entity):
    id = PrimaryKey(int, auto=True)
    naziv = Required(str)
    cijena = Required(float)
    kolicina = Required(int)
    kategorija = Required(str)

db.bind(provider='sqlite', filename='Artikli.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodaj_artikle', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'POST':
        data = request.form
        cijena = float(data['cijena'])
        kolicina = int(data['kolicina'])
        if cijena < 0 or kolicina < 0:
            return "Greška: cijena i količina ne mogu biti negativne.", 400
        with db_session:
            postojeci = Artikl.get(naziv=data['naziv'])
            if postojeci:
                return "Artikl već postoji!", 400
            Artikl(naziv=data['naziv'], cijena=float(data['cijena']), kolicina=int(data['kolicina']), kategorija=data['kategorija'])
        return redirect('/')
    return render_template('dodaj.html')

@app.route('/ukloni_artikle', methods=['GET'])
def ukloni_stranica():
    return render_template('ukloni.html')

@app.route('/ukloni_artikle/<naziv>', methods=['DELETE'])
def ukloni(naziv):
    with db_session:
        artikl = Artikl.get(naziv=naziv)
        if artikl:
            artikl.delete()
    return jsonify({"poruka": "Artikl uklonjen"}), 200

@app.route('/uredi_artikle', methods=['GET'])
def uredi_stranica():
    return render_template('uredi.html')


@app.route('/uredi_artikle/<naziv>', methods=['PUT'])
def uredi(naziv):
    data = request.get_json()
    with db_session:
        artikl = Artikl.get(naziv=naziv)
        if not artikl:
            return jsonify({"poruka": "Artikl nije pronađen"}), 404
        artikl.cijena = float(data['cijena'])
        artikl.kolicina = float(data['kolicina'])
        artikl.kategorija = float(data['kategorija'])
    return jsonify({"poruka": "Artikl uređen!"})

@app.route('/analiziraj_artikle', methods=['GET'])
def analiziraj():
    with db_session:
        artikli = list(Artikl.select())
        ukupna_kolicina = sum(a.kolicina for a in artikli)
        ukupna_vrijednost = round(sum(a.kolicina * a.cijena for a in artikli), 2)
        kategorije = set(a.kategorija for a in artikli)
        broj_kategorija = len(kategorije)
        nazivi = [a.naziv for a in artikli]
        cijene = [a.cijena for a in artikli]
        kolicine = [a. kolicina for a in artikli]
        kategorije_dict = {}
        for a in artikli:
            kategorije_dict[a.kategorija] = kategorije_dict.get(a.kategorija, 0) + 1
        kategorije_nazivi = list(kategorije_dict.keys())
        kategorije_brojevi = list(kategorije_dict.values())
    return render_template('analiza.html', ukupna_kolicina=ukupna_kolicina, ukupna_vrijednost=ukupna_vrijednost, broj_kategorija=broj_kategorija, nazivi=nazivi, cijene=cijene, kolicine=kolicine, kategorije_nazivi=kategorije_nazivi, kategorije_brojevi=kategorije_brojevi)

@app.route('/pregledaj_artikle', methods=['GET'])
def pregled():
    with db_session:
        artikli = list(Artikl.select())[:]
        lista = [{"naziv": a.naziv, "cijena": a.cijena, "kolicina": a.kolicina, "kategorija": a.kategorija} for a in artikli]
    return render_template("pregled.html", artikli=lista)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)