from flask import Flask, request, render_template, redirect
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def display_oncalls():
    """Display on-calls."""

    API_KEY = 'WTS8E_CuvcyrnLHEy_JR' # Your API key here
    
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }

    # You can add any of the parameters listed here to the payload:
    # https://v2.developer.pagerduty.com/v2/page/api-reference#!/On-Calls/get_oncalls
    # Just add params=payload to the GET request below like so:
    # r = requests.get(url, headers=headers, params=payload)
    
    # To specify a list of escalation policies or schedules, URL encode them like this:
    # r = requests.get("https://api.pagerduty.com/oncalls?escalation_policy_ids[]=PZJFPAL", headers=headers)
    # For more info: https://v2.developer.pagerduty.com/v2/page/api-reference#!/On-Calls/get_oncalls
    
    r = requests.get("https://api.pagerduty.com/oncalls", headers=headers)

    oncall_data = {} # Python dict will be structured like: {user_id: [ep_name, user_name, phone_num]}

    for oncall in r.json()['oncalls']:
        
        user_id = oncall['user']['id']
        user_name = oncall['user']['summary']
        ep_name = oncall['escalation_policy']['summary']

        r = requests.get("https://api.pagerduty.com/users/{}/contact_methods?type=phone_contact_method".format(user_id), headers=headers)

        if r.json()['contact_methods']:
            phone_num = r.json()['contact_methods'][0]['address']
        else:
            phone_num = "No phone number specified"

        oncall_data[user_id] = [ep_name, user_name, phone_num]

    # Passing the JSON body to the Jinja template in templates/index.html
    return render_template("index.html", oncalls=oncall_data)


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0", port=3000)