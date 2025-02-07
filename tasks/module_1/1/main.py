import psycopg2
import pandas as pd
db_setting = "postgresql://netology:NetoSQL2019@84.201.177.166:19001/world-db"
conn = psycopg2.connect(db_setting)
cur = conn.cursor()
query = "SELECT c.name, c.population FROM public.city c;"
cur.execute(query)
cities = cur.fetchall()
df = pd.DataFrame(cities, columns=['City', 'Population'])
df.head()
vacation_planning = pd.read_csv('vacation_planning.csv')
vacation_planning.head()
merged_df = pd.merge(df, vacation_planning, on='City', how='right')
merged_df.head()
merged_df.describe()
average_population = merged_df.groupby('City')['Population'].mean().reset_index()
average_population.head()

cur.close()
conn.close()



