import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="CardioInsight Dashboard",
    page_icon="🫀",
    layout="centered"
)

st.title("CardioInsight – Cardiac Variability Analytics Dashboard")
st.caption("Simulated heart rhythm analysis for educational and data visualization purposes")

st.divider()

st.sidebar.header("Controls")

mode = st.sidebar.selectbox(
    "Rhythm Mode",
    ["Normal", "Stress", "Irregular"]
)

beats = st.sidebar.slider(
    "Number of Beats",
    50,
    300,
    120,
    10
)

run = st.sidebar.button("Run Analysis")

def generate_rr(mode, n):
    if mode == "Normal":
        return np.random.normal(0.85, 0.03, n)
    elif mode == "Stress":
        return np.random.normal(0.75, 0.08, n)
    else:
        return np.random.uniform(0.6, 1.2, n)

def analyze(rr):
    mean_rr = np.mean(rr)
    sdnn = np.std(rr)
    rmssd = np.sqrt(np.mean(np.diff(rr) ** 2))

    if sdnn < 0.05:
        label = "Stable rhythm detected"
        color = "green"
    elif sdnn < 0.15:
        label = "Moderate variability detected (stress-like pattern)"
        color = "orange"
    else:
        label = "High variability detected (irregular pattern simulation)"
        color = "red"

    return mean_rr, sdnn, rmssd, label, color

if run:

    rr = generate_rr(mode, beats)
    mean_rr, sdnn, rmssd, label, color = analyze(rr)

    col1, col2, col3 = st.columns(3)

    col1.metric("Mean RR", f"{mean_rr:.3f}")
    col2.metric("SDNN", f"{sdnn:.3f}")
    col3.metric("RMSSD", f"{rmssd:.3f}")

    st.divider()

    st.subheader("Analysis Summary")

    if color == "green":
        st.success(label)
    elif color == "orange":
        st.warning(label)
    else:
        st.error(label)

    st.divider()

    st.subheader("Trend Visualization")

    window = 10
    moving_avg = np.convolve(rr, np.ones(window) / window, mode="valid")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=rr,
        mode="lines",
        name="RR Interval"
    ))

    fig.add_trace(go.Scatter(
        y=moving_avg,
        mode="lines",
        name="Moving Average"
    ))

    fig.update_layout(
        height=450,
        xaxis_title="Beat Number",
        yaxis_title="RR Interval (seconds)"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.caption("Built by Wareesha Khan | CardioInsight Project | Streamlit + Python + Plotly")