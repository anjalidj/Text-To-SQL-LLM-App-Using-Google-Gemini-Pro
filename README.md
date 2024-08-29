# Text To SQL LLM App with Google Gemini Pro

## Project Overview
This project implements a Text-to-SQL application using Google's Gemini Pro language model. The app allows users to input natural language queries, which are then converted into SQL queries and executed against a SQL database. The results are displayed in a user-friendly interface created with Streamlit.

## Key Features
- **Natural language to SQL query conversion**
- **Integration with Google Gemini Pro for advanced language understanding**
- **Real-time SQL database querying**
- **User-friendly interface built with Streamlit**

## Technologies Used
- **Python**: The primary programming language used for the application.
- **Anaconda**: Used for environment management and package distribution.
- **Streamlit**: Powers the web-based user interface.
- **SQL Database**: Stores and manages the data (specify which database system you're using, e.g., SQLite, MySQL, etc.).
- **Google Gemini Pro**: The large language model used for natural language processing and SQL query generation.
- **Generative AI**: Employed for converting natural language to SQL queries.

## Setup Instructions

### 1. Set Up Anaconda Environment
```bash
conda create -n text_to_sql_env python=3.8
conda activate text_to_sql_env
```
2. Install Required Packages
```bash
pip install -r requirements.txt
Note: Adjust the package list based on your specific requirements.
```
3. Configure Google Gemini Pro API
Obtain an API key from the Google AI Studio.
Set up your API key as an environment variable:
bash
```bash
export GOOGLE_API_KEY='your-api-key-here'
```

### Project Structure
```bash
text-to-sql-gemini-app/
│
├── app.py                 # Main Streamlit application
├── sql.py                 # Database connection and query execution
├── .env                   # Environment variables (e.g., API keys)
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation (this file)
```
