# Server Log Analyzer

Einfaches, webbasiertes Dashboard zur Analyse von Server-Logs.
Dieses Tool hilft dabei, wichtige Fehlermeldungen und Warnungen, auf Anhieb zu finden, anstatt sich durch tausende Zeilen Text wühlen zu müssen.

## Funktionen
- **Automatisches Filtern:** Trennt wichtige Fehler (ERROR) und Warnungen (WARNING) von normalen Informationen.
- **Ampelsystem:** Visuelle Markierung (Rot/Gelb) für eine schnelle Priorisierung.
- **Suchfunktion:** Gezielte Suche nach Fehlern (z.B "Timeout")
- **Sicherheit:** Konfiguration über Umgebungsvariablen (`.env`).

## Installation & Start
1. Repository klonen oder herunterladen.
2. Voraussetzungen installieren:
   ```bash
   pip install -r requirements.txt