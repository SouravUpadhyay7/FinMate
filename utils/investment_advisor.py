# investment_advisor.py

def suggest_investments(income, family_size, city, savings_goal_amount, goal_purpose):
    advice = []

    # General advice based on income
    if income >= 80000:
        advice.append("✅ Allocate at least 20% of your income towards diversified mutual funds or ETFs.")
        advice.append("✅ Consider investing in index funds and explore real estate or REITs if possible.")
    elif 40000 <= income < 80000:
        advice.append("✅ Start with monthly SIPs in mutual funds (e.g., ₹5,000-₹10,000).")
        advice.append("✅ Build an emergency fund covering 6 months of expenses.")
    else:
        advice.append("✅ Focus on savings with PPF, Recurring Deposits, or post-office schemes.")
        advice.append("✅ Look for zero-cost investment options like EPF, NPS, or Sukanya Samriddhi Yojana if applicable.")

    # Family size impact
    if family_size >= 4:
        advice.append("✅ Secure comprehensive health insurance for the entire family.")
        advice.append("✅ Prioritize term life insurance if you have dependents.")

    # City cost impact
    high_cost_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']
    if city in high_cost_cities:
        advice.append("✅ Since you're living in a high-cost city, try to limit non-essential spending.")
        advice.append("✅ Consider side income streams like freelancing or part-time gigs.")

    # Savings goal logic based on purpose
    if goal_purpose.lower() in ['retirement', 'future', 'long-term']:
        advice.append("✅ Consider NPS or long-term mutual funds for wealth building.")
    elif goal_purpose.lower() in ['vacation', 'short-term', 'wedding']:
        advice.append("✅ Opt for short-term debt funds or fixed deposits to preserve capital.")

    # Optional: based on savings_goal_amount
    if savings_goal_amount > 500000:
        advice.append("✅ Since your target is high, explore diversified equity-debt allocation.")

    # Universal advice
    advice.append("✅ Always review and adjust your budget quarterly.")
    advice.append("✅ Track your spending using financial apps or spreadsheets.")

    return advice
