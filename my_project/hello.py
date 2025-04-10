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

#* Total Global Sales Grouped By Gaming Systems
sql = "SELECT Platform, SUM(Global_Sales) as Total_Global_Sales FROM sample_csv GROUP BY Platform"
df_platform_sales = query(sql, "sample_csv")

text("# Global Sales Performance From All Gaming Systems")
fig = px.bar(df_platform_sales, x='Platform', y='Total_Global_Sales', title='Total Global Sales by Gaming System Platform')
plotly(fig)

#** Top 10 Best Sellers Globally
sql = "SELECT Name, Global_Sales FROM sample_csv ORDER BY Global_Sales DESC LIMIT 10"
df_top_games = query(sql, "sample_csv")

text("# Top 10 Best Sellers (Globally)")
fig = px.bar(df_top_games, x='Global_Sales', y='Name', orientation='h', title="Top 10 Best Selling Games")
plotly(fig)

#* Regional Sales Breakdown by Platform 
sql = """ 
SELECT Platform, 
    SUM(NA_Sales) as NA_Sales,
    SUM(EU_Sales) as EU_Sales,
    SUM(JP_Sales) as JP_Sales,
    SUM(Other_Sales) as Other_Sales
FROM sample_csv
GROUP BY Platform
"""

text('# Regional Sales Breakdown by Gaming System')
df_region_sales = query(sql, "sample_csv")
fig = px.bar(df_region_sales, x='Platform', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], barmode='stack', title='Regional Sales Breakdown by Gaming Platform')
plotly(fig)

#* Global Sales Distribution by Gaming Genre
sql = "SELECT Genre, SUM(Global_Sales) AS Total_Global_Sales FROM sample_csv GROUP BY Genre"
df_genre_sales = query(sql, "sample_csv")

fig = px.pie(df_genre_sales, names='Genre', values='Total_Global_Sales', title='Global Sales Distribution by Genre')
plotly(fig)

#* Global Sales Per Year
sql = "SELECT Year, SUM(Global_Sales) AS Total_Global_Sales FROM sample_csv GROUP BY Year ORDER BY Year"
df_yearly_sales = query(sql, "sample_csv")

fig = px.line(df_yearly_sales, x='Year', y='Total_Global_Sales', markers=True, title='Total Global Sales per Year')
plotly(fig)


#* NA vs. EU Sale Numbers 
sql = "SELECT NA_Sales, EU_Sales, Platform, Global_Sales FROM sample_csv"
df_sales_scatter = query(sql, "sample_csv")

fig = px.scatter(df_sales_scatter, x='NA_Sales', y='EU_Sales', color='Platform', size='Global_Sales',
                 title='NA vs EU Sales (Colored by Platform)')
plotly(fig)