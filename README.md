# Server Log Analyzer

Einfaches, webbasiertes Dashboard zur Analyse von Server-Logs. Dieses Tool hilft dabei, wichtige Fehlermeldungen und Warnungen auf Anhieb zu finden, anstatt sich durch tausende Zeilen Text wühlen zu müssen.

## Funktionen

* **Dashboard-Statistik:** Sofortiger Überblick über die Gesamtanzahl von Fehlern und Warnungen.
* **Quick-Filter:** Per Klick nur Fehler, Warnungen oder alle Einträge anzeigen.
* **Automatisches Filtern:** Erkennt und markiert `ERROR` und `WARNING` automatisch.
* **Suchfunktion:** Gezielte Suche nach Fehlercodes oder Begriffen (z. B. "Timeout").
* **Sicherheit:** Konfiguration über Umgebungsvariablen (.env).

## Tech-Stack

* **Framework:** Flask
* **Sprache:** Python
* **Frontend:** HTML (Jinja2 Templates) & Bootstrap 5

## Installation & Start

1. **Repository klonen oder herunterladen.**

2. **Voraussetzungen installieren:**
python3 -m pip install flask python-decouple

3. **Test-Logs erstellen (Optional):**
python3 generate_logs.py

4. **Programm starten:**
python3 app.py 
(Öffne danach http://127.0.0.1:5001 im Browser)