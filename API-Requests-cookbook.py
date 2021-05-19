"""
A simple `requests` based cookbook for API interactions
"""

import requests
from requests.auth import HTTPBasicAuth
import json
import getpass
from datetime import timedelta

"""
ASA/FIREPOWER
Basic Auth token generation and refresh
Use this X-Auth token to authenticate by passing it in the request headers like so:
headers = {'Content-Type': 'application/json',
           'X-auth-access-token': x_auth_token}

"""
requests.packages.urllib3.disable_warnings()  # Supresses self-signed InsecureRequestWarning

def tokenGenerate():
    """
    Get my username and secret_password via getpass
    Initiate an HTTP-POST to API
    and retrieve the X-Auth-Token value from the response headers.
    This token will then be used for API manipulation going forward.
    :return: x_auth_token - <type: string> an auth token.
    :return: x_auth_refresh_token - <type: string> a refresh token
    :return: token_expires_at - <type: datetime object> the time that the token will expire
    """
    # Gather username automatically via environment variables
    print('[!] Provide your password to generate an API token now...')
    username = getpass.getuser().lower()        # All usernames will be forced lowercase. This may cause some issues
    print(f"[!] Username: {username}")
    secret_password = getpass.getpass("[!] Password: ")
    
    # Send API request using HTTPBasicAuth for authentication
    r = requests.post('https://<<MY API TARGET HERE>>',
                       headers={'Content-Type': 'application/json'},
                       verify=False,    # verify=False for self-signed certificates
                       auth=HTTPBasicAuth(username, secret_password))

    try:
        # parsing response object and retrieving auth_token, refresh_token, and the expiry time object (optional)
        x_auth_token = r.headers['X-auth-access-token']             # Auth token in the response headers
        x_auth_refresh_token = r.headers['X-auth-refresh-token']    # Refresh token in the response headers
        token_expires_at = datetime.now() + timedelta(minutes=30)   # Timedelta of 30 minutes for token lifetime
        return x_auth_token, x_auth_refresh_token, token_expires_at
    except:
        print(f'[!] Login Failure!')
        
"""
Example usage
"""
x_auth_token, x_auth_refresh_token, token_expires_at = tokenGenerate()


def refreshToken(x_auth_token, x_auth_refresh_token):
    """
    Initiate an HTTP-POST to API
    and refresh our x-auth token for continued access.
    These tokens have a lifetime of 30m
    :param: token -<type: string> existing x_auth_token generated from tokenGenerate()
    :param: refreshtoken - <type: string> existing x_auth_refresh_token generated from tokenGenerate()
    :return: x_auth_token - <type: string> an auth token.
    :return: x_auth_refresh_token - <type: string> a refresh token
    :return: token_expires_at - a <type: datetime object> time that the token will expire
    """
    r = requests.post('https://<<MY API TARGET HERE>>',
                       headers={'Content-Type': 'application/json',
                                'X-auth-access-token': x_auth_token,
	                              'X-auth-refresh-token': x_auth_refresh_token},
                       verify=False,)
    try:
        x_auth_token = r.headers['X-auth-access-token']
        x_auth_refresh_token = r.headers['X-auth-refresh-token']
        token_expires_at = datetime.now() + timedelta(minutes=30)
        return x_auth_token, x_auth_refresh_token, token_expires_at
    except:
        print(f'[!] Token refresh failure!')
        
"""
Example usage
"""
x_auth_token, x_auth_refresh_token, token_expires_at = refreshToken(x_auth_token, x_auth_refresh_token)



##
"""
OAuth2 Bearer token authentication
"""
my_client_id = 'abcdefg'
my_client_secret = '12345'
def tokenGenerate():
    """
    This function will initiate an HTTP-POST to <<MY API>>
    and retrieve the OAuth2 access token value from the response content using API keys
    This token is then put in to the format of the Authorization header value {Bearer <token>}
    This token will be active for 30 mins.    
    :return: token - a string containing an auth token for the API
    """
    oauth2_session = requests.post(url="https://<<MY API HERE>>",
                                   headers={"accept": "application/json",
                                            "Content-Type": "application/x-www-form-urlencoded"},
                                   data=f"client_id={my_client_id}&client_secret={my_client_secret}")
    try:
        data = oauth2_session.json()['access_token']
        token = f"Bearer {data}"

    except:
        token = "Error"
        print(f'[!] Authentication Failure!')
        
""" usage """
token = tokenGenerate()

"""
Complex API call using params, headers, and payload data.
Using OAuth2 bearer token in the request 'Authorization' header
"""
def AddToSeparatedUserGroup(list_of_host_aids): 
    response = requests.post(url="https://<<MY API HERE>>",
                            headers={"accept": "application/json",
				                             "Content-Type": "application/json",
                                     "Authorization": token},
                            params={"action_name" : "add-hosts"},
                            data=json.dumps({"action_parameters": [{"name": "filter",
                                                                    "value": f"(device_id:{list_of_host_aids})"}],
                                                                    "ids": ["45ee1b0decdf4d6689f826cec0600563"]}))
    if response.ok:
        print(f"[+] Added {len(list_of_host_aids)} hosts to 'Separated User Group'")
    if not response.ok:
        print(f"[-] Failed to add {len(list_of_host_aids)} hosts to 'Separated User Group'")
