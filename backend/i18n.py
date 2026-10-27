"""Traducciones para las etiquetas que el puente MQTT (`backend/mqtt_bridge.py`) publica en
Home Assistant: nombres de entidad y opciones de los `select` (potencia, agua, mopa, modo,
tipo de base, frecuencia de vaciado).

Mismo conjunto de 9 idiomas que la interfaz web (ver el bloque i18n en
`backend/static/index.html`): el ESPAÑOL es la fuente de la verdad (clave = texto en
español); solo se listan los idiomas que difieren, y lo que falte cae al español. Varias
cadenas se han tomado literalmente del diccionario de la web para que la terminología
coincida entre la interfaz y las entidades de Home Assistant — son dos diccionarios
independientes (la web traduce HTML/JS en el navegador, esto traduce payloads MQTT en el
backend), pero conviene que digan lo mismo.

Nota: los DATOS del usuario (nombres de habitaciones, mapas, horarios) nunca se traducen
aquí tampoco, igual que en la web — solo las palabras fijas ("Limpiar", "Horario",
"Ejecutar"...) que las acompañan en el nombre de la entidad.
"""
from __future__ import annotations

# Mismo orden/códigos que `VALID` en el bloque i18n de backend/static/index.html.
VALID_LANGS = ("es", "en", "de", "it", "fr", "pt", "nl", "ca", "pl")

STR: dict[str, dict[str, str]] = {
    # — dispositivo / sensores de estado —
    "Batería": {"en": "Battery", "pt": "Bateria", "fr": "Batterie", "pl": "Bateria",
                "de": "Akku", "it": "Batteria", "nl": "Batterij", "ca": "Bateria"},
    "Área limpiada": {"en": "Area cleaned", "pt": "Área limpa", "fr": "Surface nettoyée",
                       "pl": "Posprzątana powierzchnia", "de": "Gereinigte Fläche",
                       "it": "Area pulita", "nl": "Schoongemaakt oppervlak",
                       "ca": "Àrea netejada"},
    "Tiempo limpieza": {"en": "Cleaning time", "pt": "Tempo de limpeza",
                         "fr": "Durée de nettoyage", "pl": "Czas sprzątania",
                         "de": "Reinigungszeit", "it": "Tempo di pulizia",
                         "nl": "Schoonmaaktijd", "ca": "Temps de neteja"},
    "Posición": {"en": "Position", "pt": "Posição", "fr": "Position", "pl": "Pozycja",
                 "de": "Position", "it": "Posizione", "nl": "Positie", "ca": "Posició"},
    "Habitación actual": {"en": "Current room", "pt": "Divisão atual", "fr": "Pièce actuelle",
                           "pl": "Aktualne pomieszczenie", "de": "Aktueller Raum",
                           "it": "Stanza attuale", "nl": "Huidige kamer",
                           "ca": "Habitació actual"},
    "Habitación": {"en": "Room", "pt": "Divisão", "fr": "Pièce", "pl": "Pomieszczenie",
                   "de": "Raum", "it": "Stanza", "nl": "Kamer", "ca": "Habitació"},
    "Mapa": {"en": "Map", "pt": "Mapa", "fr": "Carte", "pl": "Mapa", "de": "Karte",
             "it": "Mappa", "nl": "Kaart", "ca": "Mapa"},
    "Mapa imagen": {"en": "Map image", "pt": "Imagem do mapa", "fr": "Image de la carte",
                     "pl": "Obraz mapy", "de": "Kartenbild", "it": "Immagine mappa",
                     "nl": "Kaartafbeelding", "ca": "Imatge del mapa"},
    "Falta agua": {"en": "Low water", "pt": "Falta de água", "fr": "Manque d'eau",
                   "pl": "Brak wody", "de": "Wasser fehlt", "it": "Acqua mancante",
                   "nl": "Water laag", "ca": "Falta d'aigua"},
    "Aviso": {"en": "Warning", "pt": "Aviso", "fr": "Avertissement", "pl": "Ostrzeżenie",
              "de": "Hinweis", "it": "Avviso", "nl": "Waarschuwing", "ca": "Avís"},

    # — batería (salud) —
    "Ciclos de batería": {"en": "Battery cycles", "pt": "Ciclos de bateria",
                           "fr": "Cycles de batterie", "pl": "Cykle baterii",
                           "de": "Akkuzyklen", "it": "Cicli batteria",
                           "nl": "Batterijcycli", "ca": "Cicles de bateria"},
    "Salud de batería": {"en": "Battery health", "pt": "Saúde da bateria",
                          "fr": "État de la batterie", "pl": "Kondycja baterii",
                          "de": "Akkuzustand", "it": "Salute della batteria",
                          "nl": "Batterijgezondheid", "ca": "Salut de la bateria"},
    "Consumo de batería": {"en": "Battery drain", "pt": "Consumo da bateria",
                            "fr": "Consommation de la batterie", "pl": "Zużycie baterii",
                            "de": "Akkuverbrauch", "it": "Consumo batteria",
                            "nl": "Batterijverbruik", "ca": "Consum de bateria"},
    "Velocidad de carga": {"en": "Charging speed", "pt": "Velocidade de carga",
                            "fr": "Vitesse de charge", "pl": "Szybkość ładowania",
                            "de": "Ladegeschwindigkeit", "it": "Velocità di carica",
                            "nl": "Laadsnelheid", "ca": "Velocitat de càrrega"},

    # — consumibles —
    "Cepillo central": {"en": "Main brush", "pt": "Escova central", "fr": "Brosse centrale",
                         "pl": "Szczotka główna", "de": "Hauptbürste",
                         "it": "Spazzola centrale", "nl": "Hoofdborstel",
                         "ca": "Raspall central"},
    "Cepillo lateral": {"en": "Side brush", "pt": "Escova lateral", "fr": "Brosse latérale",
                         "pl": "Szczotka boczna", "de": "Seitenbürste",
                         "it": "Spazzola laterale", "nl": "Zijborstel",
                         "ca": "Raspall lateral"},
    "Filtro": {"en": "Filter", "pt": "Filtro", "fr": "Filtre", "pl": "Filtr", "de": "Filter",
               "it": "Filtro", "nl": "Filter", "ca": "Filtre"},
    "Mopa": {"en": "Mop", "pt": "Mopa", "fr": "Serpillière", "pl": "Mop", "de": "Wischtuch",
             "it": "Panno", "nl": "Dweil", "ca": "Mopa"},
    "Restablecer": {"en": "Reset", "pt": "Repor", "fr": "Réinitialiser", "pl": "Zresetuj",
                     "de": "Zurücksetzen", "it": "Reimposta", "nl": "Resetten",
                     "ca": "Restablir"},

    # — sensores (mantenimiento cada 35 h) —
    "Horas desde limpiar sensores": {
        "en": "Hours since sensor cleaning", "pt": "Horas desde a limpeza dos sensores",
        "fr": "Heures depuis le nettoyage des capteurs",
        "pl": "Godziny od czyszczenia czujników", "de": "Stunden seit Sensorreinigung",
        "it": "Ore dall'ultima pulizia dei sensori", "nl": "Uren sinds sensorreiniging",
        "ca": "Hores des de la neteja de sensors"},
    "Limpiar sensores": {"en": "Clean sensors", "pt": "Limpar sensores",
                          "fr": "Nettoyer les capteurs", "pl": "Wyczyść czujniki",
                          "de": "Sensoren reinigen", "it": "Pulisci sensori",
                          "nl": "Sensoren schoonmaken", "ca": "Netejar sensors"},
    "Sensores limpiados": {"en": "Sensors cleaned", "pt": "Sensores limpos",
                            "fr": "Capteurs nettoyés", "pl": "Czujniki wyczyszczone",
                            "de": "Sensoren gereinigt", "it": "Sensori puliti",
                            "nl": "Sensoren schoongemaakt", "ca": "Sensors netejats"},

    # — botones de habitación / horarios (la parte fija del nombre; el nombre de la
    #   habitación/horario en sí es dato del usuario y no se traduce) —
    "Limpiar": {"en": "Clean", "pt": "Limpar", "fr": "Nettoyer", "pl": "Sprzątaj",
                "de": "Reinigen", "it": "Pulisci", "nl": "Schoonmaken", "ca": "Netejar"},
    "Horario": {"en": "Schedule", "pt": "Horário", "fr": "Horaire", "pl": "Harmonogram",
                "de": "Zeitplan", "it": "Programmazione", "nl": "Schema", "ca": "Horari"},
    "Ejecutar": {"en": "Run", "pt": "Executar", "fr": "Exécuter", "pl": "Uruchom",
                 "de": "Ausführen", "it": "Esegui", "nl": "Uitvoeren", "ca": "Executar"},

    # — selectores —
    "Potencia succión": {"en": "Suction power", "pt": "Potência de sucção",
                          "fr": "Puissance d'aspiration", "pl": "Moc ssania",
                          "de": "Saugleistung", "it": "Potenza di aspirazione",
                          "nl": "Zuigkracht", "ca": "Potència de succió"},
    "Nivel agua": {"en": "Water level", "pt": "Nível de água", "fr": "Niveau d'eau",
                   "pl": "Poziom wody", "de": "Wasserstand", "it": "Livello dell'acqua",
                   "nl": "Waterniveau", "ca": "Nivell d'aigua"},
    "Vibración mopa": {"en": "Mop vibration", "pt": "Vibração da mopa",
                        "fr": "Vibration de la serpillière", "pl": "Wibracja mopa",
                        "de": "Wischtuch-Vibration", "it": "Vibrazione del panno",
                        "nl": "Dweiltrilling", "ca": "Vibració de la mopa"},
    "Modo de limpieza": {"en": "Cleaning mode", "pt": "Modo de limpeza",
                          "fr": "Mode de nettoyage", "pl": "Tryb sprzątania",
                          "de": "Reinigungsmodus", "it": "Modalità di pulizia",
                          "nl": "Schoonmaakmodus", "ca": "Mode de neteja"},
    "Tipo de base": {"en": "Dock type", "pt": "Tipo de base", "fr": "Type de base",
                      "pl": "Typ bazy", "de": "Stationstyp", "it": "Tipo di base",
                      "nl": "Type basisstation", "ca": "Tipus de base"},

    # — opciones de los selectores (texto de origen = clave canónica en conga_core.commands,
    #   salvo "Máx" -- usado solo en el backend legacy, ver FAN_LABELS_LEGACY en mqtt_bridge.py) —
    "Máx": {"en": "Max", "pt": "Máx", "fr": "Max", "pl": "Maks", "de": "Max", "it": "Max",
            "nl": "Max", "ca": "Màx"},
    "Eco": {},
    "Normal": {},
    "Turbo": {},
    "Bajo": {"en": "Low", "pt": "Baixo", "fr": "Faible", "pl": "Niski", "de": "Niedrig",
             "it": "Basso", "nl": "Laag", "ca": "Baix"},
    "Medio": {"en": "Medium", "pt": "Médio", "fr": "Moyen", "pl": "Średni", "de": "Mittel",
              "it": "Medio", "nl": "Gemiddeld", "ca": "Mitjà"},
    "Alto": {"en": "High", "pt": "Alto", "fr": "Élevé", "pl": "Wysoki", "de": "Hoch",
             "it": "Alto", "nl": "Hoog", "ca": "Alt"},
    "Estándar": {"en": "Standard", "pt": "Padrão", "fr": "Standard", "pl": "Standard",
                 "de": "Standard", "it": "Standard", "nl": "Standaard", "ca": "Estàndard"},
    "Fuerte": {"en": "Strong", "pt": "Forte", "fr": "Fort", "pl": "Mocny", "de": "Stark",
               "it": "Forte", "nl": "Sterk", "ca": "Fort"},
    "Potente": {"en": "Powerful", "pt": "Potente", "fr": "Puissant", "pl": "Bardzo mocny",
                "de": "Sehr stark", "it": "Potente", "nl": "Krachtig", "ca": "Potent"},
    "Auto": {},
    "Limpieza completa": {"en": "Full clean", "pt": "Limpeza completa",
                           "fr": "Nettoyage complet", "pl": "Pełne sprzątanie",
                           "de": "Komplettreinigung", "it": "Pulizia completa",
                           "nl": "Volledige schoonmaak", "ca": "Neteja completa"},
    "Fregado": {"en": "Mopping", "pt": "Lavagem", "fr": "Lavage", "pl": "Mopowanie",
                "de": "Wischen", "it": "Lavaggio", "nl": "Dweilen", "ca": "Fregat"},
    "Bordes": {"en": "Edges", "pt": "Bordas", "fr": "Bords", "pl": "Krawędzie",
               "de": "Kanten", "it": "Bordi", "nl": "Randen", "ca": "Vores"},
    "Espiral": {"en": "Spiral", "pt": "Espiral", "fr": "Spirale", "pl": "Spirala",
                "de": "Spirale", "it": "Spirale", "nl": "Spiraal", "ca": "Espiral"},
    "Espiral cuadrada": {"en": "Square spiral", "pt": "Espiral quadrada",
                          "fr": "Spirale carrée", "pl": "Kwadratowa spirala",
                          "de": "Eckige Spirale", "it": "Spirale quadrata",
                          "nl": "Vierkante spiraal", "ca": "Espiral quadrada"},
    "Punto": {"en": "Spot", "pt": "Ponto", "fr": "Point", "pl": "Punkt", "de": "Punkt",
              "it": "Punto", "nl": "Plek", "ca": "Punt"},
    "Base de carga": {"en": "Charging dock", "pt": "Base de carga", "fr": "Base de charge",
                       "pl": "Baza ładująca", "de": "Ladestation", "it": "Base di ricarica",
                       "nl": "Laadstation", "ca": "Base de càrrega"},
    "Colector automático": {"en": "Auto-empty dock", "pt": "Coletor automático",
                             "fr": "Bac auto-vidage", "pl": "Automatyczne opróżnianie",
                             "de": "Absaugstation", "it": "Svuotamento automatico",
                             "nl": "Automatische opvangbak", "ca": "Col·lector automàtic"},
    # "Off" (agua/mopa) se deja SIN traducir a propósito, igual que en la web.

    # — frecuencia de vaciado automático —
    "Nunca": {"en": "Never", "pt": "Nunca", "fr": "Jamais", "pl": "Nigdy", "de": "Nie",
              "it": "Mai", "nl": "Nooit", "ca": "Mai"},
    "Después de cada limpieza": {"en": "After every cleaning", "pt": "Depois de cada limpeza",
                                  "fr": "Après chaque nettoyage", "pl": "Po każdym sprzątaniu",
                                  "de": "Nach jeder Reinigung", "it": "Dopo ogni pulizia",
                                  "nl": "Na elke schoonmaakbeurt",
                                  "ca": "Després de cada neteja"},
    "Cada 30 minutos": {"en": "Every 30 minutes", "pt": "A cada 30 minutos",
                         "fr": "Toutes les 30 minutes", "pl": "Co 30 minut",
                         "de": "Alle 30 Minuten", "it": "Ogni 30 minuti",
                         "nl": "Elke 30 minuten", "ca": "Cada 30 minuts"},
    "Cada 60 minutos": {"en": "Every 60 minutes", "pt": "A cada 60 minutos",
                         "fr": "Toutes les 60 minutes", "pl": "Co 60 minut",
                         "de": "Alle 60 Minuten", "it": "Ogni 60 minuti",
                         "nl": "Elke 60 minuten", "ca": "Cada 60 minuts"},
    "Cada 90 minutos": {"en": "Every 90 minutes", "pt": "A cada 90 minutos",
                         "fr": "Toutes les 90 minutes", "pl": "Co 90 minut",
                         "de": "Alle 90 Minuten", "it": "Ogni 90 minuti",
                         "nl": "Elke 90 minuten", "ca": "Cada 90 minuts"},
    "Cada 2 horas": {"en": "Every 2 hours", "pt": "A cada 2 horas",
                      "fr": "Toutes les 2 heures", "pl": "Co 2 godziny",
                      "de": "Alle 2 Stunden", "it": "Ogni 2 ore", "nl": "Elke 2 uur",
                      "ca": "Cada 2 hores"},

    # — switches / number / text —
    "Doble pasada (x2)": {"en": "Double pass (x2)", "pt": "Passagem dupla (x2)",
                           "fr": "Double passage (x2)", "pl": "Podwójne przejście (x2)",
                           "de": "Doppelter Durchgang (x2)", "it": "Doppio passaggio (x2)",
                           "nl": "Dubbele beurt (x2)", "ca": "Doble passada (x2)"},
    "Turbo en alfombras": {"en": "Carpet turbo", "pt": "Turbo em tapetes",
                            "fr": "Turbo sur tapis", "pl": "Turbo na dywanach",
                            "de": "Teppich-Turbo", "it": "Turbo sui tappeti",
                            "nl": "Tapijt-turbo", "ca": "Turbo a catifes"},
    "No molestar": {"en": "Do not disturb", "pt": "Não incomodar", "fr": "Ne pas déranger",
                     "pl": "Nie przeszkadzać", "de": "Nicht stören", "it": "Non disturbare",
                     "nl": "Niet storen", "ca": "No molestar"},
    "Voz": {"en": "Voice", "pt": "Voz", "fr": "Voix", "pl": "Głos", "de": "Sprachausgabe",
            "it": "Voce", "nl": "Spraak", "ca": "Veu"},
    "Actualizaciones automáticas": {"en": "Automatic updates", "pt": "Atualizações automáticas",
                                     "fr": "Mises à jour automatiques",
                                     "pl": "Automatyczne aktualizacje",
                                     "de": "Automatische Updates",
                                     "it": "Aggiornamenti automatici",
                                     "nl": "Automatische updates",
                                     "ca": "Actualitzacions automàtiques"},
    "Volumen voz": {"en": "Voice volume", "pt": "Volume da voz", "fr": "Volume de la voix",
                     "pl": "Głośność głosu", "de": "Sprachlautstärke", "it": "Volume vocale",
                     "nl": "Spraakvolume", "ca": "Volum de veu"},
    "No molestar inicio": {"en": "Do not disturb start", "pt": "Início não incomodar",
                            "fr": "Début ne pas déranger",
                            "pl": "Początek trybu nie przeszkadzać",
                            "de": "Nicht-stören-Beginn", "it": "Inizio non disturbare",
                            "nl": "Begin niet storen", "ca": "Inici no molestar"},
    "No molestar fin": {"en": "Do not disturb end", "pt": "Fim não incomodar",
                         "fr": "Fin ne pas déranger", "pl": "Koniec trybu nie przeszkadzać",
                         "de": "Nicht-stören-Ende", "it": "Fine non disturbare",
                         "nl": "Einde niet storen", "ca": "Fi no molestar"},
    "Vaciar base": {"en": "Empty dock", "pt": "Esvaziar base", "fr": "Vider la base",
                     "pl": "Opróżnij bazę", "de": "Station leeren", "it": "Svuota base",
                     "nl": "Basis leegmaken", "ca": "Buidar base"},
    "Frecuencia de vaciado": {"en": "Emptying frequency", "pt": "Frequência de esvaziamento",
                               "fr": "Fréquence de vidage", "pl": "Częstotliwość opróżniania",
                               "de": "Entleerungshäufigkeit", "it": "Frequenza di svuotamento",
                               "nl": "Legingsfrequentie", "ca": "Freqüència de buidatge"},

    # — aviso de conexión MQTT perdida (persistent_notification en HA; ver
    # MqttBridge.ha_notify_provider / app.py) —
    "Clean Assistant: conexión MQTT perdida": {
        "en": "Clean Assistant: MQTT connection lost",
        "pt": "Clean Assistant: ligação MQTT perdida",
        "fr": "Clean Assistant : connexion MQTT perdue",
        "pl": "Clean Assistant: utracono połączenie MQTT",
        "de": "Clean Assistant: MQTT-Verbindung verloren",
        "it": "Clean Assistant: connessione MQTT persa",
        "nl": "Clean Assistant: MQTT-verbinding verloren",
        "ca": "Clean Assistant: connexió MQTT perduda"},
    "Clean Assistant ha perdido la conexión con el broker MQTT. Las entidades del robot pueden quedar sin actualizar hasta que se restablezca.": {
        "en": "Clean Assistant has lost its connection to the MQTT broker. The robot's entities may stop updating until it's restored.",
        "pt": "O Clean Assistant perdeu a ligação ao broker MQTT. As entidades do robô podem deixar de atualizar até ser restabelecida.",
        "fr": "Clean Assistant a perdu la connexion au broker MQTT. Les entités du robot risquent de ne plus se mettre à jour tant qu'elle n'est pas rétablie.",
        "pl": "Clean Assistant utracił połączenie z brokerem MQTT. Encje robota mogą przestać się aktualizować do czasu przywrócenia połączenia.",
        "de": "Clean Assistant hat die Verbindung zum MQTT-Broker verloren. Die Entitäten des Roboters werden möglicherweise nicht mehr aktualisiert, bis sie wiederhergestellt ist.",
        "it": "Clean Assistant ha perso la connessione al broker MQTT. Le entità del robot potrebbero smettere di aggiornarsi finché non viene ripristinata.",
        "nl": "Clean Assistant heeft de verbinding met de MQTT-broker verloren. De entiteiten van de robot worden mogelijk niet meer bijgewerkt totdat deze is hersteld.",
        "ca": "Clean Assistant ha perdut la connexió amb el broker MQTT. Les entitats del robot poden deixar d'actualitzar-se fins que es restableixi."},
}


def t(lang: str | None, text: str) -> str:
    """Traduce `text` (en español) al idioma `lang`. Si `lang` es None/'es'/desconocido, o si
    `text` no está en el diccionario, o si no hay traducción para ese idioma concreto,
    devuelve `text` tal cual (igual que el t() de la web: el español es siempre el valor por
    defecto). Nunca lanza excepción -- un idioma mal guardado en prefs.json simplemente cae
    al español en vez de romper el descubrimiento de HA."""
    if not text or not lang or lang == "es":
        return text
    return STR.get(text, {}).get(lang, text)
