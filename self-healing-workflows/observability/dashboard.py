import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Self-Healing System", layout="wide")

st.title("🚀 Self-Healing Workflow Dashboard")

# Load logs
with open("observability/logs.json", "r") as f:
    logs = json.load(f)

if len(logs) == 0:
    st.warning("No logs available")
    st.stop()

df = pd.DataFrame(logs)

# ---------------- METRICS ----------------
st.subheader("📊 System Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Events", len(df))
col2.metric("Success", len(df[df["status"] == "SUCCESS"]))
col3.metric("Retries", len(df[df["status"] == "RETRY"]))
col4.metric("Failures", len(df[df["status"].isin(["FAIL","ERROR"])]))

# ---------------- WORKFLOW DISTRIBUTION ----------------
st.subheader("📈 Workflow Activity")

st.bar_chart(df["step"].value_counts())

# ---------------- TIMELINE ----------------
st.subheader("📜 Live Logs")

for log in reversed(logs[-30:]):  # last 30 logs
    if log["status"] == "SUCCESS":
        st.success(f"{log['step']} → {log['details']}")
    elif log["status"] == "RETRY":
        st.warning(f"{log['step']} → {log['details']}")
    elif log["status"] in ["FAIL","ERROR"]:
        st.error(f"{log['step']} → {log['details']}")
    else:
        st.info(f"{log['step']} → {log['details']}")