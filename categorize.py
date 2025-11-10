# categorize.py

categories = {
    "food": ["coffee", "tea", "restaurant", "burger", "drink", "pizza", "snack"],
    "transport": ["bus", "taxi", "uber", "fuel", "gas", "train"],
    "shopping": ["clothes", "cosmetics", "boots", "shoes", "bag"],
    "education": ["course", "book", "subscription"],
    "entertainment": ["cinema", "movies", "game"],
}

def categorize_expense(text):
    text = text.lower()

    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            return category.capitalize()

    return "Other"
