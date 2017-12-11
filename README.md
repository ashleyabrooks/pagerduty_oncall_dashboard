
## About the dashboard

This is a Flask app built as a boilerplate for PagerDuty customers to create their own on-call dashboards. It's heavily commented to explain some of the customization that can be done with additional calls to our REST API. The app currently displays all users on-call, along with the schedules for which their on-call as well as the users' contact information. 


## How to run this app:

1. In your terminal, change directories into the directory with the dashboard code, then install the dependencies from requirements.txt. I like to use pip in a virtualenv like so:
	 a. `virtualenv env`
	 b. `source env/bin/activate`
	 c. `pip install -r requirements.txt`).
2. Enter an API key from your PagerDuty account into `server.py`.
3. Run `python server.py` to get the Flask server running.
4. View your new on-call dashboard at localhost:3000.

