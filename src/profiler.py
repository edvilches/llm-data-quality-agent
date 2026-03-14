import pandas as pd

def profile_dataset(path):

    df = pd.read_csv(path)

    profile = {}

    for col in df.columns:

        profile[col] = {
            "dtype": str(df[col].dtype),
            "missing": int(df[col].isna().sum()),
            "unique_values": int(df[col].nunique()),
            "sample_values": df[col].dropna().unique()[:5].tolist()
        }

    return profile, df
