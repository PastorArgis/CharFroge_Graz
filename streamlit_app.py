import streamlit as st
import json
from pathlib import Path

# =====================================
# Default Character
# =====================================

CHARACTER = {
    "name": ["Albert", "m"],
    "class": "Penner",
    "level": 1,
    "hp_current": 10,
    "basevals": {
        "Init": -3,
        "Ges": 10,
        "Resis": 10
    },
    "stats": {
        "STÄ": 10,
        "INT": 9,
        "WIS": 5,
        "GES": 4,
        "KON": 10,
        "CHA": 7
    },
    "multipl": {
        "STÄ": 0,
        "INT": -1,
        "WIS": -2,
        "GES": -3,
        "KON": 0,
        "CHA": -2
    },
    "fates": {
        "STÄ": {
            "Kraft": 2,
            "Überlf": 0
        },
        "INT": {
            "Kreat": 1,
            "Entlarv": -1,
            "Wahrn": -1,
            "Nachfor": -1,
            "Naturk": 1
        },
        "WIS": {
            "Rel": -2,
            "Gesch": -2,
            "Med": -4,
            "Tech": 0,
            "UmgTiere": 0
        },
        "GES": {
            "Akro": -3,
            "Verst": -3,
            "Fingerf": -3
        },
        "CHA": {
            "Überzeug": -2,
            "Täusch": -2,
            "Einschüch": -2,
            "Kunstfert": -2
        },
    },
    "skills": {
        "Klettern": "+2 Kraft",
        "Pisslacke": "acid splash",
        "Zielwasser": "produce flame",
        "Heiliges Feuer": "sacred flame",
        "Eins mit dem Park": "drudecraft",
        "Lallen": "message",
        "Alkfahne": "Konsum: -2 attack roll",
        "Revier markieren": "Konsum: difficult terrain",
        "Feueratem": "note: use D4",
        "Rasche Flucht": "expeditious retreat",
        "Ekelhafter Griff": "arms of Hader"
    },
    "knowledge": {
        "Programmieren": ["Matlab", "Python"],
        "Sprachen": ["D", "E", "IT", "ES"],
        "Dating": ["1: Gegner", "20: Hilfe"],
        "Kälteresistenz": ""
    },
    "status": {
        "inspiration": False,
        "concentrating": False,
        "poisoned": False,
        "blinded": False
    },
    "property": {
        "Ausrüstung": [
            "iphone", "EarPods", "3 USBs", "Kamm", "Schloss",
            "Kondom: ubk. Datum", "Mikrofasertuch", "ÖBB-Karte",
            "3 MTG Decks", "McFit-Karte", "BC-Karte", "Bier",
            "Rucksack", "Jacke", "eCard", "AIDS-Beratungspass"
        ],
        "Material": ["+2 Opiate", "3 Pfandflaschen", "Feuerzeug"],
        "Diverses": ["2 Gaggi-Sacki"],
        "Währung": 423.83
    }
}

SAVE_FILE = Path("character.json")


# =====================================
# Helpers
# =====================================

def load_character():
    if SAVE_FILE.exists():
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(CHARACTER, f, indent=2, ensure_ascii=False)
    return CHARACTER


def list_to_text(items):
    return "\n".join(items)


def text_to_list(text):
    raw_items = []
    for line in text.splitlines():
        raw_items.extend(line.split(","))
    return [item.strip() for item in raw_items if item.strip()]


def save_character():
    data = st.session_state.data

    data["name"][0] = st.session_state.name_input
    data["class"] = st.session_state.class_input
    data["level"] = st.session_state.level_input

    data["fates"]["STÄ"]["Kraft"] = st.session_state.fate_sta_kraft
    data["fates"]["STÄ"]["Überlf"] = st.session_state.fate_sta_ueberlf

    data["fates"]["INT"]["Kreat"] = st.session_state.fate_int_kreat
    data["fates"]["INT"]["Entlarv"] = st.session_state.fate_int_entlarv
    data["fates"]["INT"]["Wahrn"] = st.session_state.fate_int_wahrn
    data["fates"]["INT"]["Nachfor"] = st.session_state.fate_int_nachfor
    data["fates"]["INT"]["Naturk"] = st.session_state.fate_int_naturk

    data["fates"]["WIS"]["Rel"] = st.session_state.fate_wis_rel
    data["fates"]["WIS"]["Gesch"] = st.session_state.fate_wis_gesch
    data["fates"]["WIS"]["Med"] = st.session_state.fate_wis_med
    data["fates"]["WIS"]["Tech"] = st.session_state.fate_wis_tech
    data["fates"]["WIS"]["UmgTiere"] = st.session_state.fate_wis_umgtiere

    data["fates"]["GES"]["Akro"] = st.session_state.fate_ges_akro
    data["fates"]["GES"]["Verst"] = st.session_state.fate_ges_verst
    data["fates"]["GES"]["Fingerf"] = st.session_state.fate_ges_fingerf

    data["fates"]["CHA"]["Überzeug"] = st.session_state.fate_cha_ueberzeug
    data["fates"]["CHA"]["Täusch"] = st.session_state.fate_cha_taeusch
    data["fates"]["CHA"]["Einschüch"] = st.session_state.fate_cha_einschuech
    data["fates"]["CHA"]["Kunstfert"] = st.session_state.fate_cha_kunstfert

    data["basevals"]["Init"] = st.session_state.base_init
    data["basevals"]["Ges"] = st.session_state.base_ges
    data["basevals"]["Resis"] = st.session_state.base_resis

    data["stats"]["STÄ"] = st.session_state.stat_sta
    data["stats"]["INT"] = st.session_state.stat_int
    data["stats"]["WIS"] = st.session_state.stat_wis
    data["stats"]["GES"] = st.session_state.stat_ges
    data["stats"]["KON"] = st.session_state.stat_kon
    data["stats"]["CHA"] = st.session_state.stat_cha

    data["property"]["Ausrüstung"] = text_to_list(st.session_state.prop_ausruestung)
    data["property"]["Material"] = text_to_list(st.session_state.prop_material)
    data["property"]["Diverses"] = text_to_list(st.session_state.prop_diverses)
    data["property"]["Währung"] = st.session_state.prop_waehrung

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# =====================================
# Init
# =====================================

if "data" not in st.session_state:
    st.session_state.data = load_character()

data = st.session_state.data

# property-Felder nur einmal initialisieren
if "prop_ausruestung" not in st.session_state:
    st.session_state.prop_ausruestung = list_to_text(data["property"]["Ausrüstung"])

if "prop_material" not in st.session_state:
    st.session_state.prop_material = list_to_text(data["property"]["Material"])

if "prop_diverses" not in st.session_state:
    st.session_state.prop_diverses = list_to_text(data["property"]["Diverses"])

if "prop_waehrung" not in st.session_state:
    st.session_state.prop_waehrung = float(data["property"]["Währung"])


# =====================================
# UI
# =====================================

st.set_page_config(page_title="DnD Character Sheet", layout="wide")

st.title("DnD Character Sheet")

name = st.text_input(
    "Name",
    value=data["name"][0],
    key="name_input",
    on_change=save_character
)

job = st.text_input(
    "Klasse",
    value=data["class"],
    key="class_input",
    on_change=save_character
)

level = st.number_input(
    "Stufe",
    min_value=1,
    max_value=20,
    value=data["level"],
    key="level_input",
    on_change=save_character
)

if data["name"][1] == "m":
    st.write(f"{name} ist ein Level {level} {job}")
elif data["name"][1] == "w":
    st.write(f"{name} ist eine Level {level} {job}")

col1, col2 = st.columns(2)

with col1:
    st.header("Geschicke")

    st.subheader("Stärke")
    st.number_input("Kraft", -10, 10, data["fates"]["STÄ"]["Kraft"], key="fate_sta_kraft", on_change=save_character)
    st.number_input("Überleben", -10, 10, data["fates"]["STÄ"]["Überlf"], key="fate_sta_ueberlf", on_change=save_character)

    st.subheader("Intelligenz")
    st.number_input("Kreativität", -10, 10, data["fates"]["INT"]["Kreat"], key="fate_int_kreat", on_change=save_character)
    st.number_input("Entlarvung", -10, 10, data["fates"]["INT"]["Entlarv"], key="fate_int_entlarv", on_change=save_character)
    st.number_input("Wahrnehmung", -10, 10, data["fates"]["INT"]["Wahrn"], key="fate_int_wahrn", on_change=save_character)
    st.number_input("Nachforschung", -10, 10, data["fates"]["INT"]["Nachfor"], key="fate_int_nachfor", on_change=save_character)
    st.number_input("Naturkunde", -10, 10, data["fates"]["INT"]["Naturk"], key="fate_int_naturk", on_change=save_character)

    st.subheader("Wissen")
    st.number_input("Religion", -10, 10, data["fates"]["WIS"]["Rel"], key="fate_wis_rel", on_change=save_character)
    st.number_input("Geschichte", -10, 10, data["fates"]["WIS"]["Gesch"], key="fate_wis_gesch", on_change=save_character)
    st.number_input("Medizin", -10, 10, data["fates"]["WIS"]["Med"], key="fate_wis_med", on_change=save_character)
    st.number_input("Technik", -10, 10, data["fates"]["WIS"]["Tech"], key="fate_wis_tech", on_change=save_character)
    st.number_input("Umgang mit Tieren", -10, 10, data["fates"]["WIS"]["UmgTiere"], key="fate_wis_umgtiere", on_change=save_character)

    st.subheader("Geschicklichkeit")
    st.number_input("Akrobatik", -10, 10, data["fates"]["GES"]["Akro"], key="fate_ges_akro", on_change=save_character)
    st.number_input("Verstohlenheit", -10, 10, data["fates"]["GES"]["Verst"], key="fate_ges_verst", on_change=save_character)
    st.number_input("Fingerfertigkeit", -10, 10, data["fates"]["GES"]["Fingerf"], key="fate_ges_fingerf", on_change=save_character)

    st.subheader("Charisma")
    st.number_input("Überzeugungsfähigkeit", -10, 10, data["fates"]["CHA"]["Überzeug"], key="fate_cha_ueberzeug", on_change=save_character)
    st.number_input("Täuschung", -10, 10, data["fates"]["CHA"]["Täusch"], key="fate_cha_taeusch", on_change=save_character)
    st.number_input("Einschüchtern", -10, 10, data["fates"]["CHA"]["Einschüch"], key="fate_cha_einschuech", on_change=save_character)
    st.number_input("Kunstfertigkeit", -10, 10, data["fates"]["CHA"]["Kunstfert"], key="fate_cha_kunstfert", on_change=save_character)

with col2:
    st.header("Grundwerte")
    col21, col22, col23 = st.columns(3)

    with col21:
        st.number_input("Initiative", -10, 100, data["basevals"]["Init"], key="base_init", on_change=save_character)
    with col22:
        st.number_input("Gesundheit", -10, 100, data["basevals"]["Ges"], key="base_ges", on_change=save_character)
    with col23:
        st.number_input("Resistenz", -10, 100, data["basevals"]["Resis"], key="base_resis", on_change=save_character)

    col24, col25 = st.columns(2)

    with col24:
        st.number_input("Stärke", -10, 10, data["stats"]["STÄ"], key="stat_sta", on_change=save_character)
        st.number_input("Wissen", -10, 10, data["stats"]["WIS"], key="stat_wis", on_change=save_character)
        st.number_input("Konstitution", -10, 10, data["stats"]["KON"], key="stat_kon", on_change=save_character)

    with col25:
        st.number_input("Intelligenz", -10, 10, data["stats"]["INT"], key="stat_int", on_change=save_character)
        st.number_input("Geschicklichkeit", -10, 10, data["stats"]["GES"], key="stat_ges", on_change=save_character)
        st.number_input("Charisma", -10, 10, data["stats"]["CHA"], key="stat_cha", on_change=save_character)

    st.header("Fähigkeiten")
    for key, value in data["skills"].items():
        st.markdown(f"**{key}:**  \n{value}")

    st.header("Kenntnisse")
    for key, values in data["knowledge"].items():
        if isinstance(values, list):
            text = ", ".join(values)
        else:
            text = values
        st.markdown(f"**{key}:**  \n{text}")

    st.header("Besitz")

    st.subheader("Ausrüstung")
    st.text_area(
        "Ausrüstung bearbeiten",
        key="prop_ausruestung",
        height=180,
        on_change=save_character
    )

    st.subheader("Material")
    st.text_area(
        "Material bearbeiten",
        key="prop_material",
        height=100,
        on_change=save_character
    )

    st.subheader("Diverses")
    st.text_area(
        "Diverses bearbeiten",
        key="prop_diverses",
        height=80,
        on_change=save_character
    )

    st.subheader("Währung")
    st.number_input(
        "Währung bearbeiten",
        min_value=0.0,
        step=0.01,
        key="prop_waehrung",
        on_change=save_character
    )