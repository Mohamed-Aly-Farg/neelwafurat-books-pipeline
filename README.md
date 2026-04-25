# 📚 Neelwafurat Bookstore: Automated Data Pipeline
> **Automated Web Scraping, Data Cleaning, and SQL Integration.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 🌟 Project Overview
This project is a high-performance **Data Engineering pipeline** designed to extract, process, and store book data from **Neelwafurat**. It automates the transition from **unstructured web data** to a **structured SQL database**, enabling immediate market analysis and pricing strategy evaluation.

---

## 🛠️ Tech Stack & Tools

| Tool | Purpose |
| :--- | :--- |
| **BeautifulSoup4** | Advanced HTML parsing and data extraction. |
| **Requests** | Handling HTTP requests with custom Headers & Delays. |
| **Pandas** | Data cleaning, transformation, and numerical processing. |
| **Regex** | Extracting numeric prices from complex Arabic strings. |
| **SQLite** | Relational database storage for persistent data. |

---

## 🚀 Key Features

* **🛡️ Ethical Scraping:** Integrated `User-Agent` rotation and `time.sleep` to respect server limits.
* **⚠️ Robust Error Handling:** `try-except` blocks to ensure the pipeline survives missing data.
* **🧹 Automated Cleaning:** * Converts price strings (e.g., "15.00 ج.م") into `float` values.
    * Handles missing values with logical "N/A" defaults.
* **💾 Dual Storage:** Saves data as both **CSV** (for Excel) and **SQLite** (for Databases).

---

## 📂 Project Structure

```text
neelwafurat-scraper/
├── data/               # CSV and SQLite (.db) output files
├── src/                # Python engine (scraper.py)
├── .gitignore          # Files to exclude from GitHub
├── requirements.txt    # Library dependencies
└── README.md           # Documentation
---
Bash
python src/scraper.py
