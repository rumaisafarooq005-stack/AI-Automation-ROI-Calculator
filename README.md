# AI Automation ROI Calculator

## Project
Client-ready ROI calculator developed for the SafeX Solutions AI & ML Department Week 4 sprint.

## Objective
Estimate the potential time savings, labor-cost savings, annual savings, payback period, and ROI that a small business could achieve by automating repetitive workflows.

## Scenarios
- E-commerce Customer Support
- Email Management
- Customer Service / FAQ
- Custom Business

## Inputs
1. Monthly repetitive tasks/queries
2. Average staff time per task
3. Staff hourly cost
4. Expected automation rate
5. Estimated one-time setup cost

## Main formulas
- Current monthly hours = tasks × minutes per task ÷ 60
- Hours saved = current hours × automation rate
- Monthly savings = hours saved × hourly cost
- Annual savings = monthly savings × 12
- First-year net benefit = annual savings − setup cost
- Payback period = setup cost ÷ monthly savings
- Annual ROI = (annual savings − setup cost) ÷ setup cost × 100

## Run
```bash
pip install streamlit
streamlit run app.py
```

No pandas dependency is required.

## Important
The calculator is an estimation tool, not a guarantee of business results. Actual outcomes should be validated using real operational data.
