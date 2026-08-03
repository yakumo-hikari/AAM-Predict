import streamlit as st
from engine import AAMEngine


st.set_page_config(
    page_title="AAM Predict",
    layout="wide"
)


st.title("🧬 AAM Predict")

st.write(
"""
Adaptive Analytical Model

Public demonstration version for President Tech Award.
"""
)


st.divider()


col1, col2, col3 = st.columns(3)


with col1:
    tsh = st.number_input(
        "TSH",
        value=2.0
    )

with col2:
    t4 = st.number_input(
        "Free T4",
        value=15.0
    )

with col3:
    atpo = st.number_input(
        "Anti-TPO",
        value=10.0
    )


if st.button("Calculate"):

    engine = AAMEngine()

    result = engine.calculate(
        tsh,
        t4,
        atpo
    )

    st.info(
        result["message"]
    )
