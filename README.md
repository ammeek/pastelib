# pastelib
A simple python library utilising the pastebin API. At the moment it can download, upload, and delete pastes.

## Files
### pastelib.py
This file contains the functions for connecting to and using the api. You can use it to download, upload, and delete pastes.

### utils.py
This file contains some code for formatting the API responses.

### keys.py
This file contains code for handling authentication. It extracts credentials from `credentials.json` and uses them to obtain a session key, which is used by `pastelib.py` to authenticate.

### credentials.json
This file should contain your pastebin username, password, and developer key. You should not interact with it under any circumstances, instead getting a session key and developer key via `keys.py`. Remember to remove your details from this file before sharing it.
