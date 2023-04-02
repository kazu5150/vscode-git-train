import plotly.express as px


gapminder = px.data.gapminder()

print(gapminder.columns)


animation_fig = px.scatter(
    gapminder,
    x="gdpPercap",
    y="lifeExp",
    log_x=True,
    hover_name="country",
    size="pop",
    size_max=40,
    color="continent",
    animation_frame="year"
)

animation_fig.show()

