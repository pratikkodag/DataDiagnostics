import streamlit as st
st.set_page_config(layout="wide")
st.title("🔥 DataDiagnostics")

st.markdown("""
Welcome to **DataDiagnostics**—a powerful tool designed to ensure data quality, perform comprehensive analysis, and generate insightful visualizations. With a focus on data validation and statistical analysis, DataDiagnostics helps you make data-driven decisions with confidence.

Below, we outline the key concepts and techniques employed within this tool.
""", unsafe_allow_html=True)
st.markdown("""
 <span style='color:darkred;'>Data Diagnostics </span>is designed to empower 
users with robust capabilities for data validation, statistical analysis, and visualization. It leverages advanced methodologies to
ensure data integrity and provides insightful visualizations to uncover meaningful patterns and trends. Below, we outline the key 
concepts and techniques employed within this tool.
""", unsafe_allow_html=True)



st.markdown("<h2 style='color:green;'>1️⃣ Data Validation & Analysis</h2>", unsafe_allow_html=True)

st.markdown("""
In the **<span style='color:darkred;'>Data Analysis & Validation</span>** section, we prioritize ensuring the integrity and readiness of your dataset for meaningful insights. This process involves comprehensive data quality assessments, rigorous statistical evaluations, and strategic feature selection to optimize analytical outcomes. Below, we outline the key procedures implemented:

<h3 style='color:teal;'>🛠 A. Data Validation</h3>

- 🔍 <span style='color:red;'>**Missing Value Detection**</span>: 
  Identify and address missing data (NaN values) with options to either impute values (e.g., using mean or median) or remove incomplete rows/columns.

- 🧪 <span style='color:orange;'>**Data Type Validation**</span>: 
  Verify that all columns adhere to expected data types (e.g., numerical or categorical), ensuring consistency and compatibility with analytical methods.

- 🚨 <span style='color:blue;'>**Outlier Detection**</span>: 
  Detect outliers using advanced statistical methods like **Interquartile Range (IQR)** or **Z-Score**. You can choose to retain, adjust, or remove these anomalies.

<h3 style='color:teal;'>📊 B. Statistical Tests</h3>
We employ various statistical methods to validate assumptions and distributions within your dataset:

- 🧪 <span style='color:purple;'>**Normality Test (Shapiro-Wilk Test)**</span>:
  - **H₀ (Null Hypothesis)**: The data follows a normal distribution.
  - **H₁ (Alternative Hypothesis)**: The data does not follow a normal distribution.
  - 👉 Decision Rule: If **<span style='color:orange;'>p-value > 0.05</span>**, the data is considered normally distributed.

- 🚨 <span style='color:purple;'>**Outlier Visualization**</span>:
  - Outliers are visualized through 📦 box plots and 📉 histograms to provide clear insights into their impact on the dataset.

<h3 style='color:teal;'>🏗 C. Feature Selection</h3>
We ensure that only the most impactful features are retained, thereby improving model performance and interpretability:

- ✂️ <span style='color:purple;'>**Variance Threshold**</span>: 
  Eliminate features with minimal variance, as they add negligible value to analysis.

- 🔗 <span style='color:purple;'>**Correlation Analysis**</span>: 
  Detect and remove features exhibiting high correlation (correlation coefficient > 0.9) to mitigate redundancy.
  - Correlations are visually represented using 🔥 heatmaps.


<h3 style='color:green;'>Summary of Data Validation & Analysis:</h3>

- ✅ Address missing data for completeness.

- 🔧 Validate data types for consistency.

- 🧪 Conduct normality tests to confirm statistical assumptions.

- 🚨 Detect and manage outliers for accuracy.

- ✂️ Select relevant features using variance, correlation, and statistical tests.
""", unsafe_allow_html=True)


st.markdown("<h2 style='color:green;'>2️⃣ Data Visualization</h2>", unsafe_allow_html=True)

st.markdown("""
In the <span style='color:darkblue;'>Data Visualization & Charts</span> page, 
you can create various visualizations to uncover insights. Here's what’s included:

<h3 style='color:teal;'>📊 A. Chart Types</h3>

- 📊 <span style='color:purple;'>Bar Charts</span>: Compare frequencies of categories.

- 📈 <span style='color:purple;'>Histograms</span>: Visualize the distribution of numerical data.

- 🔵 <span style='color:purple;'>Scatter Plots</span>: Analyze relationships between two numerical variables.

<h3 style='color:teal;'>🔍 B. Additional Features</h3>

- 📦 <span style='color:purple;'>Box Plots</span>: Summarize data distribution and detect outliers.

- 🔥 <span style='color:purple;'>Heatmaps</span>: Visualize correlations with a color-coded matrix.

<h3 style='color:teal;'>🎛 C. Interactive Visualizations</h3>
Using Plotly, all visualizations are interactive:

- Hover over data points for exact values.

- Zoom in on specific sections of the charts.

<h3 style='color:teal;'>📥 D. Download Options</h3>
After analysis, download:

- The processed data (after handling missing values, outliers, etc.).

- Charts and plots for further use.

<h3 style='color:green;'>Summary of Visualization Methods:</h3>

- 📊 Bar charts for categorical data

- 📈 Histograms for distributions

- 🔵 Scatter plots for relationships

- 🔥 Heatmaps for correlation

- 📥 Downloadable visualizations
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:blue;'>🗝️ Key Concepts Summary</h2>", unsafe_allow_html=True)

st.markdown("""
            
- ✅ <span style='color:purple;'>Data Validation</span>: Ensure data is clean, accurate, and ready for analysis (handle missing values, validate data types, detect outliers).

- 🧪 <span style='color:purple;'>Statistical Tests</span>: Use tests like Shapiro-Wilk and IQR for validation.

- ✂️ <span style='color:purple;'>Feature Selection</span>: Identify key features with correlation analysis, ANOVA, and Chi-Square tests.

- 📊 <span style='color:purple;'>Visualization</span>: Represent data with bar charts, histograms, scatter plots, and heatmaps.

- 📥<span style='color:purple;'>Download Options</span>: Save your processed data and visualizations.

With these concepts in mind, you're ready to move to:
1️⃣ **Page 2** for Data Analysis and Validation.  
2️⃣ **Page 3** for Visualization and Charting.
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:orange;'>🚀 Next Steps</h2>", unsafe_allow_html=True)
st.markdown("""
➡️ Go to <span style='color:green;'>Page 2</span> for data validation, statistical tests, and feature selection.  
➡️ Go to <span style='color:green;'>Page 3</span> to visualize your data with various chart types.
""", unsafe_allow_html=True)
