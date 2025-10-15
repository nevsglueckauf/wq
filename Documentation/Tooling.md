# SBA
## Tooling

### Knime (First look, EDA & Data Partitioning)

### Python 3.13 (Numpy, Pandas, PX, Dash)

Die Verwendung von Python umfasst die folgenden Aufgabenbreiche:

- First-Look
- EDA 
- Grafische Datenanalyse
- Dashboard(s)
- Admin-Tool (Import neuer Daten)
- Export der Daten (mit Filter-, Sortierkriterien) nach:
    - SQL
    - CSV
    - XML
    


### SQL 

- RDBMS: Postgres,  SQLite und generisches SQL

Aus den "Rohdaten" wird (via Python) eine Extraktion der Daten vorgenommen und diese in ein normalisiertes relationales Datenmodell überführt.

Die Daten werden in eine lokale PostreSQL- und Sqlite- Instanz übernommen und als generisches SQL- (DDL, DML) Schema
ablegt, sodass eine Übernahme in andere RDBMS möglich ist.

Somit wird eine schnelle Auswertung (Views, Aggregationen, Export) der Daten zu jedem Zeitpunkt ermöglicht.

