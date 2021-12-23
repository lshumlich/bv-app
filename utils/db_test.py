#
# pytest utils/db_test.py -s -k add
#
import unittest
from utils.db import DB


class TestData(unittest.TestCase):
    """ Sample of a test suite

    This tests our simple API to ensure the results are proper
    """

    def test_stuff(self):
        print("Running TestData, not a good idea to put print statements in tests.")

    def test_get_cities(self):
        db = DB()
        cities = db.select("SELECT * FROM public.canadacities")
        # {'city': 'Oyen', 'city_ascii': 'Oyen', 'province_id': 'AB', 'province_name': 'Alberta', 'lat': '51.3522', 'lng': '-110.4739', 'population': 1001, 'density': Decimal('189.6'), 'timezone': 'America/Edmonton', 'ranking': 3, 'postal': 'T0J', 'id': '1124000494'}
        print(db.result)
