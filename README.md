# 📚 Neelwafurat Books Pipeline

A high-performance, automated **Data Engineering and Web Scraping pipeline** designed to extract, process, clean, and store structured book data from Neelwafurat, one of the leading Arabic online bookstores.

---

## 🚀 Project Overview

In the data landscape, acquiring clean and well-structured datasets is often the biggest challenge. This project solves that by building an end-to-end Python pipeline that automates data collection from a live e-commerce platform. It transforms unstructured web data into a clean, relational-ready format, making it perfect for downstream data analysis, market research, or business intelligence dashboarding.

## 🛠️ Tech Stack & Tools

* **Core Language:** Python 3.x
* **Web Scraping & Parsing:** BeautifulSoup4, Requests
* **Data Storage:** SQLite (Relational Database)
* **Development Environment:** VS Code / Jupyter Notebooks

## 📌 Key Features

* **Automated Data Extraction:** Efficiently navigates through e-commerce catalog pages to harvest book titles, authors, prices, publishers, and metadata.
* **Robust Data Cleaning Pipeline:** Implements custom Python scripts to handle missing values, eliminate duplicates, and standardize inconsistent text formatting.
* **Structured Storage:** Dynamically maps and inserts parsed data into a locally deployed SQLite database with a optimized schema.
* **Error Handling:** Designed with exception handling to manage connection timeouts and unexpected HTML structure changes gracefully.

## 📁 Database Schema

The pipeline stores data into a structured table named `books` with the following attributes:
* `id` (INTEGER, Primary Key)
* `title` (TEXT) - The title of the book.
* `author` (TEXT) - The author's name.
* `price` (REAL) - Normalized book price.
* `publisher` (TEXT) - Publishing house.
* `category` (TEXT) - Genre/Category.

## ⚙️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mohamed-Aly-Farg/neelwafurat-books-pipeline.git](https://github.com/Mohamed-Aly-Farg/neelwafurat-books-pipeline.git)
   cd neelwafurat-books-pipeline
