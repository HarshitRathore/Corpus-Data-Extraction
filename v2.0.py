import pandas as pd

df = pd.read_csv("data 2018-2019 Close only.csv")

months_dict = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
year_df = pd.to_datetime(df['Date']).dt.year.unique()
year_list = list(set(year_df))
year_value = {}
for year in year_list:
    month_df = pd.to_datetime(pd.to_datetime(df['Date'])[pd.to_datetime(df['Date']).dt.year == year]).dt.month
    month_list = list(set(month_df))
    month_value = {}
    for month in month_list:
        day_df = pd.to_datetime(pd.to_datetime(df['Date'])[pd.to_datetime(df['Date']).dt.month == month]).dt.day
        day_list = list(set(day_df))
        day_value = {}
        for x in day_list:
            value = df[df['Date'] == f"{x}-{months_dict[month-1]}-{year}"]['Close'].item()
            day_value[x] = value
        month_value[month] = day_value
    year_value[year] = month_value
print(year_value)