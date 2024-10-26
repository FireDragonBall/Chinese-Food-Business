import pandas as pd

fooddata = pd.read_csv('mock_chinese_food.csv')
print(fooddata.head())

fooddata.to_excel('fooddata.xlsx')
# food crops
# Chinese wholesale market
# present in USD
# after we get to know the data through google sheet, we have a basic idea about how to clean the data. So we switch to jupyter notebook.

# Exploring Data Analysis

# What are the questions that interest you?

# What question do you think could be helpful with picking up the crop with the most potential in its market?

# The most common Americanlized Chinese dishes are surved with rice. We can do one graph with rice to keep track of one of our main crop's cost.
# We can do one graph with maize to keep track of its cost
# We can do one graph with wheat to keep track of its cost
# We can do one graph with wheat flour to keep of its cost
 # Can we? - Back to EDA from here

# Which city has the most markets, and what does the markets sell overtime?

