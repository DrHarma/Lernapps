# Unterrichts-Apps

Startpaket für Chemie, Biologie, MoLab und Sonstige Apps.
Die Startseite ist responsiv, hat Suche und Filter und verwendet keine externen Bibliotheken.
Es sind bewusst noch keine Unterrichts-Apps enthalten.

## Einmalig veröffentlichen

1. ZIP vollständig entpacken. Den Inhalt des Ordners `unterrichts-apps` verwenden, nicht den übergeordneten Ordner.
2. Ein neues öffentliches GitHub-Repository `unterrichts-apps` erstellen. Keine vertraulichen Materialien hochladen.
3. Alle Dateien UND versteckten Ordner, insbesondere `.github`, in den Hauptordner des Repositorys übernehmen. `index.html` muss direkt im Hauptordner liegen. Standardbranch: `main`.
4. Unter Settings → Pages → Build and deployment → Source **GitHub Actions** auswählen. Anders als im ursprünglichen Praxis-Skript wird hier ein Workflow verwendet, damit die Übersicht automatisch entsteht.
5. Unter Actions den Workflow prüfen. Falls nötig „Run workflow“ ausführen. Die fertige Website-Adresse steht anschließend unter Settings → Pages.

Die Veröffentlichung ist erst nach erfolgreichem Workflow verfügbar. Kontoeinstellungen, Organisationsregeln oder deaktivierte Actions können eine Freigabe verlangen. Für den einfachen Weg ist ein öffentliches Repository vorgesehen.

## Dateien zuverlässig mit Git übertragen

Die Weboberfläche oder manche Dateiauswahldialoge übersehen versteckte Dateien. Daher kontrollieren, dass `.github/workflows/pages.yml` im Repository vorhanden ist.
Alternativ im entpackten Projektordner mit installiertem Git ausführen (PLATZHALTER ersetzen):

```sh
git init -b main
git add .
git commit -m "Unterrichts-App-Sammlung einrichten"
git remote add origin https://github.com/DEIN-BENUTZERNAME/unterrichts-apps.git
git push -u origin main
```

Diese Befehle setzen ein leeres Zielrepository voraus. Die GitHub-Anmeldung erfolgt über deine lokale Git-Umgebung; keine Zugangsdaten in Dateien eintragen.

## Neue App hinzufügen – ohne manuelle Startseitenpflege

Eine vollständige HTML-Datei im passenden Ordner hochladen, zum Beispiel:
`chemie/08/teilchenmodell.html`.
Nach dem Commit auf `main` erzeugt GitHub Actions die App-Liste neu und veröffentlicht die Website.
Die generierte `apps.js` wird im veröffentlichten Website-Artefakt aktualisiert, nicht als zusätzlicher Commit im Repository.

Titel und Kurzbeschreibung werden aus dem HTML übernommen:

```html
<title>Teilchenmodell – Übung</title>
<meta name="description" content="Teilchenanordnungen den Aggregatzuständen zuordnen.">
```

Ohne Titel wird der Dateiname verwendet; ohne Beschreibung erscheint ein allgemeiner Hinweis.
Alle `.html`- und `.htm`-Dateien unter den vier Fachordnern werden als Apps erfasst. Hilfsseiten deshalb nicht dort als eigene HTML-Dateien ablegen, wenn sie nicht in der Übersicht erscheinen sollen.
Jahrgänge Chemie: 07, 08, 09, 10, ep, q1, q2. Biologie: zusätzlich 05 und 06.
MoLab und Sonstige Apps werden jahrgangsübergreifend angezeigt.
Dateinamen möglichst klein, ohne Leerzeichen oder Umlaute. Relative Verweise auf Bilder und andere Dateien verwenden; benötigte Begleitdateien ebenfalls hochladen.

## Lokal verwenden

Die anfängliche `index.html` lässt sich direkt öffnen und zeigt die leeren Bereiche.
Nach dem Hinzufügen von Apps mit Python 3 die Liste aktualisieren:

```sh
python scripts/build_index.py
```

Unter Windows gegebenenfalls `py scripts/build_index.py` verwenden, unter macOS/Linux `python3 scripts/build_index.py`.
Danach `index.html` erneut öffnen. Für Apps mit fetch oder Modulen kann ein lokaler Webserver erforderlich sein: `python -m http.server 8000`, dann im Browser `http://localhost:8000` öffnen.

## Vor dem Unterricht

- Fachliche Inhalte, Aufgaben und Lösungen selbst prüfen.
- Tablet-, Tastaturbedienung und Links testen.
- Keine Namen, Noten, Kennwörter, API-Schlüssel oder unzulässig kopierten Inhalte veröffentlichen.
- Keine Anmeldung, kein Tracking und keine personenbezogenen Schülerdaten in Apps einbauen.
- Naturwissenschaftliche Sicherheitsanweisungen anhand der geltenden schulischen Vorgaben prüfen.
- Eine technische Ausweichlösung bereithalten.

Die Vorlage enthält kein Tracking. GitHub stellt das Hosting bereit; daraus folgt keine Zusicherung, dass beim Hosting keinerlei technische Zugriffsdaten verarbeitet werden.
Eine öffentliche Bereitstellung räumt Dritten nicht automatisch beliebige Nutzungsrechte ein. Eine Lizenz erst nach Prüfung eigener und fremder Rechte ergänzen.
