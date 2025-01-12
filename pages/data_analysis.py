import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.feature_selection import VarianceThreshold

# Streamlit App Title
st.title("Data Validation and Analysis")

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file:
    # Read the uploaded file
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)

    # Display Dataset Preview
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    # Data Validation Section
    st.write("### Data Validation")

    # Check for Missing Values
    if data.isnull().sum().any():
        st.warning("There are missing values in the dataset!")
        st.write(data.isnull().sum())
    else:
        st.success("No missing values in the dataset.")

    # Display Data Types
    st.write("### Data Types")
    st.write(data.dtypes)

    # Convert potential date columns to datetime
    for column in data.select_dtypes(include=["object"]).columns:
        if "date" in column.lower():
            data[column] = pd.to_datetime(data[column], errors="coerce")
            st.write(f"Column '{column}' converted to datetime.")

    # Normality Test: Shapiro-Wilk Test
    st.write("### Normality Test (Shapiro-Wilk Test)")
    for column in data.select_dtypes(include=[np.number]).columns:
        stat, p_value = stats.shapiro(data[column].dropna())
        st.write(f"Column '{column}': Shapiro-Wilk Test p-value = {p_value}")
        if p_value < 0.05:
            st.warning(f"Column '{column}' is *not normally distributed*. (p < 0.05)")
        else:
            st.success(f"Column '{column}' is *normally distributed*. (p ≥ 0.05)")

    # Outlier Detection: Using IQR (Interquartile Range)
    st.write("### Outlier Detection (IQR Method)")
    for column in data.select_dtypes(include=[np.number]).columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]

        if not outliers.empty:
            st.warning(f"Outliers detected in column '{column}':")
            st.write(outliers)
        else:
            st.success(f"No outliers detected in column '{column}'.")

    # Descriptive Statistics
    st.write("### Descriptive Statistics (Mean, Median, Mode, Variance, Std Dev, Min, Max)")

    # Create a DataFrame for statistics
    stats_df = pd.DataFrame(columns=["Mean", "Median", "Mode", "Variance", "Std Dev", "Min", "Max"])
    for column in data.select_dtypes(include=[np.number]).columns:
        stats_df.loc[column] = [
            data[column].mean(),
            data[column].median(),
            data[column].mode()[0],
            data[column].var(),
            data[column].std(),
            data[column].min(),
            data[column].max(),
        ]

    # Display descriptive statistics
    st.dataframe(stats_df)

    # **Variance Threshold for Feature Selection**
    st.write("### Variance Threshold (Feature Selection)")

    # User input for threshold
    threshold = st.slider("Select Variance Threshold", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    
    # Apply Variance Threshold
    selector = VarianceThreshold(threshold=threshold)
    selected_features = selector.fit_transform(data.select_dtypes(include=[np.number]))

    st.write(f"Number of features before variance threshold: {data.select_dtypes(include=[np.number]).shape[1]}")
    st.write(f"Number of features after variance threshold: {selected_features.shape[1]}")
    
    if selected_features.shape[1] == 0:
        st.warning("No features left after applying the variance threshold!")
    else:
        st.success("Features selected successfully based on the variance threshold.")

    # **Correlation Analysis**
    st.write("### Correlation Analysis (Heatmap)")

    # Calculate the correlation matrix
    corr_matrix = data.select_dtypes(include=[np.number]).corr()

    # Display correlation matrix as a heatmap
    st.write("Correlation matrix for numeric features:")
    st.dataframe(corr_matrix)

    # Visualize the correlation matrix
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    st.pyplot(plt)

    # Provide option to download the processed data
    st.write("### Download Processed Data")

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode("utf-8")

    csv = convert_df(data)
    st.download_button(
        label="Download Processed Data (CSV)", data=csv, file_name="processed_data.csv", mime="text/csv"
    )

    # Proceed to the next page for visualization if no missing values
    if data.isnull().sum().any():
        st.warning("Please fix the missing values before proceeding.")
    else:
        if st.button("Proceed to Visualization"):
            st.session_state.data = data
            st.write("Redirecting to Visualization Page...")
