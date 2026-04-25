📚 Neelwafurat Bookstore: Automated Data Pipeline & Market Scraper

🌟 Project Overview
This project is a high-performance Web Scraping and Data Engineering pipeline designed to extract, process, and store book data from Neelwafurat, one of the leading Arabic online bookstores.

Moving beyond simple data collection, this pipeline automates the transition from unstructured web data to a structured SQL database, enabling immediate market analysis, pricing strategy evaluation, and inventory tracking.

🛠️ Tech Stack
Python 3.x: Core logic and automation.

BeautifulSoup4 & Requests: Advanced web scraping with custom headers and rate-limiting.

Pandas: Data cleaning, transformation, and numerical processing.

Regular Expressions (Regex): Precise extraction of pricing data from messy strings.

SQLite: Relational database storage for persistent data management.

🚀 Key Features
Ethical Scraping: Integrated User-Agent rotation and time.sleep delays to respect server limits.

Robust Error Handling: Implemented try-except blocks to ensure the pipeline continues even if specific data points are missing.

Automated Data Cleaning:

Converted localized price strings (e.g., "15.00 ج.م") into searchable numeric formats (float).

Handled missing values by assigning logical defaults or "N/A" tags.

Dual-Format Storage: Saves data simultaneously to a clean CSV for quick Excel viewing and an SQLite Database for professional-grade querying.

📂 Project Structure
Plaintext
neelwafurat-scraper/
├── data/               # Stores generated CSV and SQLite (.db) files
├── src/                # Contains the main engine (scraper.py)
├── .gitignore          # Prevents unnecessary files from being uploaded
├── requirements.txt    # List of all Python libraries needed
└── README.md           # Project documentation
⚙️ Installation & Usage
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/neelwafurat-data-pipeline.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the pipeline:

Bash
python src/scraper.py
📈 Future Roadmap
[ ] Build a Power BI / Tableau Dashboard to visualize pricing trends.

[ ] Implement Automatic Email Alerts when new books from specific publishers are added.

[ ] Deploy the script using GitHub Actions for scheduled weekly scrapes.