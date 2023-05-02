import json
import requests
	
def main():
	
	#Get security token
	securityUrl = "http://localhost:58000/api/v1/ticket"
	securityData = json.dumps({"username": "cisco","password": "cisco123"})
	securityHeader = {'Content-type': 'application/json'}
	r = requests.post(securityUrl, data=securityData, headers=securityHeader)
	token = r.json()["response"]["serviceTicket"]
	print("token: " + token)

	#Get hosts
	apiAccessHeader = {}
	apiAccessHeader['content-type'] = 'application/json'
	apiAccessHeader['x-auth-token'] = token
	r = requests.get('http://localhost:58000/api/v1/host', headers=apiAccessHeader);
	print(json.dumps(r.json(), indent=2))

if __name__ == "__main__":
	main()