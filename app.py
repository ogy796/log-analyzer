import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = Flask(__name__)

@app.route('/')
def dashboard():
    dateiname = os.getenv('LOG_DATEI', 'server.log')
    log_pfad = os.path.join(basedir, dateiname)

    suchbegriff = request.args.get('suche', '').lower()
    filter_typ = request.args.get('typ', 'alle')

    if not os.path.exists(log_pfad):
        return f"<h3>Fehler:</h3> <p>Die Datei <b>{dateiname}</b> wurde nicht gefunden.</p>"
    
    log_daten = []
    stats = {'danger': 0, 'warning': 0, 'total': 0}

    try:
        with open(log_pfad, 'r', encoding = 'utf-8') as f:
            for zeile in f:
                zeile = zeile.strip()
                if not zeile: continue

                eintrag = None
                if "ERROR" in zeile:
                    eintrag = {'inhalt': zeile, 'farbe': 'danger', 'typ': 'danger'}
                    stats ['danger'] += 1
                elif "WARNING" in zeile:
                    eintrag = {'inhalt': zeile, 'farbe': 'warning', 'typ': 'warning'}

                if eintrag:
                    match_suche = suchbegriff in zeile.lower()
                    match_typ = (filter_typ == 'alle' or filter_typ == eintrag ['typ'])

                    if match_suche and match_typ:
                        log_daten.append(eintrag)

            stats['total'] = len(log_daten)

            return render_template('index.html',
                                   datei = dateiname,
                                   stats=stats,
                                   logs=log_daten,
                                   suche=suchbegriff,
                                   aktueller_filter=filter_typ)
                                
    except Exception as e:
        return f"Systemfehler beim Lesen der Datei: {e}"

if __name__ == '__main__':
    app.run(port=5001, debug=True)