import logging
import json
import os

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO,
)

logger = logging.getLogger()

def save_df(filetype, summary, save):
    if save:
        dir_path = os.path.dirname(save)
        if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
        
        if filetype == "json":
        # Write to file
            logger.info(f"Writing summary to {save}")
            with open(save, "a") as f:
                json.dump(summary, f)

        else:
            logger.info(f"Writing summary to {save}")
            with open(save, "a") as f:
                for col in summary["columns"]:
                    f.write(f"Column name: {col['name']}\n")
                    f.write(f"Column dtype: {col['dtype']}\n")
                    f.write(f"Percent missing: {col['null']}\n")
                    f.write(f"Column mode: {col['mode']}\n")
                    # f.write(f"Column most frequent: {col['most_frequent']}\n")

                    f.write("---------------------------------------------\n")
    else:
        logger.INFO("File successfully summarized") 