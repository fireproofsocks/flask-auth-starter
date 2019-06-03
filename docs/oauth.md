# OAuth


## Setup

Implementing Google OAuth to gain access to your web application involves setting up a browser client.

The most helpful link in setting up Google OAuth sign-in is this: [https://developers.google.com/identity/sign-in/web/sign-in](https://developers.google.com/identity/sign-in/web/sign-in)

Configure a Project - pay attention to where you're calling the OAuth process from.  If you're implementing this on a client (e.g. a Node app pointed at our API), then you'll get a Javascript button. 

Example values:

Client ID
```
123-xxxxx.apps.googleusercontent.com
```
Client Secret
```
AxBcDx_9S4b1gZ7rU5X0
```

You can always manage your API credentials and usage later in the API Console:
[https://console.developers.google.com/apis](https://console.developers.google.com/apis)

Select your app from from the dropdown in the top title bar.  Remember: this is all specific to the client at this point.  It has nothing to do with the Tenor backend.

## Whitelisting Origins

1. Go to [https://console.developers.google.com/](https://console.developers.google.com/), select your Sign-In project from dropdown at top-left.
2. Click on the "Credentials" link in the left-hand menu
3. Click on the pencil icon next to your particular client.
4. Add your domain for the "Allowed Javascript Origins", e.g. `http://127.0.0.1:5000`
5. Save

It may take Google a few minutes to register the change.

Warning: `http://127.0.0.1` does not seem to be supported -- you end up with a non-specific 400 bad request error?  But then again, eventually this seemed to work. 

## Browser Sign-In


Once you have JS working and able to receive and print profile information, you will want to package it into a token and post it to your backend:

https://developers.google.com/identity/sign-in/web/backend-auth

You can implement this in a static site: you must only include your client ID in your Javascript.

See the demo pages inside `apps/api/lib/api_web/templates/demo/`:
`google_login.html.eex` and `google_signup.html.eex`

### Troubleshooting / Errors

Remember: you cannot use an IP address! For local development, you must edit your `/etc/hosts` file and use named domain, e.g. `flask.localhost`.

If you get an error:
```
Error: redirect_uri_mismatch
```

That means you need to configure your app to allow the URL that you're using for your signin. Follow the link in the message to correct.


You can check the token that Google provides:

```
https://oauth2.googleapis.com/tokeninfo?id_token=XYZ123
```

Example response:

```
{
    "iss": "accounts.google.com",
    "azp": "202926320516-ek1je613akl5gcjkeub2r1ggnbarccvo.apps.googleusercontent.com",
    "aud": "202926320516-ek1je613akl5gcjkeub2r1ggnbarccvo.apps.googleusercontent.com",
    "sub": "1111112222222",
    "hd": "leafgroup.com",
    "email": "john.doe@somesite.com",
    "email_verified": "true",
    "at_hash": "2yCfDnLowSohnBxK4aI4Bw",
    "name": "John Doe",
    "picture": "https://lh3.googleusercontent.com/-b83NiwCriQQ/AAAAAAAAAAI/AAAAAAAAACM/LLAABB/s96-c/photo.jpg",
    "given_name": "John",
    "family_name": "Doe",
    "locale": "en",
    "iat": "1548612465",
    "exp": "1548616065",
    "jti": "9460549fc474fb60bb29c0e5765d726a0cb99caa",
    "alg": "RS256",
    "kid": "b15a2b8f7a6b3f6bc08bc1c56a88410e146d01fc",
    "typ": "JWT"
}
```

To verify the JWT's, you will need to use Google's public keys, available in the following formats:

- JWK: https://www.googleapis.com/oauth2/v3/certs
- PEM: https://www.googleapis.com/oauth2/v1/certs

Remember: these keys are regularly rotated; examine the `Cache-Control` header in the response to determine when you should retrieve them again.


### Invalid Client 

```
Error: invalid_client

The OAuth client was not found.
```

```
Error: invalid_request

Permission denied to generate login hint for target domain.
```

