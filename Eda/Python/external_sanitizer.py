# Sanitizer Script für CSV Dateien
#
# AUTHOR Sven 

import pandas as pd
import glob
name = "2019-Nov.csv"


def sanitize(name):
    """
    Datenbereinigung:
    - Nur Elektronikprodukte
    - NAs löschen
    - Spalte umwandeln: event_time (DateTime) -> date (Nur Datum nach ISO YYYY-MM-DD)
    """
    df = pd.read_csv(name) # CSV in Dataframe lesen
    df["date"] = df["event_time"].str[0:10] # Neue Spalte aus event_time (DateTime) -> date (Nur Datum nach ISO YYYY-MM-DD)
    df.dropna(inplace=True) # NA Values flach legen
    df_elec  = df[df["category_code"].str.startswith("electronics")] # Nicht-Elektronik-Podukte ausfiltern
    # Datei schreiben (ohne Spalte event_time)
    df_elec[["date","event_type","product_id","category_id","category_code","brand","price","user_id","user_session"]].to_csv('Elec-' + name, index=False)
    print(df_elec.head())



# for name in glob.glob("./*csv"):
#     print(name)
#
sanitize("2020-Apr.csv")