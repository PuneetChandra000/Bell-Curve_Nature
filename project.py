import pandas as pd
import plotly.figure_factory as pf

data = pd.read_csv("project.csv")

Average_Rating = data["Avg Rating"].tolist()

graph = pf.create_distplot([Average_Rating], ["Rating Graph"] , show_hist = False)

graph.show()



