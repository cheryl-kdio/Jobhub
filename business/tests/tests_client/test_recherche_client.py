import os
import time

from unittest import TestCase, TextTestRunner, TestLoader, mock
from business.client.offre import Offre


@mock.patch.dict(os.environ, {"HOST_WEBSERVICE": "https://api.adzuna.com/v1/api/"})
class TestOffreClient(TestCase):

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestAttackClient))