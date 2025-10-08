# Klasse als Data Dictionary
#
# AUTHOR Sven Schrodt
# SINCE 2025-09-26
class DD:
    """ Data Dictionary class matching names<->labels(@GUI) and vice versa
    """
    
    pages = {
        "Sessions": "Sitzungsanalyse",
        "Sales": "Umsätze n. Vertriebskan.",
        "Upload": "Admin Panel",
        "Products": "Produkte",
        "Test": "Lab page",
        "Ads": "Werbeerfolge",
        "Ml": "ML Stuff",
        "Kpi": "KPIs",
        "Funnel": "Event Tpe (Funnel)"
    }

    col_transl = {
        "sess_ctry": "Land",
        "sess_loc": "Ort",
        "datum": "Datum",
        "sug_platform": "Empfehlungsplattform",
        "landing_uri": "URI Landing Page",
        "session_duration": "Sitzungsdauer",
        "pages_per_sess": "Seiten je Sitzung",
        "jump_offs": "Absprünge",
        "sess_cart_add": "Sitzung: Artikel im Warenkorb",
        "sess_co": "Sitzung: Check-Out erreicht",
        "sess_co_done": "Sitzung: Check-Out abgeschlossen",
        "sessions": "Sitzungen",
        "Sitzung_min": "Sitzungsdauer[min.]",
    }

    session_y = ["jump_offs", "sess_cart_add", "sess_co", "sess_co_done", "sessions"]

    sales_chan_y = [
        "Vertriebskanal",
        "Bestellungen",
        "Bruttoumsatz",
        "Rabatte",
        "Rückgaben",
        "Nettoumsatz",
        "Versandgebühren",
        "Steuern",
        "Gesamtumsatz",
    ]

    sess_trans_orig = {
        "sess_ctry": "Sitzungsland",
        "sess_loc": "Sitzungsort",
        "date": "Monat",
        "sug_platform": "Empfehlungsplattform",
        "landing_uri": "Landing-Page-URL",
        "session_duration": "Durchschnittliche Sitzungsdauer",
        "pages_per_sess": "Seitenaufrufe pro Sitzung",
        "jump_offs": "Absprünge",
        "sess_cart_add": "Sitzungen, in denen Artikel zum Warenkorb hinzugefügt wurden",
        "sess_co": "Sitzungen, bei denen der Checkout erreicht wurde",
        "sess_co_done": "Sitzungen, bei denen der Checkout abgeschlossen wurde",
        "sessions": "Sitzungen",
    }


# cloc --by-file --fullpath --match-d 'dash'
