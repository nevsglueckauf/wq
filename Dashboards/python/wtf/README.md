# Whisky Tele Foo wtf

Package-Name für die selbst gecodeten Python-Scripte

- Verwendung von Helferklassen zur Vermeidung von (Boilerplate-) Code
- Datenbereinigungstools
- HTML-Generierung (<abbr title="Don't repeat yourself">DRY</abbr>)
- SQL-Generierung


## wtf.container 

 - Klasse, um (HTML-) Container zu verwalten und dem DRY-Prinzip Folge zu leisten

## wtf.provider 

 - Klasse, Content für GUI zu mana


 ## wtf.sanitize

 - Generische Klasse für die Datenbereinigung

 ## wtf.generic_elements

 - Generische Klasse für die Erzeugung von HTML; DRY

## wtf.factory

 - Factory für die Erzeugung von HTML; DRY

 ### Klassendiagramm
```mermaid
 ---
title: Helper
---
classDiagram
    note for Container "Generischer Container (DRY)"
    note for ElementBuilder "Wrapper für dash.* Komponenten (DRY)"
    note for Sanitizer "Datenbereingung"
    note for Provider "Content für GUI"
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
    }
    class Sanitizer{
        +get_time_df(nm, frm, utl, freq='D', format='YYYY-mm-dd') pd.DataFrame:
    }
```