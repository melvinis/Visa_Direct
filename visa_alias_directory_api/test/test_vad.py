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
from visa_alias_directory_api.test.base_test import BaseTest

DEBUG = False

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


class TestVAD(BaseTest):

    def setUp(self):
        super(TestVAD, self).setUp()
        self.visa_api_client = VisaAPIClient()
        self.create_alias_request = json.loads('''{
        "guid": "574f4b6a4c2b70472f306f300099515a789092348832455975343637a4e3710",
        "recipientFirstName": "Jamie",
        "recipientMiddleName": "M",
        "recipientLastName": "Bakari",
        "address1": "Street 1",
        "address2": "Region 1",
        "city": "Nairobi",
        "country": "KE",
        "postalCode": "00111",
        "consentDateTime": "2018-03-01 01:02:03",
        "recipientPrimaryAccountNumber": "4005520201264821",
        "issuerName": "Test Bank 1",
        "cardType": "Visa Classic",
        "alias": "254711334999",
        "aliasType": "01"
        }''')
        self.update_alias_request = json.loads('''{
            "guid": "574f4b6a4c2b70472f306f300099515a789092348832455975343637a4e3710",
            "consentDateTime" : "2018-03-01 05:02:03"
            
        }''')
        self.resolve_alias_request = json.loads('''{
        "alias": "254711334999",
        "businessApplicationId": "PP"
}''')
        self.get_alias_request = json.loads('''{
                "guid": "574f4b6a4c2b70472f306f300099515a789092348832455975343637a4e3710"
        }''')
        self.delete_alias_request = json.loads('''{
        "guid": "574f4b6a4c2b70472f306f300099515a789092348832455975343637a4e3710",
        "alias": "254711334999"  
        }''')

    # https://sandbox.api.visa.com/pav/v1/cardvalidation
    def test_vad_scenarios(self):
        base_uri = 'visaaliasdirectory/'
        resource_path_create = 'v1/manage/createalias'
        resource_path_update = 'v1/manage/updatealias'
        resource_path_resolve = 'v1/resolve'
        resource_path_delete = 'v1/manage/deletealias'
        resource_path_get_alias = 'v1/manage/getalias'

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_create,
                                                               self.create_alias_request, 'Create VAD', 'post')
        self.assertEqual(str(response.status_code), "200", "VAD Create failed")

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_update,
                                                               self.update_alias_request, 'Update VAD', 'post')
        self.assertEqual(str(response.status_code), "200", "VAD Update failed")

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_resolve,
                                                               self.resolve_alias_request, 'Resolve VAD', 'post')
        self.assertEqual(str(response.status_code), "200", "VAD Resolved")

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_get_alias,
                                                               self.get_alias_request, 'Get alias information', 'post')
        self.assertEqual(str(response.status_code), "200", "VAD Resolved")

        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path_delete,
                                                               self.delete_alias_request, 'Delete VAD', 'post')

        self.assertEqual(str(response.status_code), "200", "VAD Deleted")

        pass


################################################################

if __name__ == '__main__':
    unittest.main()
    # END