import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# -----------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(layout="wide")

# -----------------------------
# LOAD IMAGE
# -----------------------------
image_path = "gyokeres.jpg.webp"

def load_image(path):
    try:
        if os.path.exists(path):
            return Image.open(path)
        return None
    except:
        return None

image = load_image(image_path)


# -----------------------------
# PLAYER HEADER (CLEAN FIFA STYLE)
# -----------------------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image(image, width=180)

with col2:
    st.title("🇸🇪 Viktor Gyökeres")
    st.markdown("### Forward | Box Striker")
    st.markdown("---")

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Goals", "12", "+3")
col2.metric("xG", "11.43", "+0.43")
col3.metric("xA", "2.21", "-0.79")
col4.metric("xG/90", "0.49", "Elite")

st.markdown("---")

# -----------------------------
# ATTRIBUTES (FIFA STYLE)
# -----------------------------
st.markdown("### Player Attributes")

attributes = {
    "Finishing": 88,
    "Positioning": 86,
    "Physical": 90,
    "Aerial Ability": 75,
    "Creativity": 60,
    "Link-up Play": 65
}

for attr, value in attributes.items():
    st.markdown(f"**{attr}**")
    st.progress(value / 100)

st.markdown("---")

# -----------------------------
# DATA (KEEP ONLY WHAT YOU USE)
# -----------------------------
season_df = pd.DataFrame({
    "position": ["FW", "Sub"],
    "apps": [24, 8],
    "min": [1877, 202],
    "goals": [9, 3],
    "xG": [9.94, 1.50],
    "xA": [2.02, 0.19],
    "xG90": [0.48, 0.67],
    "xA90": [0.10, 0.08]
})

zone_df = pd.DataFrame({
    "zone": ["Out of box", "Penalty area", "Six-yard box"],
    "shots": [4, 34, 10],
    "goals": [1, 7, 4],
    "xG": [0.25, 6.59, 4.60]
})

type_df = pd.DataFrame({
    "type": ["Right foot", "Head", "Left foot"],
    "shots": [31, 12, 4],
    "goals": [10, 1, 1],
    "xG": [8.82, 1.89, 0.68]
})

situation_df = pd.DataFrame({
    "situation": ["Open play", "Penalty", "Corner", "Set piece"],
    "shots": [41, 3, 2, 2],
    "goals": [8, 3, 1, 0],
    "xG": [7.94, 2.28, 0.73, 0.48]
})

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
section = st.sidebar.radio("Navigate", [
    "Overview",
    "Shot Zones",
    "Shot Types",
    "Situations",
    "Scouting Summary"
])

# -----------------------------
# OVERVIEW
# -----------------------------
if section == "Overview":

    st.header("Performance Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Goals", season_df["goals"].sum())
    col2.metric("xG", round(season_df["xG"].sum(), 2))
    col3.metric("xA", round(season_df["xA"].sum(), 2))
    col4.metric("Apps", season_df["apps"].sum())

    fig, ax = plt.subplots()
    ax.bar(season_df["position"], season_df["goals"], label="Goals")
    ax.bar(season_df["position"], season_df["xG"], alpha=0.6, label="xG")
    ax.legend()
    st.pyplot(fig)

# -----------------------------
# SHOT ZONES
# -----------------------------
elif section == "Shot Zones":

    st.header("Shot Zone Analysis")

    fig, ax = plt.subplots()
    ax.bar(zone_df["zone"], zone_df["shots"])
    plt.xticks(rotation=20)
    st.pyplot(fig)

    st.dataframe(zone_df)

# -----------------------------
# SHOT TYPES
# -----------------------------
elif section == "Shot Types":

    st.header("Shot Type Breakdown")

    fig, ax = plt.subplots()
    ax.bar(type_df["type"], type_df["goals"])
    plt.xticks(rotation=20)
    st.pyplot(fig)

    st.dataframe(type_df)

# -----------------------------
# SITUATIONS
# -----------------------------
elif section == "Situations":

    st.header("Situation Analysis")

    fig, ax = plt.subplots()
    ax.pie(situation_df["xG"], labels=situation_df["situation"], autopct="%1.1f%%")
    st.pyplot(fig)

    st.dataframe(situation_df)

# -----------------------------
# SCOUTING SUMMARY
# -----------------------------
elif section == "Scouting Summary":

    st.header("Scouting Report")

    st.markdown("""
    ### Player Profile
    - Box-dominant striker  
    - High xG penalty box presence  
    - Strong physical forward profile  

    ### Strengths
    - Elite positioning in the box  
    - High conversion consistency  
    - Strong open-play threat  

    ### Weaknesses
    - Limited creativity (low xA)  
    - Minimal long-range shooting  
    - Low playmaking involvement  
    """)
