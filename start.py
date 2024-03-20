from taipy.gui import Gui
import pandas as pd


text = "client company"
df= pd.read_csv('current.csv')

page = """
# Elevatoor dashboard

Your space: <|{text}|>

<|{text}|input|>
<|{table}|df.head()|>

"""

Gui(page).run(use_reloader=True)
