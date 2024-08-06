# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:01:54 2024

@author: jperezr
"""

import streamlit as st

st.title('¡Hola, Streamlit!')
st.write('Esta es una aplicación básica de Streamlit.')

if st.button('Di hola'):
    st.write('¡Hola, mundo!')
