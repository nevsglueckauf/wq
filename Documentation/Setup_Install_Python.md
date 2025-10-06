# Setup Beispiel 

Komplett für  UNIX like OS (MacOS, Linux, Solaris etc.) -> für Wintendo Boxen mit Hinweisen

## Repo clonen

<kbd>git clone https://github.com/nevsglueckauf/wq</kbd>

<kbd>cd wq</kbd>



## VENV

### Virtuelle Umgebung einrichten
<code>sven@Thanos gesundheit% </code><kbd>python3 -m venv .venv</kbd>

### Virtuelle Umgebung aktivieren
<code>sven@Thanos gesundheit% </code><kbd>source .venv/bin/activate</kbd>

<code><span style="color:green">(.venv)</span> sven@Thanos gesundheit% </code>

#### Für Wintendo Boxen:

```PS
.venv\Scripts\activate
```

## Dependencies auflösen

<code><span style="color:green">(.venv)</span> sven@Thanos gesundheit% </code><kbd>pip install -r req.txt</kbd>

## App starten
Bootstrap starten mit Umlenkung von ```STDIN``` und ```STDOUT``` nach ```dev/null```

```sh
(.venv) svenschrodt@Thanos gesundheit% python app.py > /dev/null  2>&1 &
```

#### Für Wintendo Boxen:

```PS
Z:\gesundheit> py.exe app.py
```