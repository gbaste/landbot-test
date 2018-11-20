# Exec "python3 -m unittest" in parent dir to run tests

from .date import DateUtils

import unittest


class TestDate(unittest.TestCase):

    def test_split(self):
        date = "2018/12/01 07:03:36"
        format_date = "%Y/%m/%d %H:%i:%s"
        expected_separators = ['/', '/', ' ', ':', ':']
        expected_result = ['2018', '12', '01', '07', '03', '36']
        self.assertEqual(DateUtils.split(date, format_date), (expected_result, expected_separators))

        date = "2018-12-01 07:03:36"
        format_date = "%Y-%m-%d %H:%i:%s"
        expected_separators = ['-', '-', ' ', ':', ':']
        expected_result = ['2018', '12', '01', '07', '03', '36']
        self.assertEqual(DateUtils.split(date, format_date), (expected_result, expected_separators))

        date = "2018-12-01 07:03:36"
        format_date = "%Y/%m/%d %H:%i:%s"
        expected_separators = ['-', '-', ' ', ':', ':']
        expected_result = ['2018', '12', '01', '07', '03', '36']
        self.assertNotEqual(DateUtils.split(date, format_date), (expected_result, expected_separators))

        date = "2018/12-01 07:03:36"
        format_date = "%Y/%m/%d %H:%i:%s"
        expected_separators = ['-', '-', ' ', ':', ':']
        expected_result = ['2018', '12', '01', '07', '03', '36']
        self.assertNotEqual(DateUtils.split(date, format_date), (expected_result, expected_separators))

        date = "2018-@month-01 $hour:03:36"
        format_date = "%Y-%m-%d %H:%i:%s"
        expected_separators = ['-', '-', ' ', ':', ':']
        expected_result = ['2018', '@month', '01', '$hour', '03', '36']
        self.assertEqual(DateUtils.split(date, format_date), (expected_result, expected_separators))

        date = "2018-12-01 07:03"
        format_date = "%Y-%m-%d %H:%i:%s"
        expected_separators = ['-', '-', ' ', ':', ':']
        expected_result = ['2018', '12', '01', '07', '03']
        self.assertEqual(DateUtils.split(date, format_date), (expected_result, expected_separators))

if __name__ == '__main__':
    unittest.main()
