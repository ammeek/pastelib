import requests
import json
import utils

# Extract credentials from JSON file
def getCredentials(credentialsLocation="credentials.json"):
	# Open the credentials JSON file
	with open(credentialsLocation) as credentialsFile:
		# Load the JSON into memory
		data = json.load(credentialsFile)
		# Extract the credentials from the JSON
		devKey = data["devKey"]
		username = data["username"]
		password = data["password"]
		return (devKey, username, password)

def getKeys(credentials):
	# Construct the query
	paramaters = {
		"api_dev_key": credentials[0],
		"api_user_name": credentials[1],
		"api_user_password": credentials[2]
		}
	# Send request and get response
	response = requests.post(url = "https://pastebin.com/api/api_login.php", data = paramaters)
	# Remove formatting data
	sessionKey = utils.outputBytesToString(response.content)
	devKey = credentials[0]

	return sessionKey, devKey

sessionKey, devKey = getKeys(getCredentials())
