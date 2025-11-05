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

<kbd>Z:> cd wq\Dashboards\python<kbd>


## VENV

### Virtuelle Umgebung einrichten

> [!IMPORTANT]  
> Einmalig durchführen!

<kbd>user@Thanos python% python3 -m venv .venv</kbd>

### Virtuelle Umgebung aktivieren

<kbd>user@Thanos python% source .venv/bin/activate</kbd>


#### Für Wintendo Boxen:


<kbd>Z:\python> .\venv\Scripts\activate</kbd>


## Dependencies auflösen


<kbd><span style="color:green">(.venv)</span> user@Thanos python%  pip install -r requirements.txt</kbd>

### Windows

<kbd><span style="color:green">(.venv)</span> Z:\python> pip install -r requirements.txt</kbd>

## App starten

<kbd><span style="color:green">(.venv)</span> user@Thanos wq% python app.py</kbd>

### mit Umlenkung von ```STDIN``` und ```STDOUT``` nach ```dev/null```

<kbd><span style="color:green">(.venv)</span> user@Thanos wq% python app.py > /dev/null  2>&1 &</kbd>

#### Für Windows

<kbd><span style="color:green">(.venv)</span> Z:\python> py.exe app.py

