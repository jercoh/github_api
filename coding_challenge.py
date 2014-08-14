import json, sys
import operator
from datetime import datetime

week_commits = {}

def get_busiest_week(commits):
	json_commits = json.loads(commits)
	print len(json_commits)
	for commit in json_commits:
		date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
		if date_object.year == 2014:
			week = date_object.isocalendar()[1]
			if week not in week_commits:
				week_commits[week] = 1
			else:
				week_commits[week] += 1
	busiest_week = max(week_commits.iteritems(), key=operator.itemgetter(1))[0]
	return busiest_week

def main():
    commit_file = open(sys.argv[1]).read()
    print get_busiest_week(commit_file)

if __name__ == '__main__':
    main()
