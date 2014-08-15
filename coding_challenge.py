import json, sys
import operator
from datetime import datetime

weekly_commits = {}
daily_commits = {}

def get_busiest_week(commits):
	json_commits = json.loads(commits)
	for commit in json_commits:
		date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
		week = date_object.isocalendar()[1]
		if week not in weekly_commits.keys():
			weekly_commits[week] = 1
		else:
			weekly_commits[week] += 1

def get_busiest_day(commits):
	json_commits = json.loads(commits)
	for commit in json_commits:
		date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
		if date_object not in daily_commits.keys():
			daily_commits[date_object] = 1
		else:
			daily_commits[date_object] += 1

def main():
    commit_file = open(sys.argv[1])
    for line in commit_file:
    	get_busiest_week(line)
    	get_busiest_day(line)
    busiest_week = max(weekly_commits.iteritems(), key=operator.itemgetter(1))[0]
    busiest_day = max(daily_commits.iteritems(), key=operator.itemgetter(1))[0]
    print weekly_commits
    print daily_commits
    print "Last year, the week that had the greatest number of commits is week #"+str(busiest_week)+"."
    print "Last year, the day that had the greatest number of commits is "+str(busiest_day.date())+" in week #"+str(busiest_day.isocalendar()[1])+"."

if __name__ == '__main__':
    main()
