import json, sys, csv, operator
from datetime import datetime

result = {}

def extract_data_to_tsv(commits):
    json_commits = json.loads(commits)
    for commit in json_commits:
        date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
        day = date_object.isoweekday()
        hour = date_object.hour
        if hour == 0:
            hour = 24
        result[(day, hour)] += 1

def main():
    commit_file = open(sys.argv[1])
    for day in range(1,8):
        for hour in range(1,25):
            result[(day, hour)] = 0
    for line in commit_file:
    	extract_data_to_tsv(line)
    # Write CSV file
    myfile = open('data.tsv', 'wb')
    wr = csv.writer(myfile, delimiter='\t')
    wr.writerow(['day', 'hour', 'value'])
    for time in result.keys():
        mylist = [time[0], time[1], result[time]]
        wr.writerow(mylist)

if __name__ == '__main__':
    main()