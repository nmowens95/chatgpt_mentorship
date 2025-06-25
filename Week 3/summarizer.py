import pandas as pd
from features import FEATURE_REGISTRY

def summarize_df(df, file_name, file_type, features=None):
    print(f"\nSummary for: {file_name}{file_type}")
    print(f"Number of rows: {len(df)}, Number of columns {len(df.columns)}")

    features = features or []
    for feature in features:
        if feature in FEATURE_REGISTRY:
            result = FEATURE_REGISTRY[feature](df)
            print(f"--- {feature.upper()} ---")

            for col, value in result.items():
                print(f"{col}: {value}")

    print(f"---- End of Summary ----\n")