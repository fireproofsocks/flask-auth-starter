# -----------------------------------------------------------------------------------
# Configure your app!
# There are more options for Flask: http://flask.pocoo.org/docs/1.0/config/
# -----------------------------------------------------------------------------------
import os
from app.bootstrap import app

app.config.update(
    debug=os.getenv("FLASK_DEBUG"),
    secret_key=os.getenv("FLASK_SECRET_KEY"),
    # See https://code.google.com/apis/console
    GOOGLE_CLIENT_ID=os.getenv("GOOGLE_CLIENT_ID"),
    GOOGLE_CLIENT_SECRET=os.getenv("GOOGLE_CLIENT_SECRET"),
    # REDIRECT_URI='/oauth2callback'
)
