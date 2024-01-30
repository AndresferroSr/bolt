import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandasql import sqldf
from pycaret.regression import *

df = pd.read_excel("/workspaces/bolt/bolt/Dataset Task 2.xlsx", sheet_name = "Data")
df.rename(columns={"Created Date": "CreatedDate",
                   "Order State": "OrderState",
                   "Cuisine": "Cuisine",	
                   "Platform": "Platform", 	
                   "Payment Method":"PaymentMethod",	
                   "Card Issuer": "CardIssuer"
                    }, inplace=True)
df["CreatedDate"] = pd.to_datetime(df["CreatedDate"], format = "%d.%m.%Y")
df["ones"] = 1

grouped_df = df.groupby(["CreatedDate", "Country", "City", "OrderState", "Cuisine", "Platform", "PaymentMethod", "CardIssuer"]).agg({"ones": "sum"}).reset_index()

breakpoint()
# Set up the regression problem with PyCaret
regression_setup = setup(
    data=grouped_df,
    target="ones",
    train_size=0.8,
    fold_shuffle=True,
    session_id=42,
)

# Compare and select a regression model
best_model = compare_models()

# Train the selected model
final_model = finalize_model(best_model)

# Predict using the trained model
predictions = predict_model(final_model, data=df)

# Evaluate the model
evaluate_model(final_model)

breakpoint()