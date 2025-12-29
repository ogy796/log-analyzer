import random

aktionen = [
    "[INFO] Nutzer besucht Startseite",
    "[INFO] Bild geladen",
    "[INFO] Logout erfolgreich"
]

warnungen = [
    "[WARNING] Speicherplatz fast voll (90%)",
    "[WARNING] Antwortzeit ungewöhnlich hoch (2s)",
    "[WARNING] Veraltete API genutzt"
]

fehler = [
    "[ERROR] Datenbank Timeout",
    "[ERROR] Zahlung abgelehnt",
    "[ERROR] Server abgestürzt",
]

print("Erstelle bunte Logs...")

with open("server.log", "w", encoding="utf-8") as f:
    for i in range(100):
        zufall = random.random()

        if zufall < 0.10:
            f.write(random.choice(fehler) + "\n")
        elif zufall < 0.30:
            f.write(random.choice(warnungen) + "\n")
        else:
            f.write(random.choice(aktionen) + "\n")

print("Fertig!")