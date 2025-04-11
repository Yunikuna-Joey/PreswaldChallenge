from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px

# text("# Welcome to Preswald!")
# text("This is your first app. 🎉")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('sample_csv')

#* Boilerplate
# # Create a scatter plot
# fig = px.scatter(df, x='NA_Sales', y='EU_Sales', text='Num. of sales',
#                  title='Sales',
#                  labels={'quantity': 'Quantity', 'value': 'Value'})

# # Add labels for each point
# fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# # Style the plot
# fig.update_layout(template='plotly_white')

# # Show the plot
# plotly(fig)

# # Show the data
# table(df)

#* Top 10 Games by Global Sale Numbers
sql = "SELECT Name, Global_Sales FROM sample_csv ORDER BY Global_Sales DESC LIMIT 10"
df_top_games = query(sql, "sample_csv")

text("# Top 10 Best-Selling Games Globally")
fig = px.bar(df_top_games, x='Name', y='Global_Sales', title='Top 10 Games By Global Sales')

plotly(fig)