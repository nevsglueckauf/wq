# <img src="Dashboards/python/assets/whisk_rox.png"> Data on the Rocks - Projekt-Readme

## 📋 Projektübersicht

**Projektname:** Data on the Rocks  
**Kunde:** Das Whiskyquartier (Online-Shop für Whisky)  

Dieses Repository enthält die Datenanalyse und die Entwicklung eines Business Intelligence-Dashboards für Das Whiskyquartier. Das Ziel ist es, Verkaufs-, Kunden- und Produktmuster aus den Onlineshop-Daten zu identifizieren und Handlungsempfehlungen für die Preisgestaltung abzuleiten.

## 🎯 Ziele & Analyse-Schwerpunkte (Die "Vier Säulen")

Das Projekt konzentriert sich auf vier Hauptanalysen:

1.  **Trafficanalyse:** Ursprung und Volumen des Shop-Besucherverkehrs verstehen. (done)
2.  **Zielgruppenanalyse:** Demografische und verhaltensbezogene Muster der Besucher identifizieren. (optional)
3.  **Absprunganalyse:** Gründe für das vorzeitige Verlassen des Shops ("Bounce Rate") analysieren. (optional)
4.  **Conversion-Analyse:** Optimierung der Conversion-Rate und Verringerung der Abbruchrate beim Kaufabschluss. (optional)

Das Endziel ist die Bereitstellung eines PowerBI-Dashboards, das die "done" KPIs visualisiert und datengestützte Entscheidungen ermöglicht.

## 📁 Datenbasis

*   **Primärdaten:** Anonymisierte Atene-Exporte aus dem Onlineshop (CSV).
*   **Datenschutz:** Es werden keine persönlich identifizierbaren Kundendaten (PII) verarbeitet. Die Herkunft (Geodaten) ist zulässig.
*   **Zeitraum:** Daten von der Shop-Gründung (2024) bis zum 01. September 2025.
*   **Hinweis zur Datenqualität:** Die Tracking-Daten sind unvollständig, da sie auf der Cookie-Zustimmung der Nutzer basieren. Dieses Gap muss in der Analyse berücksichtigt werden.
*   **Geplante Erweiterungen:**
    *   Anbindung von Werbekampagnen-Daten für ein umfassendes Marketing-Attribution-Modell.
    *   Einbindung externer Datenquellen (z.B. von Statista) für Trend- und Marktvergleiche.

## 🛠 Technologie-Stack

*   **Datenanalyse & -processing:** Python (Pandas, NumPy, SciKit-Learn)
*   **Datenvisualisierung & Dashboarding:** Microsoft Power BI
*   **Versionskontrolle & Kollaboration:** Git / GitHub

## 📊 Erwartetes Ergebnis

Das Endprodukt dieses Projekts ist ein umfassendes PowerBI-Dashboard, das:
*   Die wichtigsten KPIs zur Säule "Traffic" optional zu den weiteren drei Säulen übersichtlich visualisiert.
*   Interaktiv und filterbar ist.
*   Einfach um neue Daten aktualisiert werden kann (Skripte sind entsprechend zu gestalten).
*   Handlungsempfehlungen, insbesondere für die Preisgestaltung, ableitet.
*   Optional: Qualitative Hinweise zur Optimierung der Benutzeroberfläche und des Checkout-Prozesses des Onlineshops.

## 🔄 Projektablauf & Kommunikation

*   Der Projektablauf orientiert sich an agilen Methoden (Scrumban).
*   **Statusmeetings** finden alle zwei Wochen statt.
*   Der laufende Austausch erfolgt über **WhatsApp und E-Mail**.
*   Dieses GitHub-Repository dient als zentrale Quelle für Code, Dokumentation und Issue-Tracking.
