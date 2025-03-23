# utils/calculator.py

def calculate_finance(income, city, housing, vehicle, food, family_size):
    expense_breakdown = {}

    # City-specific multipliers (simplified for now)
    if city == "Kolkata":
        base_rent = 10000 if housing == "Rent" else 0
        transport_cost = 3000 if vehicle == "Public transport" else 5000
        food_cost = 6000 if food == "Order food mostly" else 4000
        misc_factor = 5000  # other costs like entertainment
    elif city == "Jharkhand":
        base_rent = 7000 if housing == "Rent" else 0
        transport_cost = 2000 if vehicle == "Public transport" else 4000
        food_cost = 5000 if food == "Order food mostly" else 3500
        misc_factor = 4000

    # Calculate total expenses
    total_expenses = (base_rent + transport_cost + food_cost + misc_factor) + (family_size * 1000)
    savings = income - total_expenses

    # Suggest SIP (simple rule-based)
    suggested_sip = int(savings * 0.30) if savings > 0 else 0

    expense_breakdown = {
        "City": city,
        "Total Expenses": f"₹{total_expenses}",
        "Estimated Savings": f"₹{savings}",
        "Suggested SIP Investment": f"₹{suggested_sip}",
        "Breakdown": {
            "Rent": base_rent,
            "Transport": transport_cost,
            "Food": food_cost,
            "Family Misc": family_size * 1000,
            "Others": misc_factor
        }
    }
    return expense_breakdown
