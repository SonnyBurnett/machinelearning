import time
import pandas as pd
import datatable as dt
print("pandas version:   ", pd.__version__)
print("datatable version:", dt.__version__)

start = time.time()
dt_df_movies = dt.fread("movies.csv")
end = time.time()
print("datatable in", end - start, "seconds")

start = time.time()
pd_df_movies = pd.read_csv("movies.csv")
end = time.time()
print("pandas in   ", end - start, "seconds")
