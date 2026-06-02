import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PADEL_DIR = BASE_DIR / "PaDEL-Descriptor"

jar_file = PADEL_DIR / "PaDEL-Descriptor.jar"
xml_file = PADEL_DIR / "PubchemFingerprinter.xml"

# Molecular descriptor calculator
def desc_calc():
    
    bashCommand = (
    f"java -Xms512m -Xmx1G "
    f"-Djava.awt.headless=true "
    f"-jar {jar_file} "
    f"-removesalt "
    f"-standardizenitro "
    f"-fingerprints "
    f"-descriptortypes {xml_file} "
    f"-dir . "
    f"-file user_descriptors_output.csv"
    )
    result = subprocess.run(bashCommand.split(), text=True)

    if os.path.exists('molecule.smi'):
        os.remove('molecule.smi')

# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

# Model building
def build_model(input_data):
    # Reads in saved regression model
    model = joblib.load(BASE_DIR/'QSAR_regression.pkl')
    # Apply model to make predictions
    prediction = model.predict(input_data)
    st.header('**Prediction output**')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    prediction_output = pd.Series(prediction, name='pIC50')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

# Logo image
image = Image.open(BASE_DIR/'logo.png')

st.image(image, use_container_width= True)

# Page title
st.markdown("""
# Bioactivity Prediction App (Acetylcholinesterase)

This app allows you to predict the bioactivity towards inhibting the `Acetylcholinesterase` enzyme. `Acetylcholinesterase` is a drug target for Alzheimer's disease.

**Credits**
- App built using `Python` and `Streamlit` 
- Descriptors calculated using [PaDEL-Descriptor : PubChem Fingerprint]
---
""")

# Sidebar
with st.sidebar.header('Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
    st.sidebar.download_button(
        label="Download Example Input File",
        data="example_input.txt",
        file_name="example_input.txt",
        mime="text/plain"
    )

if st.sidebar.button('Predict'):
    if uploaded_file is None:
        st.error("Please, upload a file first")
        st.stop()

    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False)

    st.header('**Original input data**')
    st.write(load_data)

    with st.spinner("Calculating descriptors..."):
        desc_calc()

    # Read in calculated descriptors and display the dataframe
    st.header('**Calculated molecular descriptors**')
    desc = pd.read_csv('user_descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)
    os.remove('user_descriptors_output.csv')

    # Read descriptor list used in previously built model
    st.header('**Subset of descriptors from model used**')
    Xlist = list(pd.read_csv(BASE_DIR/'descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction on query compounds
    build_model(desc_subset)
else:
    st.info('Upload input data in the sidebar to start!')
