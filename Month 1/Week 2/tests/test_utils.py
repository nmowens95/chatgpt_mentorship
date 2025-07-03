from src.datatools import summarize_df
import unittest
import pandas as pd

class TestDF(unittest.TestCase):

    def test_numeric(self):
        df = [[1, 2, 3], ['tom', 'mandy', 'ron'], [77, 109, 26]]
        self.assertIsInstance(df[0][0], int)

    def test_summarizeDF(self):
        df = pd.DataFrame({
            "age": [1, 2, 3], 
            "name": ['tom', 'mandy', 'ron']})
        
        summary = summarize_df(df)
        
        self.assertIn("columns", summary)
        self.assertIsInstance(summary, dict)
        self.assertEqual(len(summary["columns"]), 2)

if __name__ == "__main__":
    unittest.main()