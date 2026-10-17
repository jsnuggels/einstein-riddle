"""
Ein Rätsel, das (nur der Legende nach) von Albert Einstein ist (Klasse von Rätseln)
1) Es gibt fünf Häuser mit je einer anderen Farbe
2) In jedem Haus wohnt eine Person einer anderen Nationalität
3) Jeder Hausbewohner bevorzugt ein bestimmtes Getränk, raucht eine bestimmte
Zigarettenmarke und hält ein bestimmtes Haustier
4) Keine der 5 Personen bevorzugt das gleiche Getränk, raucht die gleiche
Zigarettenmarke oder hält das gleiche Tier wie irgend eine der anderen Personen
5) Der Brite lebt im roten Haus
6) Der Schwede hält einen Hund
7) Der Däne trinkt gerne Tee
8) Der Deutsche raucht Rothmanns
9) Der Besitzer des grünen Hauses trinkt Kaffee
10) Der Winfield-Raucher trinkt gerne Bier
11) Der Norweger wohnt im ersten Haus
12) Der Norweger wohnt neben dem blauen Haus
13) Der Besitzer des gelben Hauses raucht Dunhill
14) Die Person, die Pall Mall raucht, hält einen Vogel
15) Der Mann, der im mittleren Haus wohnt, trinkt Milch
16) Das grüne Haus steht unmittelbar links vom weißen Haus
17) Der Marlboro-Raucher wohnt neben dem, der eine Katze hält
18) Der Marlboro-Raucher hat einen Nachbarn, der Wasser trinkt
19) Der Mann, der ein Pferd hält, wohnt neben dem, der Dunhill raucht


Frage: wer hält einen Fisch als Haustier?
"""

# Dictionary mit sets mit möglichen Values zum Vergleichen
Alles = {
    "farbe": {"Rot", "Grün", "Blau", "Gelb", "Weiß"},
    "nationalität": {"Deutscher", "Brite", "Däne", "Schwede", "Norweger"}
}


# Datenstrukturen für Häuser

haus_1 = {
    "farbe": "",
    "nationalität": "",
    "getränk": "",
    "nikotinabusus": "",
    "haustier": "",
    "verbotene_values": {
        "farbe": set(),
        "nationalität": set(),
        "getränk": set(),
        "nikotinabusus": set(),
        "haustier": set()
    }
}

haus_2 = {
    "farbe": "",
    "nationalität": "",
    "getränk": "",
    "nikotinabusus": "",
    "haustier": "",
    "verbotene_values": {
        "farbe": set(),
        "nationalität": set(),
        "getränk": set(),
        "nikotinabusus": set(),
        "haustier": set()
    }
}

haus_3 = {
    "farbe": "",
    "nationalität": "",
    "getränk": "",
    "nikotinabusus": "",
    "haustier": "",
    "verbotene_values": {
        "farbe": set(),
        "nationalität": set(),
        "getränk": set(),
        "nikotinabusus": set(),
        "haustier": set()
    }
}

haus_4 = {
    "farbe": "",
    "nationalität": "",
    "getränk": "",
    "nikotinabusus": "",
    "haustier": "",
    "verbotene_values": {
        "farbe": set(),
        "nationalität": set(),
        "getränk": set(),
        "nikotinabusus": set(),
        "haustier": set()
    }
}

haus_5 = {
    "farbe": "",
    "nationalität": "",
    "getränk": "",
    "nikotinabusus": "",
    "haustier": "",
    "verbotene_values": {
        "farbe": set(),
        "nationalität": set(),
        "getränk": set(),
        "nikotinabusus": set(),
        "haustier": set()
    }
}

häuser = [haus_1, haus_2, haus_3, haus_4, haus_5]

lösung = "to be found..."

"""

"""
def check_Häuser(aktuelle_häuser):
    print("testing seiteneffekte because yaaaay seiteneffekte")
    for haus in aktuelle_häuser:
        print(haus)
        zähler = 0
        for x in haus.values():
            if x == "":
                zähler += 1
        if zähler > 0:
            lösung = "I'm tired of this grandpa WELL THAT'S TOO DAMN BAD >:("
        else:
            lösung = "finally finished"
            
        

def regel_5(aktuelle_häuser):
# 5) Der Brite lebt im roten Haus
    for haus in aktuelle_häuser:
        if haus["farbe"] == "Rot":
            haus["nationalität"] = "Brite"

def regel_6(akthä):
# 6) Der Schwede hält einen Hund
    for haus in akthä:
        if haus["nationalität"] == "Schwede":
            haus["haustier"] = "Hund"

def regel_7(akthä):
# 7) Der Däne trinkt gerne Tee
    for haus in akthä:
        if haus["nationalität"] == "Däne":
            haus["getränk"] = "Tee"

def regel_8(akthä):
# 8) Der Deutsche raucht Rothmanns
    for haus in akthä:
        if haus["nationalität"] == "Deutscher":
            haus["nikotinabusus"] = "Rothmanns"
        if haus["nikotinabusus"] == "Rothmanns":
            haus["nationalität"] = "Deutscher"

def regel_9(akthä):
# 9) Der Besitzer des grünen Hauses trinkt Kaffee
    for haus in akthä:
        if haus["farbe"] == "Grün":
            haus["getränk"] = "Kaffee"

def regel_10(akthä):
# 10) Der Winfield-Raucher trinkt gerne Bier
    for haus in akthä:
        if haus["nikotinabusus"] == "Winfield":
            haus["getränk"] = "Bier"

def regel_11(akthä):
# 11) Der Norweger wohnt im ersten Haus
    akthä[0]["nationalität"] = "Norweger"
    haus1_no_gos = akthä[0]["verbotene_values"]
    haus1_no_gos["farbe"].add("Rot") # Regel 5
    haus1_no_gos["farbe"].add("Blau") # Regel 12
    haus1_no_gos["farbe"].add("Weiß") # Regel 16

def regel_12(akthä):
# 12) Der Norweger wohnt neben dem blauen Haus
    for haus in akthä:
        if haus["nationalität"] == "Norweger":
            hausstelle = akthä.index(haus)
            # dadurch dass wir aus regel 11 wissen dass der Norweger im ersten Haus wohnt, müssen wir kein davorstehendes Haus checken. da steht keins.
            # also speichern wir gleich im rechten Haus weil was anderes ist mir grad zu kompliziert deal with it
            akthä[hausstelle+1]["farbe"] = "Blau"
            akthä[hausstelle]["verbotene_values"]["farbe"].add("Grün") # Regel 16

def regel_13(akthä):
# 13) Der Besitzer des gelben Hauses raucht Dunhill
    for haus in akthä:
        if haus["farbe"] == "Gelb":
            haus["nikotinabusus"] = "Dunhill"

def regel_14(akthä):
# 14) Die Person, die Pall Mall raucht, hält einen Vogel
    for haus in akthä:
        if haus["nikotinabusus"] == "Pall Mall":
            haus["haustier"] = "Vogel"

def regel_15(akthä):
# 15) Der Mann, der im mittleren Haus wohnt, trinkt Milch
    akthä[2]["getränk"] = "Milch"
    akthä[2]["verbotene_values"]["nationalität"].add("Däne") # Aus Regel 7
    akthä[2]["verbotene_values"]["farbe"].add("Grün") # Aus Regel 9
    akthä[2]["verbotene_values"]["nikotinabusus"].add("Winfield") # Aus Regel 10

def regel_16(akthä):
# 16) Das grüne Haus steht unmittelbar links vom weißen Haus
    akthä[4]["verbotene_values"]["farbe"].add("Grün") # letztes Haus kann nicht grün sein laut der Regel
    for haus in akthä:
        if haus["farbe"] == "Weiß":
            hausstelle = akthä.index(haus)
            akthä[hausstelle-1]["farbe"] = "Grün"
        elif haus["farbe"] == "Grün":
            hausstelle = akthä.index(haus)
            akthä[hausstelle+1]["farbe"] = "Weiß"

def regel_17(akthä):
# 17) Der Marlboro-Raucher wohnt neben dem, der eine Katze hält
    for haus in akthä:
        if haus["nikotinabusus"] == "Marlboro":
            hausstelle = akthä.index(haus)
            linkes_haus = akthä[hausstelle-1]
            rechtes_haus= akthä[hausstelle+1]
            if (check_verbotene_values(linkes_haus, "haustier", "Katze") == False) and (linkes_haus["haustier"] == ""):
                linkes_haus["haustier"] = "Katze"
            elif (check_verbotene_values(rechtes_haus, "haustier", "Katze") == False) and (rechtes_haus["haustier"] == ""):
                rechtes_haus["haustier"] = "Katze"
        


def regel_18(akthä):
# 18) Der Marlboro-Raucher hat einen Nachbarn, der Wasser trinkt
    for haus in akthä:
        if haus["nikotinabusus"] == "Marlboro":
            hausstelle = akthä.index(haus)
            linkes_haus = akthä[hausstelle-1]
            rechtes_haus= akthä[hausstelle+1]
            if (check_verbotene_values(linkes_haus, "getränk", "Wasser") == False) and (linkes_haus["getränk"] == ""):
                linkes_haus["haustier"] = "Wasser"
            elif (check_verbotene_values(rechtes_haus, "getränk", "Wasser") == False) and (rechtes_haus["getränk"] == ""):
                rechtes_haus["haustier"] = "Wasser"

def regel_19(akthä):
# 19) Der Mann, der ein Pferd hält, wohnt neben dem, der Dunhill raucht
    for haus in akthä:
        if haus["nikotinabusus"] == "Dunhill":
            hausstelle = akthä.index(haus)
            linkes_haus = akthä[hausstelle-1]
            rechtes_haus= akthä[hausstelle+1]
            if (check_verbotene_values(linkes_haus, "haustier", "Pferd") == False) and (linkes_haus["haustier"] == ""):
                linkes_haus["haustier"] = "Pferd"
            elif (check_verbotene_values(rechtes_haus, "haustier", "Pferd") == False) and (rechtes_haus["haustier"] == ""):
                rechtes_haus["haustier"] = "Pferd"

def check_verbotene_values(haus, attribut, value):
    return value in haus["verbotene_values"][attribut]

check_Häuser(häuser)
count = 0
while count < 50:
    regel_5(häuser)
    regel_6(häuser)
    regel_7(häuser)
    regel_8(häuser)
    regel_9(häuser)
    regel_10(häuser)
    regel_11(häuser)
    regel_12(häuser)
    regel_13(häuser)
    regel_14(häuser)
    regel_15(häuser)
    regel_16(häuser)
    regel_17(häuser)
    regel_18(häuser)
    regel_19(häuser)
 #   check_Häuser(häuser)

    for haus in häuser:
        verbotene_values = haus["verbotene_values"]
        for key, set in verbotene_values.items():
            if len(set) == 4: # basically heißt dass das nur noch ein möglicher Wert hier geht
                value = Alles[key].difference(set)
                for x in value:
                    haus[key] = x # muss ich so machen weil set item nicht abrufbar ist, aber es ist ja nur eins da
            #    print(haus)
    count += 1
    print(count)
print("Drumroll.......")
check_Häuser(häuser)