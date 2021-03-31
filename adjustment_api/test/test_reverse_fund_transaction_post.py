# -*- coding: utf-8 -*-

#  **© Copyright 2018 - 2020 Visa. All Rights Reserved.**
#
#  *NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*
#
#  * By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR  CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally  do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims all liability for any such components, including continued availability and functionality. Benefits depend on implementation details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,implementation and resources by you based on your business and operational details. Please refer to the specific API documentation for details on the requirements, eligibility and geographic availability.*#  *This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*
#

# !/usr/bin/python

import datetime
import json
import logging
import os
import sys
import unittest

from adjustment_api.test.base_test import BaseTest
from adjustment_api.helpers.response_recorder import ResponseRecorder
from adjustment_api.helpers.visa_api_client import VisaAPIClient


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


class TestReverseFundsTransfer(BaseTest):

    def setUp(self):
        super(TestReverseFundsTransfer, self).setUp()
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        with open("request_payloads/pull_funds_transaction_request.json", 'r') as file:
            self.push_funds_request = json.load(file)
            self.push_funds_request['localTransactionDateTime'] = date
        if DEBUG: print(date)
        self.visa_api_client = VisaAPIClient()
        self.test_pull_funds_transactions()
        response_context = ResponseRecorder().get_response('pull_funds_transaction_post_response.json')
        request_context = ResponseRecorder().get_response('request_payloads/pull_funds_transaction_request.json')
        business_application_id = request_context['businessApplicationId']
        transaction_identifier = str(response_context['transactionIdentifier'])
        self.reverse_fund_request = json.loads('''{
            "systemsTraceAuditNumber": "101011",
            "retrievalReferenceNumber": "''' + request_context['retrievalReferenceNumber'] + '''",
            "transactionIdentifier": "''' + transaction_identifier + '''",
            "localTransactionDateTime": "''' + date + '''",
            "acquiringBin": "''' + request_context['acquiringBin'] + '''",
            "acquirerCountryCode": "''' + request_context['acquirerCountryCode'] + '''",
            "senderPrimaryAccountNumber" : "''' + request_context['senderPrimaryAccountNumber'] + '''",
            "senderCurrencyCode" : "''' + request_context['senderCurrencyCode'] + '''",
            "amount": "124.02",
            "businessApplicationId": "''' + business_application_id + '''",
            "merchantCategoryCode": "6012",
            "messageReasonCode": 2140,
            "transactionTypeCode": 22
        }''')
        point_of_service_data = json.loads('''{
        "panEntryMode" : "01",
        "posConditionCode" : "00"
        }''')
        self.reverse_fund_request['cardAcceptor'] = request_context['cardAcceptor']
        self.reverse_fund_request['pointOfServiceData'] = point_of_service_data

    def test_pull_funds_transactions(self):
        base_uri = 'visadirect/'
        resource_path = 'fundstransfer/v1/pullfundstransactions'
        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path, self.push_funds_request,
                                                               'Push Funds Transaction Test', 'post')
        ResponseRecorder().record_json_data("pull_funds_transaction_post_response.json",
                                                response.json(encoding='utf-8'))
        self.assertEqual(str(response.status_code), "200", "Pull Funds Transaction test failed")
        pass

    def test_reverse_fund_transaction(self):
        base_uri = 'visadirect/'
        resource_path = 'v1/adjustment'
        self.visa_api_client.do_mutual_auth_request(base_uri + resource_path, self.reverse_fund_request,
                                                               'Push Funds Transaction Test', 'post')
        pass


################################################################

if __name__ == '__main__':
    unittest.main()
    # END
