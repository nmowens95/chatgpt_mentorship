def summarize_df(df, file_name, file_type):

    print(f"\nSummary for: {file_name}{file_type}")
    print(f"Number of rows: {len(df)}, Number of columns {len(df.columns)}")

    for col in df.columns:
        print(f"{col} Nulls: {df[col].isna().sum().mean()}, Data type: {df[col].dtype}")
        
    print(f"---- End of Summary ----\n")

