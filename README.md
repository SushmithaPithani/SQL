# SQL
# 🧠 Ask Your Database (Natural Language to SQL)

This project lets you ask questions like **"Show students from GenAI class"**, and it will give you the answer by converting your question into an SQL query using **Google Gemini API**.

Built with:
- 🐍 Python  
- 🌐 Streamlit  
- 🗄️ SQLite  
- 🤖 Google Gemini API

---

## 📌 Features

- Ask questions in **plain English**
- Get **instant answers** from a student database
- Uses **Gemini 1.5 Flash** to convert your question into SQL
- Simple UI using **Streamlit**

---

## 🧾 Example Questions

- How many students are there?  
- Show students in Devops class  
- List students with marks above 80  

---

## 📦 What's in the Database?

Table Name: `STUDENT`

| NAME      | CLASS   | SECTION | MARKS |
|-----------|---------|---------|-------|
| Kishan    | Devops  | A       | 100   |
| Sushmitha | GenAI   | A       | 100   |
| Darius    | GenAI   | A       | 86    |
| Vikash    | Devops  | A       | 50    |
| Dipesh    | Devops  | A       | 35    |

---
## 2. Install the required packages
pip install -r requirements.txt

## 3. Add your Gemini API key
Create a file named .env and add your key:
GOOGLE_API_KEY=your_gemini_api_key_here

## 4. Create the database
Run this command to set up the database:
python sqlite_demo.py

## 5. Start the app
streamlit run app.py




