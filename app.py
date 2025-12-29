import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = Flask(__name__)

@app.route('/')
def dashboard():
    dateiname = os.getenv('LOG_DATEI')
    log_pfad = os.path.join(basedir, dateiname)

    suchbegriff = request.args.get('suche')

    if not os.path.exists(log_pfad):
        return f"Fehler: Datei {dateiname} nicht gefunden."
    
    log_daten = []

    try:
        with open(log_pfad, 'r', encoding='utf-8') as f:
            for zeile in f:
                zeile = zeile.strip()

                eintrag = None

                if "ERROR" in zeile:
                    eintrag = {'inhalt': zeile, 'farbe': 'danger'}
                elif "WARNING" in zeile:
                    eintrag = { 'inhalt': zeile, 'farbe': 'warning' }

                if eintrag:
                    if suchbegriff:
                        if suchbegriff.lower() in zeile.lower():
                            log_daten.append(eintrag)
                    else:
                        log_daten.append(eintrag)

        return render_template('index.html',
                               datei=dateiname,
                               anzahl=len(log_daten),
                               logs=log_daten,
                               suche=suchbegriff)
    except Exception as e:
        return f"Systemfehler: {e}"
    
    if __name__ == '__main__':
        app.run(port=5001, debug=True)
                               


    if not os.path.exists(log_pfad):
        return f"<h3>Fehler:</h3> <p> Die Datei <b>{dateiname}</b> wurde nicht gefunden.</p>"
    
    log_daten = []

    try:
        with open(log_pfad, 'r', encoding='utf-8') as f:
            for zeile in f:
                zeile = zeile.strip()

                if "ERROR" in zeile:
                    eintrag = { 'inhalt': zeile, 'farbe': 'danger' }
                    log_daten.append(eintrag)

                elif "WARNING" in zeile:
                    eintrag = { 'inhalt': zeile, 'farbe': 'warning' }
                    log_daten.append(eintrag)

                else:

                    pass
            return render_template('index.html',
                                   datei=dateiname,
                                   anzahl=len(log_daten),
                                   logs=log_daten)
    except Exception as e:
        return f"Systemfehler: {e}"



    
if __name__ == '__main__':
    app.run(port=5001, debug=True)


#bank, if betrag >10.000 and land != "Deutschland"

