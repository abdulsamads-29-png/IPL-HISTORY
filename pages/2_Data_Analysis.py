import streamlit as st
import pandas as pd

st.title("IPL Data Analysis")

@st.cache_data
def load_data():
    return pd.read_csv("IPL_2008_2026_Merged.csv")

df = load_data()

# Calculated columns
df["total_runs"] = df["team1_runs"] + df["team2_runs"]
df["total_wickets"] = df["team1_wickets"] + df["team2_wickets"]

st.subheader("Dataset")
st.dataframe(df, use_container_width=True)

st.subheader("Dataset Shape")
rows, columns = df.shape
st.write("Rows:", rows)
st.write("Columns:", columns)

st.subheader("Missing Values")
missing_values = df.isnull().sum()
st.dataframe(missing_values)

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Matches", len(df))

with col2:
    st.metric("Total Seasons", df["season"].nunique())

with col3:
    st.metric("Total Venues", df["venue"].nunique())

with col4:
    st.metric("Cities", df["city"].nunique())

st.subheader("Data Calculations")
average_runs = df["total_runs"].mean()
highest_score = df["total_runs"].max()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Match Runs", round(average_runs, 2))
with col2:
    st.metric("Highest Combined Score", highest_score)
with col3:
    st.metric("Total Wickets", int(df["total_wickets"].sum()))

# Sidebar filters
st.sidebar.title("Filters")

seasons = sorted(df["season"].dropna().unique())
teams = sorted(
    pd.concat([df["team1"], df["team2"]]).dropna().unique()
)

selected_season = st.sidebar.selectbox("Season", seasons)
selected_team = st.sidebar.selectbox("Team", ["All"] + teams)

filtered_df = df[df["season"] == selected_season]

if selected_team != "All":
    filtered_df = filtered_df[
        (filtered_df["team1"] == selected_team) |
        (filtered_df["team2"] == selected_team)
    ]

st.subheader(f"Filtered Data - Season: {selected_season}")
st.dataframe(filtered_df, use_container_width=True)

# Grouping and aggregation
st.subheader("Matches by Season")
matches_by_season = (
    df.groupby("season")
      .size()
      .reset_index(name="matches")
)
st.dataframe(matches_by_season, use_container_width=True)

st.subheader("Wins by Team")
team_wins = (
    df["winner"]
      .value_counts()
      .reset_index()
)
team_wins.columns = ["Team", "Wins"]
st.dataframe(team_wins, use_container_width=True)

st.subheader("Top Winning Teams")
st.dataframe(team_wins.head(10), use_container_width=True)

with st.expander("View Statistical Summary"):
    st.dataframe(df.describe(), use_container_width=True)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page("app.py")
