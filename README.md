# FinMate 💰 - Your Personal Finance & Investment Buddy

<img src="https://github.com/SouravUpadhyay7/FinMate/blob/main/assets/finmate%20webp.jpg?raw=true" width="600"/>


## 📋 Overview
FinMate is a simple yet powerful Streamlit web application that helps users:
- Analyze their personal financial situation
- Get personalized investment advice
- Download a professional PDF financial report

---

## 🏗️ Features

- 📊 **Financial Analysis** based on user inputs
- 💡 **Personalized Investment Suggestions** based on income, family size, city, and savings goal
- 🧾 **PDF Report Generation** with summary & insights
- 🖥️ **Interactive UI** built using Streamlit

---

## 🚀 Tech Stack

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [FPDF](https://pyfpdf.github.io/)
- Markdown & Basic HTML (for formatting)

---

## 📂 Project Structure
finmate/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── config/
│   └── kolkata.json      # City-specific config data
│   └── jharkhand.json
├── utils/
│   └── calculator.py     # Core logic for expense breakdown
│   └── report_generator.py # Generates PDF reports
│   └── investment_advisor.py # SIP & Investment logic
│
├── assets/
│   └── logo.png          # FinMate logo
│
├── reports/              # Auto-generated monthly reports
│
└── README.md


🤝 Contributing
Contributions are welcome!
Please open issues or PRs to improve FinMate 🚀
