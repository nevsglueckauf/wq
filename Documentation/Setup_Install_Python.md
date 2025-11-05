# <img src="../Dashboards/python/assets/whisk_rox.png"> „Data on the rocks“

## Setup Beispiel für X

> [!TIP]  
> Komplett für  UNIX like OS (MacOS, Linux, Solaris etc.) 
> -> für **Win**tendo Boxen mit Hinweisen

## Repo clonen

<kbd>git clone https://github.com/nevsglueckauf/wq</kbd>



## Verzeichniswechsel

<kbd>cd wq/Dashboards/python </kbd>

### In Windows

<kbd>Z:\wq> <kbd>```cd wq\Dashboards\python```

<kbd>cd wq/ Dashboards/python </kbd>

## VENV

### Virtuelle Umgebung einrichten

> [!IMPORTANT]  
> Einmalig durchführen! 

<code>sven@Thanos wq% </code><kbd>python3 -m venv .venv</kbd>

### Virtuelle Umgebung aktivieren

<code>sven@Thanos python% </code><kbd>source .venv/bin/activate</kbd>

<code><span style="color:green">(.venv)</span> sven@Thanos python% </code>

#### Für Wintendo Boxen:


<kbd>Z:\python> <kbd>.\venv\Scripts\activate


## Dependencies auflösen


<code><span style="color:green">(.venv)</span> sven@Thanos python% </code><kbd>pip install -r requirements.txt</kbd>

### Windows

<kbd>Z:\python> <kbd>pip install -r requirements.txt

## App starten

Bootstrap starten mit Umlenkung von ```STDIN``` und ```STDOUT``` nach ```dev/null```

```sh
(.venv) svenschrodt@Thanos wq% python app.py > /dev/null  2>&1 &
```

#### Für Windows

```PS
Z:\python> py.exe app.py
```

