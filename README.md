# CardioInsight Dashboard

An interactive Streamlit-based simulation tool that visualizes cardiac rhythm patterns and explores how heart rate variability (HRV) changes under different conditions.

I built this project after seeing how atrial fibrillation (AFib) affects my dad. It made me more curious about what irregular heart rhythms actually look like in data, and how they can be analyzed in a simple, visual way. This dashboard is my attempt to connect that personal experience with basic cardiac signal analysis! :)

---

## Live App

https://cardioinsight-dashboard.streamlit.app/

---

## Features

- Simulates heart rhythm patterns (Normal, Stress, Irregular)
- Computes HRV metrics (SDNN, RMSSD)
- Interactive Streamlit dashboard
- Plotly-based visualizations

---

## Tech Stack

Python, Streamlit, NumPy, Plotly

---

## How to Run

```bash
pip install -r requirements.txt
python3 -m streamlit run app.py
