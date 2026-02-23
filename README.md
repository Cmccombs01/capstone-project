# 📊 Sales Analytics & Performance Dashboard
### Analyzing $19k+ in Profit Trends (2020–2023)

https://public.tableau.com/shared/MYJ6MPHSW?:display_count=n&:origin=viz_share_link
<img width="1920" height="932" alt="image" src="https://github.com/user-attachments/assets/3d1ae288-9623-49ac-b18f-f7f749578de7" />


## 📄 Overview
This project analyzes transactional sales data from a fictional retail Superstore to identify drivers of profitability and sales performance. The dataset spans **January 2020 to October 2023**, covering consumer, corporate, and home office segments.

The goal of this analysis was to move beyond raw numbers and provide actionable insights into:
* **Profitability:** Which categories and regions yield the highest margins?
* **Operational Risk:** Identifying volatile sales regions using statistical dispersion.
* **Customer Segmentation:** Understanding buying behaviors across different client types.

## 🛠️ Tools & Skills Used
* **Microsoft Excel:** Advanced Data Cleaning, Pivot Tables, Statistical Functions.
* **Data Analysis:** Time-series forecasting, Outlier detection, KPI calculation.
* **Statistical Metrics:** Correlation analysis, Standard Deviation, Variance.

---

## 🔍 Key Insights & Findings
* **Total Profitability:** The analysis revealed a total net profit of **$19,235.94** across the documented period.
* **Top Performer:** The **Technology** category emerged as the primary driver of revenue and profit.
* **Data Quality:** Identified and corrected inconsistencies in source data (e.g., mislabeled 'Progit Margin' columns) to ensure 100% calculation accuracy.
* **Risk Assessment:** Utilized Standard Deviation and Variance to highlight regions with unstable sales patterns requiring operational review.

---

## 📈 Summary Statistics
A high-level view of performance by category:

| Category | Average Sales | Sum of Profit |
| :--- | :--- | :--- |
| **Technology** | $1,059.67 | $7,054.69 |
| **Office Supplies** | $1,011.36 | $6,205.88 |
| **Furniture** | $996.91 | $5,975.37 |
| **Grand Total** | **$1,021.50** | **$19,235.94** |

---

## 📂 Data Dictionary
The dataset (`Cleaned_Superstore.xlsx`) has been enriched with the following metrics:

### 1. Transaction Information
* **Order ID/Date:** Unique identifiers and timestamps.
* **Segment:** Consumer, Corporate, Home Office.
* **Region:** Central, East, South, West.
* **Category:** Furniture, Office Supplies, Technology.

### 2. Key Performance Indicators (KPIs)
* **Profit Margin:** Calculated as `Profit / Sales`. Represents the efficiency of each transaction.
* **Sales & Quantity:** Total revenue and units sold.
* **Discount:** Percentage deduction applied.

### 3. Statistical Enhancements
To provide immediate context for the distribution of sales data, the following columns were calculated:
* **Central Tendency:** Average Sales, Median Sales.
* **Dispersion:** Standard Deviation, Variance, Range (Max-Min).
* **Correlation Check:** Computed metric to identify relationships between variables.

---

## 🧹 Data Cleaning & Process
Raw data often contains errors. The following steps were taken to prepare the dataset for analysis:
1.  **Date Extraction:** Separated `Order Date` into distinct Year and Month columns for granular time-series analysis.
2.  **Metric Calculation:** Created a `Profit Margin` column to measure order efficiency.
3.  **Statistical Aggregation:** Calculated Mean, Median, and Variance to spot outliers and understand data spread.
4.  **Format Standardization:** Corrected column headers (e.g., fixed 'Progit Margin') and standardized currency/percentage formats.

## 🚀 Potential Use Cases
* **Profitability Analysis:** Determining high-margin products.
* **Forecasting:** Using 2020–2023 trends to predict 2024 performance.
* **Outlier Detection:** Spotting unusual order sizes using Standard Deviation.

🚀 Future Roadmap: AI & Predictive Enhancements
To evolve this project from Descriptive to Prescriptive analytics, the following AI-driven modules are proposed:

1. Automated Outlier Detection (Machine Learning)
Objective: Move beyond manual Standard Deviation checks to identify complex anomalies.

Action: Implement an Isolation Forest model in Python to flag transactions where the relationship between Discount and Profit is mathematically "suspicious," helping to prevent revenue leakage.

2. Time-Series Forecasting (2024 Predictions)
Objective: Predict sales volume for the next two quarters.

Action: Use the Prophet or ARIMA libraries to analyze the $19k+ profit trend from 2020–2023 and generate a baseline forecast for 2024, accounting for seasonal peaks in the Technology category.

3. Customer Segmentation (K-Means Clustering)
Objective: Create more granular personas than the standard "Consumer/Corporate" labels.

Action: Use unsupervised learning to cluster customers based on Frequency of Purchase and Average Profit Margin, allowing for targeted marketing strategies for "High-Value" vs. "Underperforming" accounts.

4. Natural Language Insights (LLM Integration)
Objective: Enable non-technical stakeholders to query the data.

Action: Integrate a GPT-based interface to allow users to ask questions like "Which region had the most volatile profit margins in Q3?" and receive a generated summary based on the Cleaned_Superstore.xlsx data.


---

## 👨‍💻 About Me
I am an aspiring Data Analyst passionate about uncovering the stories hidden within data. With a strong foundation in **Excel**, **SQL**, and **Data Visualization**, I focus on building projects that solve real-world business problems.

Data Analysis: Exploratory Data Analysis (EDA), Time-Series Forecasting, and Statistical Modeling.

Technical Stack: Advanced Excel (Pivot Tables, Statistical Functions), Python (Pandas, Scikit-Learn), and SQL.

Machine Learning: Anomaly Detection (Isolation Forest), Clustering (K-Means), and Predictive Analytics.

Visualization: Tableau Dashboard Design, Data Storytelling, and KPI Reporting.
📫 **Let's Connect:**
* [Portfolio / GitHub](https://github.com/Cmccombs01)
* [LinkedIn Profile](www.linkedin.com/in/caleb-mccombs-850335237)
