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

import logging
import sys
import unittest
import json
import datetime

from mobile_push_payment_refund_api.helpers.visa_api_client import VisaAPIClient
from mobile_push_payment_refund_api.test.base_test import BaseTest

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


class TestRefundsAPI(BaseTest):

    def setUp(self):
        super(TestRefundsAPI, self).setUp()
        self.visa_api_client = VisaAPIClient()
        self.date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def test_mVisa_refund_api_post(self):
        response = self.perform_merchandise_return()
        self.assertEqual(str(response.status_code), "200", "M Visa Refund API")
        pass

    def test_mVisa_refund_api_get(self):
        base_uri = 'visadirect/'
        resource_path = 'mvisa/v1/mr/'
        timeout_response = self.perform_merchandise_return(True)
        status_identifier = timeout_response.content.decode();
        get_refund_response = self.visa_api_client.do_mutual_auth_request(
            base_uri + resource_path + status_identifier,
            None,
            'Refund Get',
            'get')
        response_code = get_refund_response.status_code
        self.assertTrue(response_code >= 200 and response_code <= 299,
                        "Refund Get test failed")


    def test_mvisa_refund_reversal(self):
        merchandise_return_response = self.perform_merchandise_return()
        response = self.perform_mVisa_refund_reversal(merchandise_return_response)
        self.assertEqual(str(response.status_code), "200", "M Visa Refund Reversal API")
        pass

    def test_mVisa_refund_reversal_get(self):
        base_uri = 'visadirect/'
        resource_path = 'mvisa/v1/mrr/'
        merchandise_return_response = self.perform_merchandise_return()
        timeout_response = self.perform_mVisa_refund_reversal(merchandise_return_response, True)
        status_identifier = timeout_response.content.decode()
        get_refund_reversal_response = self.visa_api_client.do_mutual_auth_request(
            base_uri + resource_path + status_identifier,
            None,
            'Refund Reversal Get',
            'get')
        response_code = get_refund_reversal_response.status_code
        self.assertTrue(response_code >= 200 and response_code <= 299,
                        "Refund Reversal Get test failed")


    def perform_mVisa_refund_reversal(self, merchandise_return_response, simulate_timeout = False):
        merchandise_return_response_json = json.loads(merchandise_return_response.text)
        request_payload = json.loads('''
        {"localTransactionDateTime": "''' + self.date + '''",
         "acquiringBin": "400171", 
         "feeProgramIndicator": "aaa",
         "transactionFeeAmt": "2",
         "acquirerCountryCode": "643", 
         "transactionIdentifier": "381228649430011", 
         "cardAcceptor": {"idCode": "ID-Code123","terminalId": "ABCD1234", "name": "CA123", "address": {"country": "IND"}}, 
         "originalDataElements": {
            "acquiringBin": "400171", 
            "systemsTraceAuditNumber": "897825", 
            "approvalCode": "20304B",
             "transmissionDateTime": "2016-11-30T03:00:37"
             },
            "recipientPrimaryAccountNumber": "4761360055652118", 
            "retrievalReferenceNumber": "430000367722", 
            "systemsTraceAuditNumber": "313223", 
            "senderCurrencyCode": "USD", 
            "amount": "24.01"
            }
        ''')
        request_payload['originalDataElements']['approvalCode'] = merchandise_return_response_json['approvalCode']
        request_payload['transactionIdentifier'] = merchandise_return_response_json['transactionIdentifier']
        base_uri = 'visadirect/'
        resource_path = 'mvisa/v1/mrr'
        if simulate_timeout:
            response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path,
                                                               request_payload,
                                                               'M Visa Refund Reversal API with Timeout', 'post',
                                                               {'x-transaction-timeout-ms': "1"},
                                                               stream=True)
        else:
            response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path,
                                                               request_payload,
                                                               'M Visa Refund Reversal API', 'post')
        return response

    def perform_merchandise_return(self, simulate_timeout=False):
        request_payload = json.loads(''' 
                {
                "acquirerCountryCode": "643",
                "transactionFeeAmt": "2.00",
                "acquiringBin": "400171",
                "amount": 124.05,
                "cardAcceptor": {
                "address": {
                "city": "Test",
                "country": "USA",
                "county": "San Mateo",
                "state": "CA",
                "zipCode": "94404"
                },
                "idCode": "CA-IDCode-77765",
                "name": "Visa Inc. USA-Foster City",
                "terminalId": "TID-9999"
                },
                "localTransactionDateTime": "''' + self.date + '''",
                "merchantCategoryCode": "6012",
                "merchantVerificationValue": {
                "mvvVisaAssigned": "41394644363445313243",
                "mvvAcquirerAssigned": "41394644363445313243"
                },
                "recipientPrimaryAccountNumber": "4761360055652118",
                "retrievalReferenceNumber": "430000367722",
                "systemsTraceAuditNumber": "451018",
                "transactionCurrencyCode": "USD",
                "feeProgramIndicator": "aaa",
                "settlementServiceIndicator": "9"
                }
''')
        base_uri = 'visadirect/'
        resource_path = 'mvisa/v1/mr'
        if simulate_timeout:
            response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path,
                                                                   request_payload,
                                                                   'M Visa Refund with Timeout', 'post',
                                                                   {'x-transaction-timeout-ms': "1"},
                                                                   stream=True)
        else:
            response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path,
                                                                   request_payload,
                                                                   'M Visa Refund API', 'post')
        return response


################################################################

if __name__ == '__main__':
    unittest.main()
    # END
