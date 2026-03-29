import streamlit as st
import json
from pathlib import Path

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

# Character Data .json:

    

CHARACTER = {
    "name": ["Albert", "m"],
    "class": "Penner",
    "level": 1,
    "hp_current": 10,
    "basevals":{
        "Init": -3,
        "Ges": 10,
        "Resis":10},
    "stats":{
        "STÄ": 10,
        "INT": 9,
        "WIS": 5,
        "GES": 4,
        "KON": 10,
        "CHA": 7
    },
    "multipl":{
        "STÄ": 0,
        "INT": -1,
        "WIS": -2,
        "GES": -3,
        "KON": 0,
        "CHA": -2
        },
    "fates":{
        "STÄ":{
            "Kraft": 2,
            "Überlf":0},
        "INT":{
            "Kreat": 1,
            "Entlarv": -1,
            "Wahrn": -1,
            "Nachfor": -1,
            "Naturk": 1},
        "WIS":{
            "Rel": -2,
            "Gesch": -2,
            "Med": -4,
            "Tech": 0,
            "UmgTiere": 0},
        "GES":{
            "Akro": -3,
            "Verst": -3,
            "Fingerf": -3},
        "CHA":{
            "Überzeug": -2,
            "Täusch": -2,
            "Einschüch": -2,
            "Kunstfert": -2},
        },
    "skills":{
        "Klettern": "+2 Kraft",
        "Pisslacke": "acid splash",
        "Zielwasser":"produce flame",
        "Heiliges Feuer": "sacred  flame",
        "Eins mit dem Park": "drudecraft",
        "Lallen":  "message",
        "Alkfahne": "Konsum: -2 attack roll",
        "Revier markieren": "Konsum: difficult terrain",
        "Feueratem": "note: use D4",
        "Rasche Flucht": "expeditious retreat",
        "Ekelhafter Griff": "arms of Hader"
        },
    "knowledge":{
        "Programmieren":["Matlab","Python"],
        "Sprachen":["D","E","IT","ES"],
        "Dating":["1: Gegner", "20: Hilfe"],
        "Kälteresistenz":""
        },
    
    "status": {
        "inspiration": False,
        "concentrating": False,
        "poisoned": False,
        "blinded": False
    },
    "property":{
        "Ausrüstung":[
            "iphone", "EarPods", "$ USBs", "Kamm", "Schloss", 
            "Kondom: ubk. Datum", "Mikrofasertuch", "ÖBB-Karte", 
            "3 MTG Decks", "McFit-Karte", "BC-Karte", "Bier", 
            "Rucksack", "Jacke", "eCard", "AIDS-Beratungspass"
            ],
        "Material": ["+2 Opiate", "3 Pfandflaschen", "Feuerzeug"],
        "Diverses": ["2 Gaggi-Sacki"],
        "Währung": 423.83}
}
# %%



SAVE_FILE = Path("character.json")

def load_character():
    if SAVE_FILE.exists():
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        with open("character.json", "w", encoding="utf-8") as f:
            json.dump(CHARACTER, f, indent=2, ensure_ascii=False)
        return(CHARACTER)

data = load_character()

st.title("DnD Character Sheet")

name = st.text_input("Name", data["name"][0])
job = st.text_input("Klasse", data["class"])
level = st.number_input("Stufe", 1, 20, data["level"])

if data["name"][1] == "m":
    st.write(f"{name} ist ein Level {level} {job}")
if data["name"][1] == "w":
    st.write(f"{name} ist eine Level {level} {job}")

col1, col2= st.columns(2)

with col1:
    st.header("Geschicke")
    st.subheader("**Stärke**")
    st.number_input("Kraft",-10,10, data["fates"]["STÄ"]["Kraft"])
    st.number_input("Kraft",-10,10, data["fates"]["STÄ"]["Überlf"])
    st.subheader("**Intelligenz**")
    st.number_input("Kreativität",-10,10, data["fates"]["INT"]["Kreat"])
    st.number_input("Entlarvung",-10,10, data["fates"]["INT"]["Entlarv"])
    st.number_input("Wahrnehmung",-10,10, data["fates"]["INT"]["Wahrn"])
    st.number_input("Nachforschung",-10,10, data["fates"]["INT"]["Nachfor"])
    st.number_input("Naturkunde",-10,10, data["fates"]["INT"]["Naturk"])
    st.subheader("**Wissen**")
    st.number_input("Religion",-10,10, data["fates"]["WIS"]["Rel"])
    st.number_input("Geschichte",-10,10, data["fates"]["WIS"]["Gesch"])
    st.number_input("Medizin",-10,10, data["fates"]["WIS"]["Med"])
    st.number_input("Technik",-10,10, data["fates"]["WIS"]["Tech"])
    st.number_input("Umgang mit Tieren",-10,10, data["fates"]["WIS"]["UmgTiere"])
    st.subheader("**Geschicklichkeit**")
    st.number_input("Akrobatik",-10,10, data["fates"]["GES"]["Akro"])
    st.number_input("Verstohlenheit",-10,10, data["fates"]["GES"]["Verst"])
    st.number_input("Fingerfertigkeit",-10,10, data["fates"]["GES"]["Fingerf"])
    st.subheader("**Charisma**")
    st.number_input("Überzeugungsfähigkeit",-10,10, data["fates"]["CHA"]["Überzeug"])
    st.number_input("Täuschung",-10,10, data["fates"]["CHA"]["Täusch"])
    st.number_input("Einschüchtern",-10,10, data["fates"]["CHA"]["Einschüch"])
    st.number_input("Kunstfertigkeit",-10,10, data["fates"]["CHA"]["Kunstfert"])
    
    
with col2:
    st.header("Grundwerte")
    col21, col22, col23= st.columns(3)
    
    with col21:
        st.number_input("Initiative",-10,10, data["basevals"]["Init"])
    with col22:
        st.number_input("Gesundheit",-10,10, data["basevals"]["Ges"])
    with col23:
        st.number_input("Resistenz",-10,10, data["basevals"]["Resis"])
    
    col24, col25 = st.columns(2)
    
    with col24:
        st.number_input("Stärke",-10,10, data["stats"]["STÄ"])
        st.number_input("Wissen",-10,10, data["stats"]["WIS"])
        st.number_input("Konstitution",-10,10, data["stats"]["KON"])
    with col25:
        st.number_input("Intelligenz",-10,10, data["stats"]["INT"])
        st.number_input("Geschicklichkeit",-10,10, data["stats"]["GES"])
        st.number_input("Charisma",-10,10, data["stats"]["CHA"])
    
    st.header("Fähigkeiten")
    for key, value in data["skills"].items():
        st.write(f"**{key}:**  \n{value}")

    st.header("Kenntnisse")
    for key, values in data["knowledge"].items():
        st.write(f"**{key}:**  \n{', '.join(values)}")
    
    st.header("Besitz")        
    st.subheader("**Ausrüstung**")
    Ausrüstung = data["property"]["Ausrüstung"]
    st.write(f"{', '.join(Ausrüstung)}")
        
    st.subheader("**Material**")
    Material = data["property"]["Material"]
    st.write(f"{', '.join(Material)}")
        
    st.subheader("**Diverses**")
    Diverses = data["property"]["Diverses"]
    st.write(f"{', '.join(Diverses)}")

    st.subheader("**Währung**")
    st.write(str(data["property"]["Währung"]))