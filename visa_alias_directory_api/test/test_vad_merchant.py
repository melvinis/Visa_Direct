# -*- coding: utf-8 -*-

#  **© Copyright 2018 - 2020 Visa. All Rights Reserved.**
# 
#  *NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*
# 
#  * By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR  CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally  do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims all liability for any such components, including continued availability and functionality. Benefits depend on implementation details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,implementation and resources by you based on your business and operational details. Please refer to the specific API documentation for details on the requirements, eligibility and geographic availability.*
# 
#  *This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*
#

# !/usr/bin/python

import json
import logging
import sys
import unittest

from visa_alias_directory_api.helpers.visa_api_client import VisaAPIClient

from visa_alias_directory_api.helpers.response_recorder import ResponseRecorder
from visa_alias_directory_api.test.base_test import BaseTest

DEBUG = True

if DEBUG:

    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

if sys.version_info < (3, 0):
    pass
else:
    pass
'''
@author: visa
'''


class TestVADMerchant(BaseTest):

    def setUp(self):
        super(TestVADMerchant, self).setUp()
        self.visa_api_client = VisaAPIClient()
        self.response_recorder = ResponseRecorder()
        self.create_alias_request = json.loads('''{
        "aliasId": "888111",
        "merchantId": "4123450131001381",
        "merchantCategoryCode": "6012",
        "payloadFormatIndicator": "01",
        "pointOfInitiationMethod": "11",
        "transactionCurrencyCode": "404",
        "recipientName": "Test brand",
        "city": "Nairobi",
        "country": "KE"
}''')
        self.update_alias_request = json.loads('''{
            "aliasId" : "888111",
            "recipientName": "Updated"
        }''')
        self.delete_alias_request = json.loads('''{
        "aliasId": "888111",
        "merchantId": "4123450131001381"
        }''')

    def test_vad_merchant_scenarios(self):
        base_uri = 'visaaliasdirectory/'
        resource_path_create = 'v1/managemerchant/createalias'
        resource_path_delete = 'v1/managemerchant/deletealias'
        resource_path_update = 'v1/managemerchant/updatealias'
        resource_path_get_alias = '/v1/managemerchant?merchantaliasid=888111'

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_create,
                                                               self.create_alias_request, 'Create VAD for merchant',
                                                               'post')
        self.assertEqual(str(response.status_code), "200", "VAD Created for merchant")

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_update,
                                                               self.update_alias_request, 'Update VAD for merchant',
                                                               'post')
        self.assertEqual(str(response.status_code), "200", "VAD Updated for merchant")

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_delete,
                                                               self.delete_alias_request, 'Delete VAD for merchant',
                                                               'post')
        self.assertEqual(str(response.status_code), "200", "VAD Deleted for merchant")

        pass


################################################################

if __name__ == '__main__':
    unittest.main()
    # END
