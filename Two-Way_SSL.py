import requests
import json

url 	= "https://sandbox.api.visa.com/vdp/helloworld"
cert 	= 'cert.pem'
key 	= 'key_141490f1-47f9-474d-ad5c-299bf6e8283b.pem'
headers	= {}
user_id	= '59EFB7J0LYMR9L0945TP21zQ43-A4CCG0apNkBp6pvEiAe4jw'
password= 'RYPLmxZ8'
body	= {}
payload = json.loads('''{}
''')
timeout	= 10

r = requests.get(url,
                #   verify = ('put the CA certificate pem file path here'),
				  cert = (cert,key),
				  headers = headers,
				  auth = (user_id, password),
				#   data = body,
				  json = payload,
				  timeout = timeout)

print(r.text)		