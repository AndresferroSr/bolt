import pandas as pd
from ydata_profiling import ProfileReport


try:
    df = pd.read_excel('Dataset Task 2.xlsx', sheet_name = "Data")
    print(df.shape)
    profile = ProfileReport(df, title="Profiling Report", explorative=True)
    profile.to_file("your_report_task2.html")
except Exception as e:
    print(e)
    breakpoint()