import pandas as pd
from pandas.core.reshape import tile
import plotly.express as px
import csv

df = pd.read_csv("data.csv")
sp = px.scatter(df, x="date", y="cases", color="country", size="cases", size_max=20, title="Scatter Plot")
sp.show()