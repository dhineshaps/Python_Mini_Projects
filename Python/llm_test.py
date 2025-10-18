from gemini_llm import get_ai_portfolio_recommendation
import streamlit as st

total_invested=1000000
total_current_invested_value=1150000
total_invested_stock=500000
total_invested_mf=300000
total_invested_gold=200000
total_current_amount_stock=600000
total_current_amount_mf=350000
total_current_amount_gold=200000

with st.expander("AI Portfolio Recommendation"):
    st.info("This analysis assumes a 10-year investment horizon and is fully AI-curated. Treat the results as a preview for informational purposes only, No Individual Assests are Analyzed , only the portfolio based on allocation")
    with st.form("portfolio_form"):
        risk_profile = st.selectbox(
            "What is your Risk Profile?",
            ("Conservative", "Moderate", "Aggressive"),
            index=1
        )
        goal = st.selectbox(
            "What is your Goal?",
            (
                "Wealth Growth",
                "Retirement Corpus",
                "Buying a Home",
                "Child’s Education",
                "Capital Preservation",
                "Emergency Fund",
                "Financial Independence"
            ),
        )
        submitted = st.form_submit_button("Get AI Report")

        if submitted:
            with st.spinner("Analyzing your portfolio..."):
                response = get_ai_portfolio_recommendation(
                    total_invested,
                    total_current_invested_value,
                    total_invested_stock,
                    total_invested_mf,
                    total_invested_gold,
                    total_current_amount_stock,
                    total_current_amount_mf,
                    total_current_amount_gold,
                    risk_profile,
                    goal
                )

            st.markdown("### 🧭 AI Recommendation")
            st.write(response)