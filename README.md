# Telecom Data Analysis Project

This project focuses on analyzing telecom data stored in a PostgreSQL database. It covers tasks such as user overview analysis, user engagement analysis, and visualization of the insights. The analysis results help derive actionable insights into customer behavior and network performance.

---

## **Directory Structure**

```
project/
│
├── notebooks/                   # Jupyter Notebooks for tasks
│   ├── task1_user_overview.ipynb    # Task 1: User Overview Analysis
│   ├── task2_user_engagement.ipynb  # Task 2: User Engagement Analysis
│
├── scripts/                         # Modular scripts
│   ├── __init__.py
│   ├── database.py                  # Database connection and querying
│   ├── user_overview.py             # Functions for Task 1
│   ├── user_engagement.py           # Functions for Task 2
│   ├── analysis.py                  # Univariate and Bivariate analysis
│   └── utils.py                     # Helper functions (e.g., saving data)
│
├── data/                        # Intermediate data files
│
├── requirements.txt             # Required Python libraries
├── .env                         # Environment variables for database credentials
└── README.md                    # Project documentation
```

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git https://github.com/gtnt-sileshi/TellCo-Telecom-Financial-Data-Analysis
cd TellCo-Telecom-Financial-Data-Analysis
```

### **2. Install Required Libraries**

Use the `requirements.txt` file to install the necessary Python libraries.

```bash
pip install -r requirements.txt
```

### **3. Configure Database Connection**

Create a `.env` file in the project root directory and add your database credentials:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

### **4. Run Jupyter Notebooks**

Start Jupyter Notebook and open the respective tasks:

```bash
jupyter notebook
```

---

## **Usage**

### **Task 1: User Overview Analysis**

This task analyzes the top handsets and manufacturers used by customers.

1. Open `notebooks/task1_user_overview.ipynb`.
2. Run the cells to:
   - Query the top 10 handsets.
   - Analyze the top manufacturers.
   - Visualize the distribution of handsets and manufacturers.

### **Task 2: User Engagement Analysis**

This task explores user engagement metrics and clusters users based on their activity.

1. Open `notebooks/task2_user_engagement.ipynb`.
2. Run the cells to:
   - Query engagement metrics (e.g., session frequency, total duration).
   - Perform univariate and bivariate analysis.
   - Apply clustering to segment users.

---

## **Features**

- **Database Integration**: Uses PostgreSQL to store and query telecom data.
- **Modular Scripts**: Reusable Python modules for data extraction and analysis.
- **Data Visualization**: Visualizations using Matplotlib and Seaborn.
- **Clustering**: K-means clustering for user segmentation.

---

## **Requirements**

- Python 3.8+
- PostgreSQL
- Python libraries:
  - pandas
  - SQLAlchemy
  - psycopg2
  - matplotlib
  - seaborn
  - scikit-learn
  - python-dotenv

---

## **Contributing**

If you wish to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.
