# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:57:28 2026

@author: ramon
"""

import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Ofentse Ramonnye | Research Profile",
    page_icon="🧪",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Home", "Research Interests", "Projects", "Skills & Tools", "Contact"]
)

# Header
st.title("Ofentse Ramonnye")
st.subheader("Electrochemistry | Sensors | Computational Chemistry")
st.markdown("---")

# Home section
if section == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/480px-No_image_available.svg.png",
            width=220
        )

    with col2:
        st.markdown(
            """
            I am a researcher with interests spanning **electrochemistry**, **sensor development**,
            and **computational chemistry**. My work focuses on understanding electrochemical
            mechanisms, designing functional materials, and using computational tools to interpret
            and predict experimental behavior.
            
            This page showcases my research interests, technical skills, and ongoing projects.
            """
        )

# Research Interests section
elif section == "Research Interests":
    st.header("Research Interests")
    st.markdown(
        """
        - ⚡ **Electrochemistry**: Reaction mechanisms, charge transfer, energy storage materials
        - 🧫 **Electrochemical Sensors**: Chemical and biological sensing, electrode modification
        - 💻 **Computational Chemistry**: DFT calculations, electronic structure analysis, modeling
        - 📊 **Data Analysis**: Interpreting electrochemical and spectroscopic data
        """
    )

# Projects section
elif section == "Projects":
    st.header("Selected Projects")

    st.markdown("**Electrochemical Sensor Development**")
    st.write(
        "Design and characterization of electrochemical sensors for detecting chemical species, "
        "with emphasis on sensitivity, selectivity, and stability."
    )

    st.markdown("**Computational Study of Redox-Active Materials**")
    st.write(
        "Density Functional Theory (DFT) calculations to investigate electronic structures and "
        "redox behavior of electrode materials."
    )

    st.markdown("**Data-Driven Analysis of Electrochemical Systems**")
    st.write(
        "Use of Python-based tools for processing and visualizing electrochemical data."
    )

# Skills & Tools section
elif section == "Skills & Tools":
    st.header("Skills & Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Experimental**")
        st.markdown(
            """
            - Cyclic voltammetry (CV)
            - Galvanostatic charge–discharge (GCD)
            - Electrochemical impedance spectroscopy (EIS)
            - Sensor fabrication and testing
            """
        )

    with col2:
        st.markdown("**Computational & Data**")
        st.markdown(
            """
            - Density Functional Theory (DFT)
            - VASP, Gaussian (basic familiarity)
            - Python (NumPy, Pandas, Matplotlib)
            - Data visualization and analysis
            """
        )

# Contact section
elif section == "Contact":
    st.header("Contact")
    st.markdown(
        """
        📧 **Email**: 4500056@myuwc.ac.za  
        🔗 **https://github.com/4500056-lang/RO-ccsCHPC / https://scholar.google.com/citations?hl=en&user=gw5WE5sAAAAJ&view_op=list_works&gmla=APjjwuYiTyDGX10ygYgi7uGHoLNQEtMFStELGEvWOd2t3XPSV7HCTkDiXJ6dwpoJysNCtFul7-9gsC_Fy8lqrXuj / LinkedIn**: (add links here)
        """
    )

    st.info("This Streamlit app is hosted on Streamlit Cloud as a public research profile page.")