# Credit Score Checker (Demo Django App)

A simple **Django web app** that calculates a demo credit score based on user input (age, income, debt, credit utilization, etc.).  
⚠️ **Note:** This is **not a real credit score calculator**. It’s an educational/demo project to learn Django and Azure App Service deployment.

---

## Features
- Django 5.2 project with a single app: `score`
- Form-based input for credit factors
- Demo scoring algorithm → returns a score (300–850) + category (Poor → Exceptional)
- Styled with plain HTML/CSS (no frontend framework)
- Ready for deployment to **Azure App Service (Linux, Free F1 tier)** using a single CLI command
- Uses **WhiteNoise** for static file serving