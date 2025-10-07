# <img src="../Dashboards/python/assets/whisk_rox.png"> „Data on the rocks“

## Datenqualität

### Datenfluß

```mermaid
sequenceDiagram
    autonumber
    
    box orange Neue Dateien
    participant inp@{ "type" : "collections" }
    end
    box lightblue  Python &  File IO
    participant Pipeline@{ "type" : "control" }
    participant fs@{ "type" : "queue" }
    participant Datenbereinigung@{ "type" : "control" }
    end 

    box lightgray  Datenkonsumenten
    participant knime@{ "type" : "boundary" }
    participant pbi@{ "type" : "boundary" }
    participant dash@{ "type" : "boundary" }
    participant RDBMS@{ "type" : "database" }
    end 

    box lightgreen  Dashboards
    actor Web
    actor PowerBI
    end 

    inp-->>Pipeline: Dateityp checken
     alt CSV?
            Pipeline->>fs: Temp. Ablage
     else XLSX?
            Pipeline->>fs: Temp. Ablage
            Pipeline->>fs: Konvertierung nach CVS
    end
    Note right of Datenbereinigung: Checks durchführen
    Datenbereinigung->>fs: Datentypen korr. [Falsche Dezimaltrenner?]
    Datenbereinigung->>fs: Daten typen korr. [str->float, str->datetime]

    knime->>fs: Dateiimport
    pbi->>fs: Dateiimport
    dash->>fs: Dateiimport
    RDBMS->>fs: Dateiimport
    
    par Web to knime
    Web->>knime: Lesezugriff
    and Web to RDBMS
    Web->>RDBMS: Lesezugriff
    and Web to dash
    Web->>dash: Lesezugriff
    and Web to fs
    Web->>fs: Lesezugriff
    end
    PowerBI->fs: Lesezugriff



    

```