# RW/WW CSV Summary

## English

This project processes `RW_WW_ohne_leere_Werte.csv` with pandas. It reads the large CSV in chunks, groups the rows by `Name`, and calculates the sums of `RW`, `WW`, and `RW_WW` for each group. Each name is written to its own one-row summary CSV in the `summaries/` folder.

### Requirements

- Python 3.11 or newer
- pandas (installed from `requirements.txt`)
- The input CSV in the same folder as `process_csv.py`

The input CSV must contain the columns `Name`, `RW`, `WW`, and `RW_WW`.

### Run on Windows (PowerShell)

From this project folder, create and activate a virtual environment, install the dependency, and run the script:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\process_csv.py
```

The script processes 100,000 rows at a time. It creates or replaces files such as `summaries/Rur-Scholle_summary.csv`. Output files use UTF-8 encoding with a BOM so Excel can display names with accented characters correctly.

### Large input file and GitHub

The source CSV is about 92 MiB and is excluded from Git by `.gitignore`. GitHub warns about files larger than 50 MiB and blocks regular Git files larger than 100 MiB. Only upload the dataset if you are allowed to share it. For a reproducible repository without the dataset, provide the CSV separately and place it beside `process_csv.py`; for versioning the dataset, use Git LFS.

## Deutsch

Dieses Projekt verarbeitet `RW_WW_ohne_leere_Werte.csv` mit pandas. Die große CSV-Datei wird blockweise eingelesen. Die Zeilen werden nach `Name` gruppiert und die Summen der Spalten `RW`, `WW` und `RW_WW` berechnet. Für jeden Namen wird eine einzeilige Zusammenfassungs-CSV im Ordner `summaries/` gespeichert.

### Voraussetzungen

- Python 3.11 oder neuer
- pandas (Installation über `requirements.txt`)
- Die Eingabe-CSV im selben Ordner wie `process_csv.py`

Die Eingabe-CSV muss die Spalten `Name`, `RW`, `WW` und `RW_WW` enthalten.

### Ausführung unter Windows (PowerShell)

Im Projektordner eine virtuelle Umgebung erstellen und aktivieren, die Abhängigkeit installieren und das Skript starten:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\process_csv.py
```

Das Skript verarbeitet jeweils 100.000 Zeilen. Es erstellt oder ersetzt Dateien wie `summaries/Rur-Scholle_summary.csv`. Die Ausgabedateien verwenden UTF-8 mit BOM, damit Excel Umlaute korrekt anzeigen kann.

### Große Eingabedatei und GitHub

Die Quelldatei ist etwa 92 MiB groß und wird durch `.gitignore` von Git ausgeschlossen. GitHub warnt bei Dateien über 50 MiB und blockiert reguläre Git-Dateien über 100 MiB. Lade den Datensatz nur hoch, wenn du ihn teilen darfst. Für ein reproduzierbares Repository ohne Datensatz muss die CSV separat bereitgestellt und neben `process_csv.py` abgelegt werden. Für die Versionierung des Datensatzes sollte Git LFS verwendet werden.