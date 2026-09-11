import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("IPL Data Visualization")

@st.cache_data
def load_data():
    return pd.read_csv("IPL_2008_2026_Merged.csv")

df = load_data()

df["total_runs"] = df["team1_runs"] + df["team2_runs"]

st.sidebar.title("Filters")

seasons = sorted(df["season"].dropna().unique())
selected_season = st.sidebar.selectbox("Select Season", seasons)

filtered_df = df[df["season"] == selected_season]

st.subheader(f"Analysis for Season: {selected_season}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Matches", len(filtered_df))

with col2:
    st.metric("Average Runs", round(filtered_df["total_runs"].mean(), 2))

with col3:
    st.metric("Highest Score", filtered_df["total_runs"].max())

# Bar chart
season_matches = (
    df.groupby("season")
      .size()
      .reset_index(name="matches")
)

st.subheader("Matches by Season")
st.bar_chart(season_matches.set_index("season"))

# Line chart
season_runs = (
    df.groupby("season")["total_runs"]
      .sum()
      .reset_index()
)

st.subheader("Total Runs by Season")
st.line_chart(season_runs.set_index("season"))

# Top winning teams
team_wins = (
    filtered_df["winner"]
      .value_counts()
      .reset_index()
)
team_wins.columns = ["Team", "Wins"]

fig1 = px.bar(
    team_wins.head(10),
    x="Team",
    y="Wins",
    title="Winning Teams"
)
st.plotly_chart(fig1, use_container_width=True)

# Toss decision pie chart
toss_decision = (
    df["toss_decision"]
      .value_counts()
      .reset_index()
)
toss_decision.columns = ["Decision", "Count"]

fig2 = px.pie(
    toss_decision,
    names="Decision",
    values="Count",
    title="Toss Decision Distribution"
)
st.plotly_chart(fig2, use_container_width=True)

# Histogram
fig3 = px.histogram(
    filtered_df,
    x="total_runs",
    nbins=20,
    title="Match Run Distribution"
)
st.plotly_chart(fig3, use_container_width=True)

# Scatter plot
fig4 = px.scatter(
    filtered_df,
    x="team1_runs",
    y="team2_runs",
    title="Team 1 Runs vs Team 2 Runs"
)
st.plotly_chart(fig4, use_container_width=True)

# Matplotlib histogram
st.subheader("Matplotlib: Distribution of Match Runs")
fig5, ax = plt.subplots()
ax.hist(df["total_runs"].dropna(), bins=30)
ax.set_title("Distribution of Match Runs")
ax.set_xlabel("Total Runs")
ax.set_ylabel("Number of Matches")
st.pyplot(fig5)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page("app.py")
