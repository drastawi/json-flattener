import json
import unittest
from json_formatter import flatten_json


class TestFormatter(unittest.TestCase):
    # Should handle all JSON data types
    def test_nesting(self):
        formatted_json = flatten_json(json.loads("""
        {
            "user": {
                "first": "dominik",
                "last": "rastawicki",
                "birthday": {
                    "day": 7,
                    "month": "june"
                }
            },
            "company": "mongodb"
        }
        """))

        self.assertEqual([
            '"user.first": "dominik"',
            '"user.last": "rastawicki"',
            '"user.birthday.day": 7',
            '"user.birthday.month": "june"',
            '"company": "mongodb"'
        ], formatted_json)

    # Should handle all JSON data types
    def test_data_types(self):
        formatted_json = flatten_json(json.loads("""
        {
            "data": {
                "number": 5,
                "null": null,
                "truthfulness": true
            }
        }
        """))

        self.assertEqual([
            '"data.number": 5',
            '"data.null": null',
            '"data.truthfulness": true'
        ], formatted_json)

    # Should throw if an invalid input has been provided.
    def test_input(self):
        formatted_json = flatten_json(json.loads("""
                {
                    "data": [
                        1,
                        2,
                        3
                    ]
                }
                """))


if __name__ == '__main__':
    unittest.main()
