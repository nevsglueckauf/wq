# <img src="../assets/whisk_rox.png"> Data on the Rocks
## Whisky Tumbler Foo wtf

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

### Foo

```mermaid
architecture-beta
    group api(logos:aws-lambda)[API]

    service db(logos:aws-aurora)[Database] in api
    service disk1(logos:aws-glacier)[Storage] in api
    service disk2(logos:aws-s3)[Storage] in api
    service server(logos:aws-ec2)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db
```