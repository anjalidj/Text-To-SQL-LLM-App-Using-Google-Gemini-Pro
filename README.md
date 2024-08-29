Text To SQL LLM App with Google Gemini Pro
Project Overview
This project implements a Text-to-SQL application using Google's Gemini Pro language model. The app allows users to input natural language queries, which are then converted into SQL queries and executed against a SQL database. The results are displayed in a user-friendly interface created with Streamlit.
Key Features

Natural language to SQL query conversion
Integration with Google Gemini Pro for advanced language understanding
Real-time SQL database querying
User-friendly interface built with Streamlit

Technologies Used

Python: The primary programming language used for the application.
Anaconda: Used for environment management and package distribution.
Streamlit: Powers the web-based user interface.
SQL Database: Stores and manages the data (specify which database system you're using, e.g., SQLite, MySQL, etc.).
Google Gemini Pro: The large language model used for natural language processing and SQL query generation.
Generative AI: Employed for converting natural language to SQL queries.

Setup Instructions


Set Up Anaconda Environment
conda create -n text_to_sql_env python=3.8
conda activate text_to_sql_env

Install Required Packages
pip install -r requirments.txt
Note: Adjust the package list based on your specific requirements.
Configure Google Gemini Pro API

Obtain an API key from the Google AI Studio.
Set up your API key as an environment variable:
Copyexport GOOGLE_API_KEY='your-api-key-here'



Prepare Your Database

Ensure your SQL database is set up and accessible.
Update the database connection details in the application code.



Usage

Start the Streamlit App
Copystreamlit run app.py

Using the Application

Open the provided URL in your web browser.
Enter your query in natural language in the text input field.
Click the "Execute Query" button to process your request.
View the results displayed on the screen.



Project Structure
Copytext-to-sql-gemini-app/
│
├── app.py                 # Main Streamlit application
├── sql.py            # Database connection and query execution
├── .evn              # add key marker duit Google
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation (this file)
