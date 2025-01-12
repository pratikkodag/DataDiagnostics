import streamlit as st
import plotly.express as px
import pandas as pd

# Fetch data from session state
data = st.session_state.get("data")

if data is not None:
    st.write("### Visualization")
    
    # Maximum 7 Charts
    chart_count = 7
    selected_charts = []
    
    for i in range(chart_count):
        chart_expansion = st.expander(f"Chart {i + 1}", expanded=False)
        with chart_expansion:
            # Chart Type Selection
            chart_type = st.selectbox(f"Choose Chart Type for Chart {i + 1}", 
                                      options=["Bar Chart", "Histogram", "Box Plot", "Scatter Plot", "Line Chart"], 
                                      key=f"chart_type_{i}")
            
            # X-axis and Y-axis Column Selection
            x_col = st.selectbox(f"Select X-axis Column for Chart {i + 1}", options=data.columns, key=f"x_col_{i}")
            y_col = st.selectbox(f"Select Y-axis Column for Chart {i + 1} (Optional for some charts)", 
                                 options=[None] + list(data.columns), key=f"y_col_{i}")
            
            # Add to selected charts
            selected_charts.append((chart_type, x_col, y_col))

    # Function to Validate Axis Selection
    def validate_axis(x, y, chart_type):
        if chart_type == "Bar Chart":
            if pd.api.types.is_categorical_dtype(data[x]) or data[x].nunique() < 20:
                if y is not None and pd.api.types.is_numeric_dtype(data[y]):
                    return True
                else:
                    st.error(f"For a Bar Chart, Y-axis must be numeric.")
            else:
                st.error(f"For a Bar Chart, X-axis must be categorical or have limited unique values.")
        elif chart_type == "Histogram":
            if pd.api.types.is_numeric_dtype(data[x]):
                return True
            else:
                st.error(f"For a Histogram, X-axis must be numeric.")
        elif chart_type == "Box Plot":
            if pd.api.types.is_categorical_dtype(data[x]) and pd.api.types.is_numeric_dtype(data[y]):
                return True
            else:
                st.error(f"For a Box Plot, X-axis must be categorical, and Y-axis must be numeric.")
        elif chart_type == "Scatter Plot":
            if pd.api.types.is_numeric_dtype(data[x]) and pd.api.types.is_numeric_dtype(data[y]):
                return True
            else:
                st.error(f"For a Scatter Plot, both X-axis and Y-axis must be numeric.")
        elif chart_type == "Line Chart":
            if pd.api.types.is_numeric_dtype(data[y]) and (pd.api.types.is_datetime64_any_dtype(data[x]) or pd.api.types.is_numeric_dtype(data[x])):
                return True
            else:
                st.error(f"For a Line Chart, X-axis must be numeric or datetime, and Y-axis must be numeric.")
        return False

    # Validate All Charts First
    st.write("### Validating Charts...")
    valid_charts = []
    for idx, (chart_type, x_col, y_col) in enumerate(selected_charts):
        if validate_axis(x_col, y_col, chart_type):  # Validation happens outside the loop
            valid_charts.append((chart_type, x_col, y_col))

    # Generate and Display Plots Only for Valid Charts
    st.write("### Plotting Charts")
    if valid_charts:
        for idx, (chart_type, x_col, y_col) in enumerate(valid_charts):
            st.write(f"#### Chart {idx + 1}")
            if chart_type == "Bar Chart":
                fig = px.bar(data, x=x_col, y=y_col)
            elif chart_type == "Histogram":
                fig = px.histogram(data, x=x_col)
            elif chart_type == "Box Plot":
                fig = px.box(data, x=x_col, y=y_col)
            elif chart_type == "Scatter Plot":
                fig = px.scatter(data, x=x_col, y=y_col)
            elif chart_type == "Line Chart":
                fig = px.line(data, x=x_col, y=y_col)
            st.plotly_chart(fig)

    # Provide option to download the generated charts as images
    
    if valid_charts:
        for idx, (chart_type, x_col, y_col) in enumerate(valid_charts):
            fig = None
            if chart_type == "Bar Chart":
                fig = px.bar(data, x=x_col, y=y_col)
            elif chart_type == "Histogram":
                fig = px.histogram(data, x=x_col)
            elif chart_type == "Box Plot":
                fig = px.box(data, x=x_col, y=y_col)
            elif chart_type == "Scatter Plot":
                fig = px.scatter(data, x=x_col, y=y_col)
            elif chart_type == "Line Chart":
                fig = px.line(data, x=x_col, y=y_col)

            