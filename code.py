import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv("bell curve project.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],["Sr.No"],show_hist=False)
fig.show()