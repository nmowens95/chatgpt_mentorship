import unittest
import pandas as pd
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "./src")))
from src.datatools import summarize_df

class TestSummarize(unittest.TestCase):


    def test_nulls(self):
        df = pd.DataFrame({
            "age": [77, 109, 26], 
            "name": ['tom', 'mandy', 'ron']   
            })
        null_count = df.isnull().sum()
        self.assertEqual(null_count.sum(), 0)
        self.assertEqual(df.isnull().sum().sum(), 0) # These two are the same


    def test_datatype(self):
        df = pd.DataFrame({
            "age": [77, 109, 26], 
            "name": ['tom', 'mandy', 'ron']   
            })
        
        summary = summarize_df(df)

        self.assertIsInstance(summary, dict)
        self.assertIsNotNone(summary["columns"])
        self.assertIsInstance(summary["columns"][0], dict)

        for col_summary in summary["columns"]:
            self.assertIn("name", col_summary)
            self.assertIn("dtype", col_summary)

    
    def test_nullHandling(self):
        df = pd.DataFrame({
            "age": [77, 109, 26, None, 88, 64], 
            "name": ['tom', 'mandy', None, "kylie", None, 'ron']   
            })
        
        summary = summarize_df(df)

        self.assertGreater(summary["columns"][0]["isna"], 10)

if __name__ == "__main__":
    unittest.main()