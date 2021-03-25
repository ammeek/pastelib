import requests
import keys
import utils

sessionKey = keys.sessionKey
devKey = keys.devKey

def getPaste(pasteKey, sessionKey = sessionKey, devKey = devKey):
	paramaters = {
		"api_dev_key": devKey,
		"api_user_key": sessionKey,
		"api_paste_key": pasteKey,
		"api_option": "show_paste"
		}
	response = requests.post(url = "https://pastebin.com/api/api_raw.php", data = paramaters)
	pasteText = utils.outputBytesToString(response.content)
	return pasteText

# Posts a paste, and returns the paste ID.
# Full details are available at https://pastebin.com/api
def makePaste(pasteName, pasteText, expiryDate = "N", privacy = "0", devKey = devKey, sessionKey = sessionKey):
	paramaters = {
		"api_option": "paste",
		"api_dev_key": devKey,
		"api_paste_code": pasteText,
		"api_paste_private": privacy,
		"api_paste_name": pasteName,
		"api_paste_expire_date": expiryDate,
		"api_user_key": sessionKey
		}
	response = requests.post(url = "https://pastebin.com/api/api_post.php", data = paramaters)
	output = utils.outputBytesToString(response.content)
	return output

def deletePaste(pasteKey, sessionKey = sessionKey, devKey = devKey):
	paramaters = {
		"api_dev_key": devKey,
		"api_user_key": sessionKey,
		"api_paste_key": pasteKey,
		"api_option": "delete"
		}
	response = requests.post(url = "https://pastebin.com/api/api_post.php", data = paramaters)
	output = utils.outputBytesToString(response.content)
	return output
