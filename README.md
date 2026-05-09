# 🚀 Selenium ETL Pipeline

A simple Data Engineering project built with Python that demonstrates an ETL (Extract, Transform, Load) workflow using Web Scraping, API Integration, Data Cleaning, and SQLite storage.

---

## 📌 Project Overview

This project collects product data from two different sources:

- 🌐 Web Scraping using Selenium
- 🔗 API Data Extraction using Requests

Then the data is:
- Cleaned and transformed with Pandas
- Stored in CSV format
- Loaded into a SQLite database

---

## ⚙️ Technologies Used

- Python
- Selenium
- Pandas
- Requests
- SQLAlchemy
- SQLite
- WebDriver Manager

---

## 🔄 ETL Pipeline Flow

### 1️⃣ Extract
- Scrape books data from:
  https://books.toscrape.com/
- Fetch products data from:
  https://dummyjson.com/products

### 2️⃣ Transform
- Clean prices
- Convert data types
- Remove duplicates
- Handle missing values
- Standardize text
- Add timestamps

### 3️⃣ Load
- Save cleaned data into:
  - `final_data.csv`
  - `final_data.db`

---

## 📂 Project Structure

```bash
selenium-etl-pipeline/
│
├── selenium-etl-pipeline.py
├── requirements.txt
├── README.md
├── final_data.csv
├── final_data.db
└── pipeline.log
```

---

## ▶️ Run The Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the pipeline

```bash
python selenium-etl-pipeline.py
```

---

## 📊 Example Output

```text
Pipeline finished successfully!
```

Generated files:
- final_data.csv
- final_data.db
- pipeline.log

---

## 💡 Features

✔ Automated Web Scraping  
✔ API Integration  
✔ Data Cleaning & Transformation  
✔ CSV Export  
✔ SQLite Database Loading  
✔ Logging System  
✔ ETL Workflow Implementation  

---

## 🎯 Learning Objectives

This project demonstrates:
- ETL Pipeline concepts
- Web Scraping automation
- API handling
- Data transformation using Pandas
- Database loading with SQLAlchemy
- Logging and automation

---

## 👨‍💻 Author

**Tharwat Farag**

- GitHub:
  https://github.com/tharwat-farag

---

## 📎 Repository

https://github.com/tharwat-farag/selenium-etl-pipeline

---

#DataEngineering #Python #ETL #WebScraping #Selenium #Digilians
