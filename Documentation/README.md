# <div style="text-align:center;">Winvy</div>

## <div style="text-align:center;">Sadržaj</div>
<div style="display: flex; align-items:center; gap: 10px;">
    <img src="static/Logo.PNG" width="50px" height="75px">
    <p>Navedeni README dokument se sastoji od detaljnog opisa Winvy web servisa čiji je kreator: Alex Mihatović, student redovnog smjera informatike na fakultetu za informatiku u Puli, a web servis je kreiran za kolegij Informacijski sustav.</p>
</div>

## <div style="text-align:center;">Važna napomena</div>
Web servis se emitira na lokalnoj mreži pomoću porta 8080

Navedeno je sadržaj konstrukcije navedenog README filea

* <a href="#opis">Opis projekta</a>
* <a href="#funkcionalnosti">Funkcionalnosti</a>
* <a href="#sustav">Sustav</a>
* <a href="#svrha">Svrha</a>

---

## <div style="text-align:center;">Opis projekta</div>
<div id="opis">
    <p>Web servis za upravljanje, praćenje i analizu artikala u web shopu, koji uključuje CRUD operacije te analizu artikala na temelju cijene, količine i kategorije.
    Entitet koji se nalazi unutar baze podataka jest Artikl i sastoji se od atributa: id, naziv, cijena, količina, kategorija.
    Relacijska shema je konstruirana na temelju pravila konstrukcije tablica i naziva pojedinih stupaca unutar samih tablica:</p>

    Artikl(id, naziv, cijena, količina, kategorija)
</div>

---

## <div style="text-align:center;">Funkcionalnosti</div>
<div id="funkcionalnost">
    <p>Winvy se sastoji od više CRUD funkcionalnosti koje su sastavljene kako bi se pravilno i logički upravljalo inventarom web shopa.</p>
</div>

### Funkcionalnosti su slijedeće:  

* Dodavanje
* Uklananje
* Uređivanje
* Analiziranje
* Pregledavanje

### <div style="text-align:center;">Dodavanje</div>
<div>
    <p>Funkcionalnost za dodavanje kreirana kao ruta unutar backend dijela, naziva se "/dodaj_artikle" te se koriste GET i POST metode kako bi se dohvatili podatci unutar baze podatka i kako bi se dodali novi artikli, za svaki artikl se unosi naziv, cijena, kolicina i kategorija.</p>
</div>

### <div style="text-align:center;">Uklanjanje</div>
<div>
    <p>Funkcionalnost za uklanjanje kreirana je kao ruta unutar backend dijela, naziva se "/ukloni_artikle" te se koriste ponovno GET i POST  metode kako bi se dohvatili podatci a potom kako bi se objavile promjene dok unutar samog programskog dijela se koristi delete kako bi se maknuo određeni artikl za koji odredimo naziv.</p>
</div>

### <div style="text-align:center;">Uređivanje</div>
<div>
    <p>Funkcionalnost za uređivanje kreirana je kao ruta unutar backend dijela, naziva se "/uredi_artikle" te se koriste GET i Post metode kojima se novo unešeni podatci za artikl koji uređujemo, a koji smo odabrali na temelju naziva preslikavaju na stare podatke i tako uređujemo artikle.</p>
</div>

### <div style="text-align:center;">Analiziranje</div>
<div>
    <p>Funkcionalnost za analiziranje je kreirana unutar backend dijela, naziva se "/analiziraj_artikle" i koristi se metoda GET i ona pomoću chart.js analizira podatke o artiklima i iznosi grafički prikaz navedenih podataka koji olakšavaju preglednost pojedinih trendova i omogučavaju korištenje navedenog web servisa unutar više oblika.</p>
</div>

### <div style="text-align:center;">Pregledavanje</div>
<div>
    <p>Funkcionalnost za pregledavanje je kreirana unutar backenda, naziva se "/pregledaj_artikle" gdje se koristi metoda GET koja omogućava dohvaćanje podataka i ti dohvaćeni podatci se onda formiraju u obliku liste i tako se prikazuju korisniku, važno za napomenuti jest kako se navedeni pregled artikala izvršava odmah na početnoj stranici na kojoj se početno nalazimo kada pokrenemo web servis ili kada izvršimo neku CRUD operaciju, CRUD operacije se odabiru u navbaru na vrhu stranica. Navbar je formiran unutar jinja formata</p>
</div>

---

## <div style="text-align:center;">Sustav</div>
<div id="sustav">
    Sustav za Winvy web servis konstruiran je pomoću python flaska, ponyorma te je use case dijagram konstruiran pomoću Lucidchart online web aplikacije link:
    <a href="https://lucid.app/lucidchart/35df017e-a29f-4050-b4d2-7dd062cf979b/edit?viewport_loc=-899%2C-624%2C1663%2C800%2C0_0&invitationId=inv_30358928-d56a-46a1-8e07-02f64bc06152">Winvy - Lucidchart </a>
    <img src="Winvy.png" width="310px" height="325px">
</div>

---

## <div style="text-align:center;">Svrha</div>
<div id="svrha">
    Svrha Winvy web servisa jest da pruži uvid u inventar pojedinog webshopa te omogućava kao što je unutar stavke <a href="#opis">opis sustava</a> navedeno.
</div>