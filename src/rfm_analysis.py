import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px

def compute_rfm(df: pd.DataFrame, snapshot_date: str = None) -> pd.DataFrame:
    """
    Compute RFM (Recency, Frequency, Monetary) scores for customer segmentation.
    df must have columns: customer_id, order_date, order_value
    """
    df["order_date"] = pd.to_datetime(df["order_date"])
    snapshot = pd.to_datetime(snapshot_date) if snapshot_date else df["order_date"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("customer_id").agg(
        Recency=("order_date", lambda x: (snapshot - x.max()).days),
        Frequency=("order_date", "count"),
        Monetary=("order_value", "sum")
    ).reset_index()

    rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
    rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])
    rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)

    def segment(row):
        r, f = int(row["R_Score"]), int(row["F_Score"])
        if r >= 4 and f >= 4:
            return "Champion"
        elif r >= 3 and f >= 3:
            return "Loyal Customer"
        elif r >= 4 and f <= 2:
            return "New Customer"
        elif r <= 2 and f >= 3:
            return "At Risk"
        else:
            return "Lost"

    rfm["Segment"] = rfm.apply(segment, axis=1)
    return rfm

def plot_segments(rfm: pd.DataFrame):
    fig = px.treemap(rfm, path=["Segment"], values="Monetary",
                     color="Recency", color_continuous_scale="RdYlGn_r",
                     title="Customer Segments by Revenue (RFM Analysis)")
    fig.show()

if __name__ == "__main__":
    np.random.seed(42)
    n = 1000
    sample_data = pd.DataFrame({
        "customer_id": np.random.randint(1, 200, n),
        "order_date": pd.date_range("2022-01-01", periods=n, freq="8H"),
        "order_value": np.random.exponential(scale=150, size=n).round(2)
    })
    rfm = compute_rfm(sample_data)
    print(rfm["Segment"].value_counts())
    plot_segments(rfm)