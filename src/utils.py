# Removes formatting and converts the API output to a string
def outputBytesToString(outputBytes):
	strVersion = str(outputBytes)
	strVersion = strVersion[:-1]
	strVersion = strVersion[2:]
	strVersion = strVersion.replace("\\r\\n", "\n")
	return strVersion