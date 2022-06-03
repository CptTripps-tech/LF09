import unittest
from unittest.mock import patch

from src.host_service import call_api
from src.networkdevice_service import call_api
from src.user_service import get_api


class MyTestCase(unittest.TestCase):

    @patch('src.user_service.requests.get')
    def test_get_user(self, mock_get):
        mock_get.return_value.status_code = 200  # Mock status code of response.
        response = get_api("123")
        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
