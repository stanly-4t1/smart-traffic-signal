import streamlit as st
import random
import time

st.set_page_config(page_title="AI Traffic Signal Controller", layout="wide")

st.title("🚦 AI-Based Smart Traffic Signal Simulation")

# Lane states
directions = ["North", "East", "South", "West"]
vehicle_counts = {d: random.randint(5, 20) for d in directions}

# Simulated emergency vehicle detection
emergency_vehicle = st.sidebar.selectbox("Select Emergency Vehicle Lane (if any)", ["None"] + directions)

# Display vehicle counts
st.subheader("Live Traffic Status (Simulated)")
cols = st.columns(4)
for i, d in enumerate(directions):
    cols[i].metric(label=f"{d} Lane", value=f"{vehicle_counts[d]} vehicles")

# Decision logic function
def decide_next_signal(vehicle_counts, emergency_lane):
    if emergency_lane != "None":
        return emergency_lane
    else:
        sorted_lanes = sorted(vehicle_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_lanes[0][0]

# Simulate sensor clearing
clearing_threshold = st.sidebar.slider("Vehicle clearing threshold", 3, 20, 5)

# Decide next green signal
next_green = decide_next_signal(vehicle_counts, emergency_vehicle)

# Display current signal status
st.markdown("---")
st.header(f"🚦 Current Green Light: {next_green} Lane")
st.markdown(f"### Green light will be ON for {clearing_threshold if vehicle_counts[next_green] <= clearing_threshold else 10} seconds")

progress = st.progress(0)
time.sleep(1)
for i in range(100):
    time.sleep(0.02)
    progress.progress(i + 1)

st.success("Signal cycle complete.")