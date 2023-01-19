import pandas as pd
import numpy as np
import openpyxl as ox
import streamlit as st

#####################################################
########### Read the file ####################
files = ox.load_workbook("https://github.com/deepaligatade/exceltry/blob/cbcc6634ef1f82e9a3a704cb8ef9d73505564cf2/data/Data.xlsx")
#https://github.com/deepaligatade/exceltry/blob/cbcc6634ef1f82e9a3a704cb8ef9d73505564cf2/data/Data.xlsx
data = files.active
id =st.number_input("ID")
name = st.text_input("Name")
price = st.number_input("price")
order = st.number_input("order quantity")
data.append((id,name,price,order))
save = st.button("Save",1)
if save:
    files.save(".\\data\\Data.xlsx")
    display = st.button("Display",2)
    df = pd.read_excel(".\\data\\Data.xlsx")
    if display:
        
        st.table(df)
    st.write(df)
