import streamlit as st

from engine import AAMEngine


st.set_page_config(
    page_title="AAM Predict Demo",
    page_icon="🧬",
    layout="wide"
)


# Header

st.title("🧬 AAM Predict Demo")

st.subheader(
    "Adaptive Analytical Model"
)

st.write(
    """
A research prototype for longitudinal biomarker analysis
and adaptive state assessment.

This public version demonstrates the project concept
and user interface.
"""
)


st.divider()


# Project overview

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Longitudinal Analysis",
        "Enabled"
    )

with col2:
    st.metric(
        "Predictive Framework",
        "Concept"
    )

with col3:
    st.metric(
        "Clinical Support",
        "Prototype"
    )


st.divider()


# Input section

st.header("Biomarker Input")


col1, col2, col3 = st.columns(3)


with col1:
    tsh = st.number_input(
        "TSH",
        min_value=0.0,
        value=2.0
    )


with col2:
    t4 = st.number_input(
        "Free T4",
        min_value=0.0,
        value=15.0
    )


with col3:
    atpo = st.number_input(
        "Anti-TPO",
        min_value=0.0,
        value=10.0
    )


st.divider()


if st.button(
    "Calculate Demo Result",
    type="primary"
):

    engine = AAMEngine()

    result = engine.calculate(
        tsh,
        t4,
        atpo
    )


    st.info(
        result["message"]
    )


    st.subheader(
        "Input Summary"
    )

    st.json(
        result["inputs"]
    )


st.divider()


# Screenshots section

st.header(
    "Project Visualization"
)


st.write(
"""
The full AAM Predict platform includes:
- trajectory visualization;
- compensatory reserve assessment;
- predictive analysis modules.

These components are not included in the public repository.
"""
)
