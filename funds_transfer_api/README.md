##License
**© Copyright 2018 - 2020 Visa. All Rights Reserved.** 

*NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*

*By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims all liability for any such components, including continued availability and functionality. Benefits depend on implementation details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,implementation and resources by you based on your business and operational details. Please refer to the specific API documentation for details on the requirements, eligibility and geographic availability.*

*This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*

# Funds Transfer API
The Funds Transfer API can pull funds from the sender&apos;s Visa account (in preparation for pushing funds to a recipient&apos;s account) in an Account Funding Transaction (AFT).  Additionally, the Funds Transfer API also provides functionality to push funds to the recipient&apos;s Visa account in an Original Credit Transaction (OCT).  If a transaction is declined, the Funds Transfer API can also return the funds to the sender&apos;s funding source in an Account Funding Transaction Reversal (AFTR). The API has been enhanced to allow originators to send their PushFundsTransactions(OCTs) and PullFundsTransactions(AFTs) to Visa for routing to multiple U.S. debit networks.

- API version: 1.0
- Package version: 1.0.0

For more information, please visit [https://developer.visa.com/](https://developer.visa.com/)

## Requirements.

Python  3.4+

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

Refer to VDP for detailed reference of API.

All URIs are relative to *https://sandbox.api.visa.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FundsTransferApi* | [**getmultipullfundstransactions**](docs/FundsTransferApi.md#getmultipullfundstransactions) | **GET** /visadirect/fundstransfer/v1/multipullfundstransactions/{statusIdentifier} | 
*FundsTransferApi* | [**getmultipushfundstransactions**](docs/FundsTransferApi.md#getmultipushfundstransactions) | **GET** /visadirect/fundstransfer/v1/multipushfundstransactions/{statusIdentifier} | 
*FundsTransferApi* | [**getmultireversefundstransactions**](docs/FundsTransferApi.md#getmultireversefundstransactions) | **GET** /visadirect/fundstransfer/v1/multireversefundstransactions/{statusIdentifier} | 
*FundsTransferApi* | [**getpullfundstransactions**](docs/FundsTransferApi.md#getpullfundstransactions) | **GET** /visadirect/fundstransfer/v1/pullfundstransactions/{statusIdentifier} | 
*FundsTransferApi* | [**getpushfundstransactions**](docs/FundsTransferApi.md#getpushfundstransactions) | **GET** /visadirect/fundstransfer/v1/pushfundstransactions/{statusIdentifier} | 
*FundsTransferApi* | [**getreversefundstransactions**](docs/FundsTransferApi.md#getreversefundstransactions) | **GET** /visadirect/fundstransfer/v1/reversefundstransactions/{statusIdentifier} | 
*FundsTransferApi* | [**postmultipullfunds**](docs/FundsTransferApi.md#postmultipullfunds) | **POST** /visadirect/fundstransfer/v1/multipullfundstransactions | 
*FundsTransferApi* | [**postmultipushfunds**](docs/FundsTransferApi.md#postmultipushfunds) | **POST** /visadirect/fundstransfer/v1/multipushfundstransactions | 
*FundsTransferApi* | [**postmultireversefunds**](docs/FundsTransferApi.md#postmultireversefunds) | **POST** /visadirect/fundstransfer/v1/multireversefundstransactions | 
*FundsTransferApi* | [**postpullfunds**](docs/FundsTransferApi.md#postpullfunds) | **POST** /visadirect/fundstransfer/v1/pullfundstransactions | 
*FundsTransferApi* | [**postpushfunds**](docs/FundsTransferApi.md#postpushfunds) | **POST** /visadirect/fundstransfer/v1/pushfundstransactions | 
*FundsTransferApi* | [**postreversefunds**](docs/FundsTransferApi.md#postreversefunds) | **POST** /visadirect/fundstransfer/v1/reversefundstransactions | 


## Documentation For Models
Refer to VDP for detailed reference of models.
 - [Address](docs/Address.md)
 - [AddressVerificationData](docs/AddressVerificationData.md)
 - [CardAcceptor](docs/CardAcceptor.md)
 - [MagneticStripeData](docs/MagneticStripeData.md)
 - [MerchantVerificationValue](docs/MerchantVerificationValue.md)
 - [MultipullfundspostPayload](docs/MultipullfundspostPayload.md)
 - [MultipullfundspostResponse](docs/MultipullfundspostResponse.md)
 - [MultipullfundstransactionsgetResponse](docs/MultipullfundstransactionsgetResponse.md)
 - [MultipushfundspostPayload](docs/MultipushfundspostPayload.md)
 - [MultipushfundspostResponse](docs/MultipushfundspostResponse.md)
 - [MultipushfundstransactionsgetResponse](docs/MultipushfundstransactionsgetResponse.md)
 - [MultireversefundspostPayload](docs/MultireversefundspostPayload.md)
 - [MultireversefundspostResponse](docs/MultireversefundspostResponse.md)
 - [MultireversefundstransactionsgetResponse](docs/MultireversefundstransactionsgetResponse.md)
 - [OriginalDataElements](docs/OriginalDataElements.md)
 - [PinData](docs/PinData.md)
 - [PointOfServiceCapability](docs/PointOfServiceCapability.md)
 - [PointOfServiceData](docs/PointOfServiceData.md)
 - [PullfundspostPayload](docs/PullfundspostPayload.md)
 - [PullfundspostResponse](docs/PullfundspostResponse.md)
 - [PullfundstransactionsgetResponse](docs/PullfundstransactionsgetResponse.md)
 - [PushfundspostPayload](docs/PushfundspostPayload.md)
 - [PushfundspostResponse](docs/PushfundspostResponse.md)
 - [PushfundstransactionsgetResponse](docs/PushfundstransactionsgetResponse.md)
 - [ReversefundspostPayload](docs/ReversefundspostPayload.md)
 - [ReversefundspostResponse](docs/ReversefundspostResponse.md)
 - [ReversefundstransactionsgetResponse](docs/ReversefundstransactionsgetResponse.md)
 - [SecurityRelatedControlInfo](docs/SecurityRelatedControlInfo.md)

