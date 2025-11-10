# <img src="../assets/whisk_rox.png"> Data on the Rocks

## Package Whisky Tumbler Foo (wtf)

Package-Name für die selbst gecodeten Python-Scripte

- Verwendung von Helferklassen zur Vermeidung von (Boilerplate-) Code
- Datenbereinigungstools
- HTML-Generierung (<abbr title="Don't repeat yourself">DRY</abbr>)
- SQL-Generierung

### wtf.container

- Klasse, um (HTML-) Container zu verwalten und dem DRY-Prinzip Folge zu leisten

### wtf.provider

- Content für GUI managen

### wtf.sanitize

- Generische Klasse für die Datenbereinigung

### wtf.generic_elements

- Generische Klasse für die Erzeugung von HTML; DRY

### wtf.factory

- Factory für die Erzeugung von HTML; DRY

#### Klassendiagramm

```mermaid
 ---
title: Helper
---
classDiagram
    note for Container "Generischer Container (DRY)"
    note for ElementBuilder "Wrapper für dash.* Komponenten (DRY)"
    note for Sanitizer "Datenbereingung"
    note for Provider "Content für GUI"
    note for TabFactory "Factory für Tab Content"

    class Container{
        +String rt = None
        +String dta = None
        +apd(self, dta) Self
        +apd_row(self, dta) Self
        +rndr_in(self, rt = "Div") list
    }
    ElementBuilder --> "many" Container : Uses
   
   
    ElementBuilder : +int id
    ElementBuilder : +String title_el = "h3"
    ElementBuilder: +init(self)
    ElementBuilder: +card(dta, title = "", img_src="", wdth="23rem") dbc.Card
    ElementBuilder: +dd(df, strt_colz=[], id="") dcc.Dropdown
    ElementBuilder: col(ctnt) dbc.Col
    ElementBuilder: row(ctnt) dbc.Row
    ElementBuilder: row(rows) list
   
    class Provider{
       
        +get_brands(self) list
        +get_sales_per(self, mode="daily") list

    }
    class Sanitizer{
        +get_time_df(nm, frm, utl, freq='D', format='YYYY-mm-dd') pd.DataFrame
    }

    class TabFactory{
        +df(ds, dt= "") pd.DataFrame
        +generic(ds) html.Div
        +grid()

    }
   

    style DataFrame fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5

    class DataFrame{

    }
```
## Architektur

### Multi-Tier-Modell Dash

```mermaid
sequenceDiagram
autonumber
    
    box lightblue User, Browser
    participant User-Agent
    end

    box ORANGE  Python & Libs
    participant Pandas
    participant Dash
    participant Plotly
    participant Flask
    end

    box gray Persistente Daten
    participant CSV
    participant SQL
    end
    
    User-Agent->>Flask: Anfrage URI
    Note over User-Agent, Flask: HTTP-Request
    
    Flask->>Dash: URI parsen
    Dash->>Pandas: Daten anfordern
    Pandas ->> CSV: Daten holen
    Pandas ->> Dash: Daten aufbereitet weiterleiten
    Pandas ->> Plotly: Charts/Plots erstellen
    Pandas ->> Flask: Webinhalte anfordern 
    Pandas ->> SQL: Daten persistieren 
    Flask --> Flask: Generiere HTML, CSS, Javascript
    
    Flask->>User-Agent: Webinhalte liefern
    Note over User-Agent, Flask: HTTP-Request
    

   
   
```