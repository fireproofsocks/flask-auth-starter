from flask import render_template, jsonify, request
from app.auth import google
from app.bootstrap import app


@app.route('/')
def index():
    return app.config['GOOGLE_CLIENT_ID']
    # access_token = session.get('access_token')
    # if access_token is None:
    #     return redirect(url_for('login'))
    #
    # access_token = access_token[0]
    #
    #
    # headers = {'Authorization': 'OAuth ' + access_token}
    # req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
    #               None, headers)
    # try:
    #     res = urlopen(req)
    # except URLError, e:
    #     if e.code == 401:
    #         # Unauthorized - bad token
    #         session.pop('access_token', None)
    #         return redirect(url_for('login'))
    # return res.read()


@app.route('/login')
def login():
    return render_template('login.html', GOOGLE_CLIENT_ID=app.config['GOOGLE_CLIENT_ID'])
    # callback = url_for('authorized', _external=True)
    # return google.authorize(callback=callback)


@app.route('/private')
def private():
    return 'This page should be private'

# ---------------------------------------------------------------------------------------------------------------
# API Routes
# ---------------------------------------------------------------------------------------------------------------
@app.route('/api/login', methods=['POST'])
def post_login():

    token = request.json['token']

    token = google.validate_token(token, app.config['GOOGLE_CLIENT_ID'])

    return jsonify({"jwt": token})
#
#
# @app.route(REDIRECT_URI)
# @google.authorized_handler
# def authorized(resp):
#     access_token = resp['access_token']
#     session['access_token'] = access_token, ''
#     return redirect(url_for('index'))
#
#
# @google.tokengetter
# def get_access_token():
#     return session.get('access_token')

