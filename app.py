# app.py

import streamlit as st
import pandas as pd
from categorize import categorize_expense  # ✅ Исправленный импорт

st.set_page_config(page_title="Expense Tracker", page_icon="💸")

st.title("💸 Expense Tracker Dashboard")


FILE = "expenses.csv"

# Load or create CSV file
try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Expense", "Amount", "Category"])
    df.to_csv(FILE, index=False)


# Input form
with st.form("expense_form"):
    expense_text = st.text_input("Enter expense (example: `coffee 1200`):")
    submitted = st.form_submit_button("Add expense")

    if submitted:
        try:
            # Split into (text, amount)
            *expense_words, amount = expense_text.split()
            expense_name = " ".join(expense_words)
            amount = float(amount)

            category = categorize_expense(expense_name)

            new_row = pd.DataFrame(
                {"Expense": [expense_name], "Amount": [amount], "Category": [category]}
            )
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(FILE, index=False)

            st.success(f"✅ Added: **{expense_name} — {amount}₸** ({category})")

        except:
            st.error("❌ Format must be: `name amount` (example: `coffee 1200`)")


# Table
st.subheader("📊 Expense Table")
st.dataframe(df)

if not df.empty:
    st.subheader("📈 Spending by Category")
    category_chart = df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_chart)

    st.subheader("💰 Total spending")
    st.write(f"**{df['Amount'].sum()} ₸**")
