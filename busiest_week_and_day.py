import json, sys
import operator
from datetime import datetime

weekly_commits = {}
weekday_commits = {}

def get_busiest_week(commits):
	json_commits = json.loads(commits)
	for commit in json_commits:
		date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
		week = date_object.isocalendar()[1]
		if week not in weekly_commits.keys():
			weekly_commits[week] = 1
		else:
			weekly_commits[week] += 1

def get_busiest_weekday(commits):
	json_commits = json.loads(commits)
	for commit in json_commits:
		date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
		weekday = date_object.strftime('%A')
		if weekday not in weekday_commits.keys():
			weekday_commits[weekday] = 1
		else:
			weekday_commits[weekday] += 1

def main():
    commit_file = open(sys.argv[1])
    for line in commit_file:
    	get_busiest_week(line)
    	get_busiest_weekday(line)
    busiest_week = max(weekly_commits.iteritems(), key=operator.itemgetter(1))[0]
    busiest_weekday = max(weekday_commits.iteritems(), key=operator.itemgetter(1))[0]
    print "Last year, the week that had the greatest number of commits is week #"+str(busiest_week)+"."
    print "Last year, the weekday that had the greatest number of commits is "+str(busiest_weekday)+" with "+str(weekday_commits[busiest_weekday])+" commits."

if __name__ == '__main__':
    main()
