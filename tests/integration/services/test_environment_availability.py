# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import EnvironmentAvailability


class TestEnvironmentAvailability(TestSuite):
    """
    TestBasicMerchant testa a integração da classe de serviço BasicMerchant
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = EnvironmentAvailability(**self.get_config())

    def test_check(self):
        resp = self.service.check()
        self.assertEqual(resp['Status']['Code'], 'OK')
        self.assertEqual(resp['Status']['Message'], 'OK')
