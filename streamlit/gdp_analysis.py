import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.set_page_config(layout="wide")

st.write("# GDP Analyis dashboard")

#Download the sample data
data = px.data.gapminder()


st.markdown(
    """
            This is a dashboard showing the *GDP* of Countires:  
            Data source: [Plotly](https://plotly.com/python-api-reference/generated/plotly.express.data.html)
            """
)

col1, col2 = st.columns([5, 5])


# user input
year_col, continent_col, log_x_col = st.columns([5, 5, 5])
with year_col:
    year_choice = st.slider(
        "What year would you like to examine?",
        min_value=1952,
        max_value=2007,
        step=5,
        value=2007,
    )
with continent_col:
    continent_choice = st.selectbox(
        "What continent would you like to look at?",
        ("All", "Asia", "Europe", "Africa", "Americas", "Oceania"),
    )
with log_x_col:
    log_x_choice = st.checkbox("Log X Axis?")

# -- Apply the year filter given by the user
filtered_data = data[(data.year == year_choice)]
# -- Apply the continent filter
if continent_choice != "All":
    filtered_data = filtered_data[filtered_data.continent == continent_choice]

# -- Create the figure in Plotly
fig = px.scatter(
    filtered_data,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="country",
    hover_name="country",
    log_x=log_x_choice,
    size_max=60,
)
fig.update_layout(title="GDP per Capita vs. Life Expectancy")

st.plotly_chart(fig, use_container_width=True)

#================ To compare countries===============
st.subheader("# GDP Per Capita and Population Comparison")
clist = data["country"].unique().tolist()

countries = st.multiselect("Select country", clist)
st.subheader("Selected Countries: {}".format(", ".join(countries)))

datas = {country: data[data["country"] == country] for country in countries}

fig = go.Figure()
fig = make_subplots(rows=1, cols=2)

for country, data in datas.items():
    fig = fig.add_trace(go.Scatter(x=data["year"], y=data["gdpPercap"], name=country), row=1, col=1)
    fig = fig.add_trace(go.Bar(x=data["year"], y=data["pop"], name=country), row=1, col=2)
fig.update_layout(margin=dict(l=50, r=50, t=50, b=50))

st.plotly_chart(fig)


with st.sidebar:
    st.subheader("About")
    st.markdown("This dashboard is made by using **Streamlit**")

st.sidebar.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=30)
