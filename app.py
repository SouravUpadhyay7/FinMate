# app.py

import streamlit as st
from utils.calculator import calculate_finance
from utils.report_generator import generate_pdf
from utils.investment_advisor import suggest_investments

st.set_page_config(page_title="FinMate", page_icon=":moneybag:", layout="centered")

st.image('assets/finmate webp.jpg', width=150)
st.title("FinMate - Your Personal Finance & Investment Buddy")

# --- Collecting User Inputs ---
st.header("Enter Your Financial Details")

income = st.number_input("Enter your monthly income (₹)", min_value=1000, step=500)

city = st.selectbox("Select your city:", ["Kolkata", "Jharkhand"])

housing = st.selectbox("Do you own or rent your house?", ["Own", "Rent"])
vehicle = st.selectbox("Do you have your own vehicle or use public transport?", ["Own vehicle", "Public transport"])
food = st.selectbox("Do you mostly cook or order food?", ["Cook at home", "Order food mostly"])
family_size = st.number_input("How many family members (including you)?", min_value=1, step=1)

other_expenses = st.text_input("Any additional expenses? (e.g., EMI, healthcare, etc.)")
savings_goal = st.number_input("Enter your savings goal (₹)", min_value=1000, step=500)
goal_purpose = st.text_input("What is the purpose of your savings goal?")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# Add this after calculating results but before generating PDF
if st.button("Calculate Report"):
    results = calculate_finance(income, city, housing, vehicle, food, family_size)
    st.success("Here is your financial analysis:")
    st.json(results)
    
    # Create pie chart visualization
    st.subheader("Expense Breakdown")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Extract expenses from results (adjust these keys according to your actual data structure)
    expense_categories = []
    expense_values = []
    
    # Filter and collect expense data
    for key, value in results.items():
        if 'expense' in key and isinstance(value, (int, float)) and value > 0:
            expense_categories.append(key.replace('_expense', '').replace('_', ' ').title())
            expense_values.append(value)
    
    # Add a fallback if no expense data is found
    if not expense_values:
        expense_categories = ['Sample Category 1', 'Sample Category 2', 'Sample Category 3']
        expense_values = [5000, 3000, 2000]
    
    # Create and display the pie chart
    wedges, texts, autotexts = ax.pie(
        expense_values, 
        autopct='%1.1f%%',
        textprops={'color': "w", 'fontweight': 'bold'},
        shadow=True, 
        startangle=90
    )
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    
    # Add legend
    ax.legend(wedges, expense_categories, title="Expense Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    
    # Display in Streamlit
    st.pyplot(fig)
    
    # Save pie chart to a buffer for later inclusion in PDF
    pie_chart_buffer = BytesIO()
    plt.savefig(pie_chart_buffer, format='png', bbox_inches='tight')
    pie_chart_buffer.seek(0)
    
    # Show Investment Advice Section
    advice = suggest_investments(income, family_size, city, savings_goal, goal_purpose)
    
    st.subheader("💡 Investment Advice:")
    for tip in advice:
        st.write(f"- {tip}")
    
    # Add investment advice to results for PDF generation
    results['investment_advice'] = advice
    
    # Generate the PDF with complete data, passing the pie chart image
    pdf_buffer = generate_pdf(results, pie_chart_buffer)
    
    # Provide the download button directly
    st.download_button(
        label="📥 Download PDF Report",
        data=pdf_buffer,
        file_name="FinMate_Report.pdf",
        mime="application/pdf"
    )

st.caption("FinMate Beta v1.0")
