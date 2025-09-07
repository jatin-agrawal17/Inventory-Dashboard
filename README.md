
# 📦 Python-MySQL Streamlit Inventory Dashboard
- 🚀 This project demonstrates a **real-world database app** combining **MySQL backend** with a **Streamlit frontend**.
- 📊 Users can **view, update, and analyze inventory and sales data** without writing SQL.
- 🧭 Supports operations like marking orders as received, checking stock, and running business calculations.
- 🎨 Streamlit UI provides **interactive tables, forms, and charts** for a clean and engaging experience.
##  🚀 Features

- View and filter data from tables and views  
- Run stored procedures with a single click (e.g., mark orders as received)  
- Add or update records such as products and prices  
- Perform business calculations with built-in functions  
- See live results without writing SQL
## 📊 Streamlit App Overview

The app consists of **two main sections**:

### 🔹 1. Basic Information
Provides key metrics and reference data to understand the inventory and sales at a glance:

- **Total Suppliers** – Shows the total number of suppliers the system is dealing with  
- **Total Products** – Displays the total number of products available in the inventory  
- **Total Categories Dealing** – Indicates how many product categories are being handled  
- **Total Sale Value** – Represents the cumulative value of all sales  
- **Total Restock Value** – Represents the total cost of restocking inventory  
- **Below Reorder & No Pending Reorders** – Shows the count of products that are below reorder level and have no pending reorders  

**Reference Tables:**
- 📑 **Suppliers Contact Details** – Lists supplier names and contact information  
- 📑 **Products with Supplier and Stock** – Shows products, their suppliers, and current stock levels  
- 📑 **Products Needing Reorder** – Displays products that are below the reorder threshold  

### 🔹 2. Operational Tasks
Enables performing **four key tasks** to manage inventory and orders:

1. **Add Product** – Insert new products into the database  
2. **Product History** – View historical data of product sales and stock  
3. **Place Reorder** – Create a new reorder for products that are low in stock  
4. **Receive an Order** – Mark orders as received, automatically updating stock levels  

#### This design ensures non-technical users can both monitor inventory and perform essential operations easily.
### ⚠️ Important Note on Deployment

Currently, this project **does not host the database in the cloud**. Instead, the **MySQL database and Streamlit app are fully Dockerized**.  

You do **not** need to set up a separate cloud database. Everything will run locally using Docker.  

- The application uses a `.env` file to store sensitive credentials (e.g., database username and password).  
- **The `.env` file is not pushed to GitHub**, which is intentional for security.  
- Anyone running the app via Docker Compose must **create their own `.env` file** with the appropriate credentials to successfully connect to the database.

To run the project:

1. **Clone the repository**
```bash
git clone https://github.com/jatin-agrawal17/Inventory-Dashboard.git
```
2. **Move to Project folder**
```bash
cd Inventory-Dashboard
```
3. **Build and run the application**
```bash
docker-compose up --build
```

## Dependencies
```bash 
pip install -r requirements.txt
```
## 🙌 Acknowledgements

📚 Gained practical experience in **SQL data modeling, stored procedures, functions, and database integration with Python**.  

🖥️ Inspired by real-world **inventory and sales management applications** and best practices in building interactive dashboards for non-technical users.  

🙏 Special thanks to **MySQL** and **Streamlit** for enabling seamless data handling, backend-frontend integration, and interactive UI development.
## 📊 Dataset Used

[Data](https://github.com/jatin-agrawal17/Inventory-Dashboard/tree/main/DATA)
## 📂 Project Structure

📦 Inventory Dashboard  
│  
├── DATA/ ← Folder containing static data or CSV files used in the app  
├── DB/ ← MySQL scripts for creating tables, views, stored procedures, and functions  
├── app.py ← Streamlit application  
├── db_function.py ← Python functions to interact with MySQL  
├── Dockerfile ← Docker setup for the app  
├── docker-compose.yml ← Docker Compose configuration to run both app and database  
├── requirements.txt ← Python dependencies  
├── .gitignore ← Files to be ignored by git  
├── .dockerignore ← Files to be ignored by Docker  
└── README.md ← Project documentation  
## 👤 Author

Jatin Agrawal  
📬 [LinkedIn](https://www.linkedin.com/in/jatin-agrawal-b80092367/)

## 📎 License

This project is open-source and available under the MIT License.
