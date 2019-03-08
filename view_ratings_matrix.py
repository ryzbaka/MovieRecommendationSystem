import pandas as pd
import numpy as np
import os
import webbrowser

df=pd.read_csv("movie_ratings_data_set.csv")
revised_df=pd.pivot_table(df,index="user_id",columns="movie_id",aggfunc=np.max)
html=revised_df.to_html(na_rep="")

with open("review_matrix.html","w") as f:
    f.write(html)

full_filename=os.path.abspath("review_matrix.html")
webbrowser.open("file://{}".format(full_filename))

