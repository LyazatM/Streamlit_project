# -*- coding: utf-8 -*-
"""strimlit_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E96EdOKpC3Bke_bLaEsOynMr5Hs7PyF6
"""

!pip install streamlit

import streamlit as st

# app.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")

st.write("Here's our first attempt at using data to create a table:")
data = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(data)

st.write("And here's a line chart:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

