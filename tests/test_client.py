import unittest
from longship.client import LongshipClient


class TestLongshipClient(unittest.TestCase):
    client = LongshipClient(base_url='https://kabisa.longship.io', apiKey='WENOOStCJLoVY7iBrmJbMaZK2QN53n2v', ocpKey='2d0b43bda8df4bd9925a42218f81893f', token_group_id='1')

    def test_client_instance(self):
        self.assertIsInstance(self.client, LongshipClient)


if __name__ == '__main__':
    unittest.main()