from holehe.core import *
from holehe.localuseragent import *


def vrbo(email):
    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'x-homeaway-site': 'vrbo',
        'Origin': 'https://www.vrbo.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    data = '{"emailAddress":"' + email + '"}'

    response = requests.post(
        'https://www.vrbo.com/auth/aam/v3/status',
        headers=headers,
        data=data)
    response = response.json()

    if "authType" in response.keys():
        if response["authType"][0] == "LOGIN_UMS":
            return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
        elif response["authType"][0] == "SIGNUP":
            return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
        else:
            return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
