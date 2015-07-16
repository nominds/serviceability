from flask import request
from flask import Response
from flask import render_template
from flask import Flask

import datetime
import time
import re

app = Flask(__name__)
app.debug = True

def readLogFile(stDate, edDate):
	fhand = open('audit.log')
	d = dict()
	count = 0
	errorsList = []
	index = 0

	for line in fhand:
		if (line.find('COEN00') != -1):
			line = line.rstrip()
			logDateTime = line[0:19]
			try:
				logDateTime = datetime.datetime.strptime(logDateTime, "%Y-%m-%d %H:%M:%S")
			except:
				if (line.find('Caused by:')== -1):
					continue
			if ((line.find('Caused by:')!= -1) or (logDateTime >= stDate and logDateTime <= edDate)):
				errorsList.append(line + "<br>")
				index = index + 1
				#errorsList = '<li>' + errorsList + '</li>'
				startIndex = line.find('COEN00')
				endIndex = line.find(' ', startIndex)
				key = line[startIndex:endIndex]
				count = count + 1
				if key not in d:
					d[key] = 1
				else:
					d[key] = d[key] + 1
	errorsList.append("<br>" + "Summary: " + str(d))	
	return errorsList
#print 'Approximate errors reported :', count


@app.route("/JSR")
def hello():
    return "Hello JSR's World!"
	
	
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

	
@app.route('/first/')
def index():
	return render_template('calendar.html')
	#return render_template('calendar.html')   

@app.route('/first/calendar')
def readCalendar():
	index = 0
	stDate = request.args.get('startDate')
	stTime = request.args.get('startTime')
	edDate = request.args.get('endDate')
	edTime = request.args.get('endTime')
	stDate = stDate + ' ' + stTime
	edDate = edDate + ' ' + edTime
	#print stDate
	startDate = datetime.datetime.strptime(stDate, "%m/%d/%Y %H:%M")
	try:
		endDate1 = datetime.datetime.strptime(edDate, "%m/%d/%Y %H:%M")
	except:
		endDate1 = time.strftime('%m/%d/%Y %H:%M')
		endDate1 = datetime.datetime.strptime(endDate1, "%m/%d/%Y %H:%M")
	#print startDate
	d = []
	d = readLogFile(startDate, endDate1)
	return Response("%s" % (d))


	
@app.route('/first/login')
def login():
	fname1 = request.args.get('fname')
	lname1 = request.args.get('lname')
	return Response("Hello %s %s" % (fname1,lname1))
	
if __name__ == "__main__":
    app.run()