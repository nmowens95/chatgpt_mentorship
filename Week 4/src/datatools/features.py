FEATURE_REGISTRY = {}

def register_feature(name):
    def wrapper(func):
        FEATURE_REGISTRY[name] = func
        return func
    return wrapper

@register_feature("dtype")
def dtype_summary(df):
    return {col: str(df[col].dtypes) for col in df.columns}

@register_feature("null")
def null_summary(df):
    return {col: df[col].isna().sum() for col in df.columns}

@register_feature("mode")
def mode_summary(df):
    return {col: df[col].mode()[0] if not df[col].mode().empty else None
        for col in df.columns}


# FEATURE_REGISTRY = {
#     "dtype": dtype_summary,
#     "null": null_summary,
#     "mode": mode_summary
# }