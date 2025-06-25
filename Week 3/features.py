def dtype_summary(df):
    return {col: str(df[col].dtypes) for col in df.columns}

def null_summary(df):
    return {col: df[col].isna().sum() for col in df.columns}

def mode_summary(df):
    return {col: df[col].mode().to_list()[0] if not df[col].mode().empty else None
        for col in df.columns}

FEATURE_REGISTRY = {
    "dtype": dtype_summary,
    "null": null_summary,
    "mode": mode_summary
}