import unittest
from longship.client import LongshipClient
from longship.chargepoint import get_chargepoint, ChargepointDto, get_chargepoint_status, ChargepointStatusDto, get_all_chargepoints


class TestChargePoint(unittest.TestCase):
    client = LongshipClient(base_url='https://api.longship.io', apiKey='WENOOStCJLoVY7iBrmJbMaZK2QN53n2v', ocpKey='2d0b43bda8df4bd9925a42218f81893f', token_group_id='1')

    def test_get_chargepoint_response_type(self):
        response = get_chargepoint(self.client, chargepoint_id='623400302')
        self.assertIsInstance(response, ChargepointDto)

    def test_get_invalid_chargepoint(self):
        response = get_chargepoint(self.client, chargepoint_id='invalid_id')

    def test_get_valid_chargepoint(self):
        chargpoint = get_chargepoint(self.client, chargepoint_id='623400302')
        self.assertIsInstance(chargpoint, ChargepointDto)

    def test_get_chargepoint_status(self):
        status = get_chargepoint_status(self.client, chargepoint_id='623400302')
        self.assertIsInstance(status, ChargepointStatusDto)


if __name__ == '__main__':
    unittest.main()

