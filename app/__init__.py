# Load up ENV variables
import app.bootstrap
import app.config
import app.routes


# import os
# from flask import Flask, redirect, url_for, session, render_template, jsonify, request
# from flask import Flask

# from app.auth import google


#
# # You must configure these 3 values from Google APIs console
# # https://code.google.com/apis/console
# GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
#
# app = Flask(__name__, static_folder='./public', static_url_path='')
# app.debug = os.getenv("FLASK_DEBUG")
# app.secret_key = os.getenv("FLASK_SECRET_KEY")
# # app.config['SERVER_NAME'] = 'flask.localhost:5000'
# #
# # @app.route('/')
# # def index():
# #     return GOOGLE_CLIENT_ID
# #     # access_token = session.get('access_token')
# #     # if access_token is None:
# #     #     return redirect(url_for('login'))
# #     #
# #     # access_token = access_token[0]
# #     #
# #     #
# #     # headers = {'Authorization': 'OAuth ' + access_token}
# #     # req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
# #     #               None, headers)
# #     # try:
# #     #     res = urlopen(req)
# #     # except URLError, e:
# #     #     if e.code == 401:
# #     #         # Unauthorized - bad token
# #     #         session.pop('access_token', None)
# #     #         return redirect(url_for('login'))
# #     # return res.read()
# #
# #
# # @app.route('/login')
# # def login():
# #     return render_template('login.html', GOOGLE_CLIENT_ID=GOOGLE_CLIENT_ID)
# #     # callback = url_for('authorized', _external=True)
# #     # return google.authorize(callback=callback)
# #
# #
# # @app.route('/api/login', methods=['POST'])
# # def post_login():
# #     # https://developers.google.com/identity/sign-in/web/backend-auth
# #     token = request.json['token']
# #
# #     token = google.validate_token(token, GOOGLE_CLIENT_ID)
# #     # try:
# #     #     # Specify the CLIENT_ID of the app that accesses the backend:
# #     #     idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
# #     #     print(idinfo)
# #     #     # Or, if multiple clients access the backend server:
# #     #     # idinfo = id_token.verify_oauth2_token(token, requests.Request())
# #     #     # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
# #     #     #     raise ValueError('Could not verify audience.')
# #     #
# #     #     if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
# #     #         raise ValueError('Wrong issuer.')
# #     #
# #     #     # If auth request is from a G Suite domain:
# #     #     # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
# #     #     #     raise ValueError('Wrong hosted domain.')
# #     #
# #     #     # ID token is valid. Get the user's Google Account ID from the decoded token.
# #     #     userid = idinfo['sub']
# #     # except ValueError:
# #     #     # Invalid token
# #     #     pass
# #
# #     return jsonify({"jwt": token})
# #     # return jsonify({"some": "thing"})
# # #
# # #
# # # @app.route(REDIRECT_URI)
# # # @google.authorized_handler
# # # def authorized(resp):
# # #     access_token = resp['access_token']
# # #     session['access_token'] = access_token, ''
# # #     return redirect(url_for('index'))
# # #
# # #
# # # @google.tokengetter
# # # def get_access_token():
# # #     return session.get('access_token')
# #
#
# # print(app)