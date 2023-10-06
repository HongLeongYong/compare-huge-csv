import unittest
from unittest.mock import patch, mock_open
import src.count_row as count_row  # 要測試的模組

class TestCsvCountRows(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="data1\ndata2\ndata3\n")
    def test_csv_count_rows(self, mock_file):
        result = count_row.csv_count_rows("some_file.csv")
        self.assertEqual(result, 3)

def __main__():
    unittest.main()