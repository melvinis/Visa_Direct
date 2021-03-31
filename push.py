# Financial Message Type: OCT - Original Credit Transaction (Push Funds Transaction)
import requests
import json
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
url 	= "https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pushfundstransactions"
cert 	= 'cert.pem'
key 	= 'key_141490f1-47f9-474d-ad5c-299bf6e8283b.pem'
headers	= {"Accept": "application/json"}
user_id	= '59EFB7J0LYMR9L0945TP21zQ43-A4CCG0apNkBp6pvEiAe4jw'
password= 'RYPLmxZ8'
body	= {}
payload = json.loads(''' 
{
"amount": "124.05",
"senderAddress": "901 Metro Center Blvd",
"localTransactionDateTime": "''' + date + '''",
"pointOfServiceData": {
"panEntryMode": "90",
"posConditionCode": "00",
"motoECIIndicator": "0"
},
"recipientPrimaryAccountNumber": "4957030420210496",
"colombiaNationalServiceData": {
"addValueTaxReturn": "10.00",
"taxAmountConsumption": "10.00",
"nationalNetReimbursementFeeBaseAmount": "20.00",
"addValueTaxAmount": "10.00",
"nationalNetMiscAmount": "10.00",
"countryCodeNationalService": "170",
"nationalChargebackReason": "11",
"emvTransactionIndicator": "1",
"nationalNetMiscAmountType": "A",
"costTransactionIndicator": "0",
"nationalReimbursementFee": "20.00"
},
"cardAcceptor": {
"address": {
"country": "USA",
"zipCode": "94404",
"county": "San Mateo",
"state": "CA"
},
"idCode": "CA-IDCode-77765",
"name": "Visa Inc. USA-Foster City",
"terminalId": "TID-9999"
},
"senderReference": "",
"transactionIdentifier": "381228649430015",
"acquirerCountryCode": "840",
"acquiringBin": "408999",
"retrievalReferenceNumber": "412770451018",
"senderCity": "Foster City",
"senderStateCode": "CA",
"systemsTraceAuditNumber": "451018",
"senderName": "Mohammed Qasim",
"businessApplicationId": "AA",
"settlementServiceIndicator": "9",
"merchantCategoryCode": "6012",
"transactionCurrencyCode": "USD",
"recipientName": "rohan",
"senderCountryCode": "124",
"sourceOfFundsCode": "05",
"senderAccountNumber": "4653459515756154"
}
''')
timeout	= 10

r = requests.post(url,
                #   verify = ('put the CA certificate pem file path here'),
				  cert = (cert,key),
				  headers = headers,
				  auth = (user_id, password),
				#   data = body,
				  json = payload,
				  timeout = timeout)

print(r.text)		