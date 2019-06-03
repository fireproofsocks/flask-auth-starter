from google.oauth2 import id_token
from google.auth.transport import requests


def validate_token(token, client_id, **kwargs):
    """
    This function validates the given JWT and returns the Google User data if the token is valid for
    the restrictions supplied.

    See https://developers.google.com/identity/sign-in/web/backend-auth

    :param token: string JWT from Google Sign In flow
    :param client_id: string or list of Google Client ID
    :param kwargs: optionally list allowable GSuite domains that are considered valid creators of this token.
    :return: dictionary representing Google User, Exception on invalid
    """

    client_ids = client_id if isinstance(client_id, list) else [client_id]
    domains = kwargs.get('domains', [])

    user_data = id_token.verify_oauth2_token(token, requests.Request())

    if user_data['aud'] not in client_ids:
        raise ValueError('Could not verify audience: client ID not allowed.')

    if user_data['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    # Verify that token is from allowed G Suite domain(s):
    if domains and user_data['hd'] not in domains:
        raise ValueError('Invalid hosted domain.')

    return user_data
