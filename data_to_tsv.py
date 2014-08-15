import json, sys, csv, operator
from datetime import datetime

day_hour = {}
weekday = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

def extract_data_to_tsv(commits):
    json_commits = json.loads(commits)
    for commit in json_commits:
        date_object = datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ')
        day = date_object.isoweekday()
        hour = date_object.hour
        str_day = date_object.strftime('%A')

        if hour == 0:
            hour = 24
        day_hour[(day, hour)] += 1
        weekday[str_day] += 1

def main():
    commit_file = open(sys.argv[1])
    # Initialize dicts
    for day in range(1,8):
        for hour in range(1,25):
            day_hour[(day, hour)] = 0
    # Fill dicts
    for line in commit_file:
    	extract_data_to_tsv(line)

    # Write CSV files
    day_hour_file = open('commit_heatmap.tsv', 'wb')
    weekday_file = open('commit_per_weekday.tsv', 'wb')

    wr1 = csv.writer(day_hour_file, delimiter='\t')
    wr2 = csv.writer(weekday_file, delimiter='\t')

    wr1.writerow(['day', 'hour', 'value'])
    wr2.writerow(['day', 'value'])

    for time in day_hour.keys():
        mylist = [time[0], time[1], day_hour[time]]
        wr1.writerow(mylist)
    for day in weekday.keys():
        mylist = [day, weekday[day]]
        wr2.writerow(mylist)

if __name__ == '__main__':
    main()