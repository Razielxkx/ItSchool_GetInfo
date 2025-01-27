# IT School Application

This project is a web-based platform that interacts with the IT School database and scrapes information about trainers and courses from the IT School website. It provides APIs using FastAPI and a frontend interface built with Streamlit to view and search trainers.

---

## Features

- **Frontend**: Built with Streamlit to allow users to:
  - View all trainers.
  - Search trainers by name.
- **Backend**: Provides APIs for retrieving trainers and courses using FastAPI.
- **Database**: Utilizes SQLAlchemy to interact with a MySQL database storing information on trainers and courses.
- **Web Scraping**: Scrapes trainer and course details directly from the IT School website using BeautifulSoup.

---

## Requirements

- Python 3.9 or later
- MySQL database
- Environment variables for database credentials:
  - `MYSQL_USERNAME`
  - `MYSQL_PASSWORD`

---

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/it-school-app.git
   cd it-school-app
   pip install -r requirements.txt

2. Start the api use the following command:
    ```bash
   uvicorn api:app --port 9125 --reload

3. Start the streamlit server:
    ```bash
    streamlit run main.py