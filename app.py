import streamlit as st
from streamlit_lottie import st_lottie
import requests
from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]














def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a relevant Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

st.set_page_config(page_title="SQL Data Retriever", page_icon=":mag:", layout="wide")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Gemini App To Retrieve SQL Data")
        st.write("Enter your question and get SQL data in response.")
        user_input = st.text_area("Input:", height=100, placeholder="Type your question here...")
        if st.button("Ask the question", key="ask_button"):
            # Here you would typically process the input and retrieve data
            st.success("Query processed! (Replace this with actual data retrieval)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

st.markdown("---")
st.markdown("Made with ❤️ by Anjali Joshi")