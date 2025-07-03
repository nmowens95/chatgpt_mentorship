import pandas as pd
from .features import FEATURE_REGISTRY
from .writer import WRITER_REGISTRY
from .logger_config import setup_logger

logger = setup_logger()

def summarize_df(df, file_name, file_type, features=None, writer=None):
    print(f"\nSummary for: {file_name}{file_type}")
    print(f"Number of rows: {len(df)}, Number of columns {len(df.columns)}")

    # Print to Console
    features = features or []
    summary = {}
    for feature in features:
        if feature in FEATURE_REGISTRY:
            result = FEATURE_REGISTRY[feature](df)
            summary[feature] = result # Group by feature

            print(f"--- {feature.upper()} ---")
            for col, value in result.items():
                print(f"{col}: {value}")

    # To output summary
    if writer in WRITER_REGISTRY:
        path = WRITER_REGISTRY[writer](summary, file_name, output_dir="output")
        logger.info(f"Summary written to {path}")
    
    else:
        logger.warning(f"Writer {writer} not recognized. Skipping file output")

    print(f"---- End of Summary ----\n")