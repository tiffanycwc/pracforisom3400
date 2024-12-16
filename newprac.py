import streamlit as st
st.title('Company Performance Dashboard')
st.header('Executive Summary')
st.subheader('Company Overview')
st.write('Our company focuses on delivering high-quality products to our customers globally, leveraging technology to drive innovation.')
st.text('All figures are updated quarterly.')
st.markdown('**Misson Statement:** Deliver excellence through innovation and customer-centric solutions.')
st.code("
def calculate_growth(revenue_q1, revenue_q2):
            return (revenue_q2 - revenue_q1) / revenue_q1 * 100", language="python")
st.caption("This function calculates quaterly growth base on revenue.")
st.divider()
