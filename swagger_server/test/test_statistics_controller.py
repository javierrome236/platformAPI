# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.models.position import Position  # noqa: E501
from swagger_server.models.statistics import Statistics  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStatisticsController(BaseTestCase):
    """StatisticsController integration test stubs"""

    def test_get_activity_statistics(self):
        """Test case for get_activity_statistics

        Devuelve las estadísticas de actividad de un usuario
        """
        query_string = [('user_id', 56)]
        response = self.client.open(
            '/javierrome/PlatformAPI/1.0.0/statistics',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_live_time_position(self):
        """Test case for get_live_time_position

        Devuelve posición actual del dispositivo
        """
        response = self.client.open(
            '/javierrome/PlatformAPI/1.0.0/statistics/device/liveTime/{deviceId}'.format(device_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_device(self):
        """Test case for post_device

        añade un nuevo dispositivo a la cuenta
        """
        body = Device()
        response = self.client.open(
            '/javierrome/PlatformAPI/1.0.0/statistics/device/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
