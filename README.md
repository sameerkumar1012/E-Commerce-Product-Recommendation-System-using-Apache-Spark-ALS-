# E-Commerce Recommendation System (Spark ALS)
🚀 Project Overview

Modern e-commerce platforms rely heavily on personalized recommendations to improve user engagement and sales.
This project builds a Collaborative Filtering (CF) based recommendation model using Spark’s ALS algorithm.

Key Features:

Preprocessing of millions of user–item interaction rows

Creation of implicit ratings from events

ALS model training on a limited dataset (optimized for Colab)

Top-N Recommendations for each user

Exporting recommendations as CSV for dashboards (Tableau, PowerBI)

Evaluation using RMSE

📂 Dataset

Dataset: RetailRocket E-Commerce Dataset
Source: Kaggle (Free)

Contains user events:

view

addtocart

transaction

Each row includes:

visitorid (User ID)

itemid (Product ID)

event (Interaction type)

timestamp

🛠️ Tech Stack

PySpark (Spark 3.5)

Google Colab

Spark MLlib

Python 3

Pandas (optional for exports)
