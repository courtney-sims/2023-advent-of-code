import unittest

import day1


class TestDay1(unittest.TestCase):
    def test_get_calibration_value(self):
        testcases = [
            {"input": "1abc2", "expected": 12},
            {"input": "pqr3stu8vwx", "expected": 38},
            {"input": "a1b2c3d4e5f", "expected": 15},
            {"input": "treb7uchet", "expected": 77},
        ]

        for test in testcases:
            val = day1.get_calibration_value(test["input"])
            self.assertEqual(val, test["expected"])

    def test_process_calibration_document(self):
        val = day1.process_calibration_document("input.txt")
        self.assertEqual(val, 55386)


if __name__ == '__main__':
    unittest.main()
