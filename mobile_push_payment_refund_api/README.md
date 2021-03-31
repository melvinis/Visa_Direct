##License
**© Copyright 2018 - 2020 Visa. All Rights Reserved.** 

*NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*

*By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims all liability for any such components, including continued availability and functionality. Benefits depend on implementation details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,implementation and resources by you based on your business and operational details. Please refer to the specific API documentation for details on the requirements, eligibility and geographic availability.*

*This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*

# Reports API
The Reports API provides reporting capabilities such as transaction reconciliation data API. The data needed for reconciliation includes both push(OCT) and pull(AFT) transaction details and any exceptions such as chargebacks & reversals. This data allows you to reconcile the transactions sent by your systems with what was processed through VisaNet.<br> <br> <b>Note: This functionality is currently available for US transactions ONLY.</b>

- API version: 1.0
- Package version: 1.0.0

For more information, please visit [https://developer.visa.com/](https://developer.visa.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

To install by pip, execute the below command.

```sh
pip install -r requirements.txt
```
(you may need to run `pip` with root permission: `sudo pip install -r requirements.txt`)

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Tests
- Edit the file **configuration.ini** to set the fields shown below. Please refer the [Getting Started Guide](https://developer.visa.com/vdpguide#get-started-overview) to get the credentials.

```
# For mutual auth
userId = {YOUR USER NAME}
password = {YOUR PASSWORD}
cert = {/absolute/path/to/cert.pem}
key = {/absolute/path/to/key_xxxx.pem}


# For x-pay token
apiKey = {YOUR API KEY}
sharedSecret = {YOUR SHARED SECRET}

# For Proxy
proxyHostName = {PROXY HOST NAME}
proxyPortNumber = {PROXY PORT NUMBER}
proxyUserName = {PROXY USER NAME HERE}
proxyPassword = {PROXY PASSWORD}

```
To run the unit tests:
- Note: The data in the unit tests are just placeholders. Please refer the [Create Project Guide](https://developer.visa.com/pages/working-with-visa-apis/create-project) to get the test data
```
nosetests --nocapture
```


## Documentation for API Endpoints

All URIs are relative to *https://sandbox.api.visa.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RefundApiApi* | [**getmerchandise_return_get**](docs/RefundApiApi.md#getmerchandise_return_get) | **GET** /visadirect/mvisa/v1/mr/{statusIdentifier} | 
*RefundApiApi* | [**getmerchandise_return_reversal_get**](docs/RefundApiApi.md#getmerchandise_return_reversal_get) | **GET** /visadirect/mvisa/v1/mrr/{statusIdentifier} | 
*RefundApiApi* | [**postmerchandise_return_post**](docs/RefundApiApi.md#postmerchandise_return_post) | **POST** /visadirect/mvisa/v1/mr | 
*RefundApiApi* | [**postmerchandise_return_reversal_post**](docs/RefundApiApi.md#postmerchandise_return_reversal_post) | **POST** /visadirect/mvisa/v1/mrr | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [CardAcceptor](docs/CardAcceptor.md)
 - [MerchandiseReturnGetgetResponse](docs/MerchandiseReturnGetgetResponse.md)
 - [MerchandiseReturnPostpostPayload](docs/MerchandiseReturnPostpostPayload.md)
 - [MerchandiseReturnPostpostResponse](docs/MerchandiseReturnPostpostResponse.md)
 - [MerchandiseReturnReversalGetgetResponse](docs/MerchandiseReturnReversalGetgetResponse.md)
 - [MerchandiseReturnReversalPostpostPayload](docs/MerchandiseReturnReversalPostpostPayload.md)
 - [MerchandiseReturnReversalPostpostResponse](docs/MerchandiseReturnReversalPostpostResponse.md)
 - [MerchantVerificationValue](docs/MerchantVerificationValue.md)
 - [OriginalDataElements](docs/OriginalDataElements.md)

