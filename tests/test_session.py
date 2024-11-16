import unittest
from longship.client import LongshipClient
from longship.session import remote_start_session, remote_stop_session, get_session_id, get_session_status_with_id, filter_sessions


class TestSession(unittest.TestCase):
    client = LongshipClient(base_url='https://api.longship.io', apiKey='WENOOStCJLoVY7iBrmJbMaZK2QN53n2v', ocpKey='2d0b43bda8df4bd9925a42218f81893f', token_group_id='1')

    def test_remote_start_session(self):
        response = remote_start_session(self.client, chargepoint_id='623400302', connector_id=1, id_tag='250783089337')
        self.assertEqual(response, 'Failed')

    def test_get_session_id(self):
        session_id = get_session_id(self.client, chargepoint_id='623400302', connector_number=1, running_only=False)
        self.assertIsInstance(session_id, list)

