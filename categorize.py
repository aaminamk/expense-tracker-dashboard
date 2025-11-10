# categorize.py

categories = {
    "Food": ["coffee", "tea", "restaurant", "burger", "drink", "pizza", "snack"],
    "Transport": ["bus", "taxi", "uber", "fuel", "gas", "train"],
    "Shopping": ["clothes", "cosmetics", "boots", "shoes", "bag"],
    "Education": ["course", "book", "subscription"],
    "Entertainment": ["cinema", "movies", "game"],
}

def categorize_expense(text: str) -> str:
    """Categorizes expense based on keywords."""
    text = text.lower()

    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            return category

    return "Other"
