from flask import Flask, request, render_template, redirect
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def display_oncalls():
    """Display on-calls."""

    API_KEY = '' # Your API key here

    url = 'https://api.pagerduty.com/oncalls'
    
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }

    # You can add any of the parameters listed here to the payload:
    # https://v2.developer.pagerduty.com/v2/page/api-reference#!/On-Calls/get_oncalls
    # Just add params=payload to the GET request below like so:
    # r = requests.get(url, headers=headers, params=payload)
    
    r = requests.get(url, headers=headers)

    # Passing the JSON body to the Jinja template in templates/index.html
    return render_template("index.html", oncalls=r.json()['oncalls'])


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0", port=3000)