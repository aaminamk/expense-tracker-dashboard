# app.py

import streamlit as st
import pandas as pd
from categorize.py import categorize_expense

st.title("💸 Expense Tracker Dashboard")

# CSV file to store expenses
FILE = "expenses.csv"

# If file does not exist, create an empty one
try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Expense", "Amount", "Category"])
    df.to_csv(FILE, index=False)

# Input form
with st.form("expense_form"):
    expense_text = st.text_input("Enter expense (e.g., 'coffee 1200')")
    submitted = st.form_submit_button("Add")

    if submitted:
        try:
            *expense, amount = expense_text.rsplit(" ", 1)
            expense_name = " ".join(expense)
            amount = float(amount)

            category = categorize_expense(expense_name)

            new_row = pd.DataFrame({"Expense": [expense_name], "Amount": [amount], "Category": [category]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(FILE, index=False)

            st.success(f"Added: {expense_name} — {amount}₸ ({category})")

        except ValueError:
            st.error("Format must be: name + space + amount (example: coffee 1200)")

st.subheader("📊 Expense Table")
st.dataframe(df)

if not df.empty:
    st.subheader("📈 Spending by Category")
    chart = df.groupby("Category")["Amount"].sum()
    st.bar_chart(chart)

    st.subheader("💰 Total Spending")
    st.write(f"**{df['Amount'].sum()} ₸**")
