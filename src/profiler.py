import pandas as pd


def profile_dataset(path):

    df = pd.read_csv(path)

    profile = {}

    for col in df.columns:

        series = df[col]

        profile[col] = {
            "dtype": str(series.dtype),
            "missing": int(series.isna().sum()),
            "missing_pct": float(series.isna().mean()),
            "unique_values": int(series.nunique()),
            "sample_values": series.dropna().astype(str).unique()[:5].tolist()
        }

    return profile, df
