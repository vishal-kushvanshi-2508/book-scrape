# 📚 Book Scrape Using Python

A robust Python web scraping project designed to collect, process, and store book information from an online bookstore. The project follows a modular architecture that separates data collection, extraction, and database operations, making it scalable and easy to maintain.

---

## 📖 Overview

Book Scrape is an automated data extraction project built with Python that scrapes book information from an online bookstore website. The scraper navigates through book listing pages, collects product URLs, extracts detailed information from individual book pages, and stores the data in a structured format for further analysis.

This project demonstrates practical implementation of:

* Web Scraping
* Data Extraction Pipelines
* HTML Parsing
* Database Management
* Data Processing Automation
* Python Project Architecture

---

## 🚀 Key Features

Automated book data collection

Multi-page website scraping

Product URL extraction

Detailed book information extraction

Database integration

Structured data storage

Error handling and data validation

Modular and scalable architecture

---

## 🛠️ Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core Programming Language |
| Requests          | HTTP Requests             |
| BeautifulSoup4    | HTML Parsing              |
| SQLite / Database | Data Storage              |
| JSON              | Data Serialization        |
| Logging           | Monitoring & Debugging    |

---

## 📊 Extracted Data

The scraper can collect:

* Book Title
* Book Price
* Availability Status
* Product Rating
* Category
* Product Description
* Product URL
* Stock Information

---

## 🏗️ Project Architecture

```text
Website
   │
   ▼
Page Collection
   │
   ▼
URL Extraction
   │
   ▼
Database Storage
   │
   ▼
Book Detail Extraction
   │
   ▼
Data Processing
   │
   ▼
Structured Output
```

---

## 📁 Project Structure

```text
book-scrape/
│
├── main.py
├── extract_data.py
├── pages_request_city_data.py
├── store_data_database.py
├── sub_book_database.py
├── sub_book_extract.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Module Description

#### main.py

Project entry point that controls the complete scraping workflow.

#### extract_data.py

Extracts listing page information and generates book URLs.

#### pages_request_city_data.py

Handles HTTP requests and page retrieval operations.

#### store_data_database.py

Creates and manages database tables.

#### sub_book_database.py

Performs database operations for detailed book records.

#### sub_book_extract.py

Extracts detailed information from individual book pages.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vishal-kushvanshi-2508/book-scrape.git
```

### Navigate to Project

```bash
cd book-scrape
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / MacOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Execute the scraper:

```bash
python main.py
```

The workflow will:

1. Create database tables
2. Collect product URLs
3. Store URLs in the database
4. Download book pages
5. Extract book details
6. Save structured information

---

## 📂 Example Output

```json
{
    "title": "A Light in the Attic",
    "price": "£51.77",
    "availability": "In stock",
    "rating": "Three",
    "category": "Poetry",
    "url": "https://books.toscrape.com/catalogue/..."
}
```

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* Web Scraping Fundamentals
* HTTP Request Handling
* BeautifulSoup Data Extraction
* Database Design & Operations
* Data Cleaning & Processing
* Error Handling Strategies
* Python Project Organization
* Real-World Data Collection Workflows

---

## 🔮 Future Improvements

* Multithreaded Scraping
* Async Request Handling
* CSV & Excel Export
* Docker Containerization
* REST API Integration
* Automated Scheduling
* Advanced Logging & Monitoring
* Data Visualization Dashboard

---

#### GitHub Profiles

🔹 Professional Portfolio
https://github.com/vishal-kushvanshi-2508

🔹 Practice Projects & Learning
https://github.com/vishal-2508

