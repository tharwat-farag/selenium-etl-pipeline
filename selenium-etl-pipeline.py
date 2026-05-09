import pandas as pd
import requests
import logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from sqlalchemy import create_engine

# =========================
# Logging Setup
# =========================
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# =========================
# Config
# =========================
BOOKS_URL = "https://books.toscrape.com/"
API_URL = "https://dummyjson.com/products"


# =========================
# Step 1: Web Scraping
# =========================
def scrape_data():
    logging.info("Starting web scraping")

    # Chrome Options
    options = webdriver.ChromeOptions()

    # تشغيل المتصفح في الخلفية
    options.add_argument("--headless")

    # تحسين الأداء والثبات
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # تشغيل ChromeDriver تلقائي
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get(BOOKS_URL)

    scraped_data = []

    try:
        # أول 10 كتب
        items = driver.find_elements(By.CLASS_NAME, "product_pod")[:10]

        for item in items:

            title = item.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")

            price = item.find_element(By.CLASS_NAME, "price_color").text

            scraped_data.append([title, price])

        logging.info("Scraping completed successfully")

    except Exception as e:
        logging.error(f"Scraping error: {e}")

    finally:
        driver.quit()

    df_scraped = pd.DataFrame(scraped_data, columns=["title", "price"])

    return df_scraped


# =========================
# Step 2: API Extraction
# =========================
def fetch_api_data():
    logging.info("Fetching API data")

    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()

        product_list = data["products"]

        df_api = pd.DataFrame(product_list)[["title", "price"]]

        logging.info("API data fetched successfully")

        return df_api

    except requests.exceptions.RequestException as e:
        logging.error(f"API error: {e}")

        return pd.DataFrame(columns=["title", "price"])


# =========================
# Step 3: Data Transformation
# =========================
def clean_data(df_scraped, df_api):
    logging.info("Starting data cleaning")

    # تنظيف الأسعار
    df_scraped["price"] = (
        df_scraped["price"].str.replace("£", "", regex=False).astype(float)
    )

    # تحويل نوع البيانات
    df_api["price"] = df_api["price"].astype(float)

    # دمج البيانات
    final_df = pd.concat([df_scraped, df_api], ignore_index=True)

    # تنظيف النصوص
    final_df["title"] = final_df["title"].str.lower().str.strip()

    # حذف التكرارات
    final_df = final_df.drop_duplicates(subset="title")

    # معالجة Null Values
    final_df["price"] = final_df["price"].fillna(0)

    # إضافة Timestamp
    final_df["timestamp"] = datetime.now()

    logging.info("Data cleaning completed")

    return final_df


# =========================
# Step 4: Load Data
# =========================
def save_data(final_df):
    logging.info("Saving data")

    try:
        # Save CSV
        final_df.to_csv("final_data.csv", index=False)

        # Save SQLite
        engine = create_engine("sqlite:///final_data.db")

        final_df.to_sql("products", con=engine, if_exists="replace", index=False)

        logging.info("Data saved successfully")

    except Exception as e:
        logging.error(f"Saving error: {e}")


# =========================
# Main Pipeline
# =========================
def run_pipeline():
    logging.info("Pipeline started")

    print("Starting ETL Pipeline...")

    # Extract
    df_scraped = scrape_data()
    df_api = fetch_api_data()

    # Transform
    final_df = clean_data(df_scraped, df_api)

    # Load
    if final_df.empty:
        logging.warning("Final DataFrame is empty!")
        print("No data found!")

    else:
        save_data(final_df)

        print("\nPipeline finished successfully!\n")

        print(final_df.head())


# =========================
# Run Pipeline
# =========================
if __name__ == "__main__":
    run_pipeline()
