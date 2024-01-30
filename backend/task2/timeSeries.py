import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandasql import sqldf

df = pd.read_excel("/workspaces/bolt/bolt/Dataset Task 2.xlsx", sheet_name = "Data")
df.rename(columns={"Created Date": "CreatedDate"}, inplace=True)
df["CreatedDate"] = pd.to_datetime(df["CreatedDate"], format = "%d.%m.%Y")
df["ones"] = 1

def organice_country(df_temp, country):
    try:
        frame = df_temp[df_temp["Country"] == country]
        frame = frame[["CreatedDate", "ones"]]

        query = """ select CreatedDate, sum(ones) as ones from frame group by 1"""
        frame = sqldf(query)
        frame.set_index('CreatedDate', inplace=True)
        frame.index = pd.to_datetime(frame.index)
        return frame
    except Exception as e:
        print(e)

def analyze_seasonality(country_data, country_name):
    result = seasonal_decompose(country_data, model='multiplicative', extrapolate_trend='freq')
    result.plot()
    plt.suptitle(f'Seasonal Decomposition for {country_name}')
    plt.savefig(f'{country_name}_seasonal_decomposition.png')
    plt.close()

df_portugal = organice_country(df, "Portugal")
df_ghana = organice_country(df, "Ghana")

analyze_seasonality(df_portugal, "Portugal")
analyze_seasonality(df_ghana, "Ghana")
