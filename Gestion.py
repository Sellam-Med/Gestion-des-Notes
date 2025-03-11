import streamlit as st
import pandas as pd

# Titre et logo de l'établissement
st.title("Application de Gestion des Notes")
st.image("C:\\Users\DELL\Downloads\logo.png", width=200)

# Formulaire pour saisir les informations
with st.form("student_form"):
    name = st.text_input("Nom & Prénom")
    module = st.text_input("Module")
    grade = st.number_input("Note finale", min_value=0, max_value=20)
    submit_button = st.form_submit_button("Enregistrer")

    if submit_button:
        # Charger les données existantes ou créer un nouveau DataFrame
        try:
            df = pd.read_csv("grades.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Nom & Prénom", "Module", "Note finale"])

        # Ajouter la nouvelle entrée
        new_entry = pd.DataFrame([[name, module, grade]], columns=["Nom & Prénom", "Module", "Note finale"])
        df = pd.concat([df, new_entry], ignore_index=True)

        # Sauvegarder les données dans un fichier CSV
        df.to_csv("grades.csv", index=False)

# Afficher le tableau des entrées enregistrées
try:
    df = pd.read_csv("grades.csv")
    st.write("### Entrées enregistrées")
    st.dataframe(df)
except FileNotFoundError:
    st.write("Aucune entrée enregistrée pour le moment.")