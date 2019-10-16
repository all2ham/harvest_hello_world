import os
import json
import urllib.request
import requests
from datetime import datetime, date, timedelta


HARVEST_ACCOUNT_ID = #####
HARVEST_ACCESS_TOKEN = #####

USERS_ME_URL = "https://api.harvestapp.com/v2/users/me"
TIME_ENTRIES_URL = "https://api.harvestapp.com/v2/time_entries"

headers = {
    "User-Agent": ####,
    "Authorization": "Bearer " + HARVEST_ACCESS_TOKEN,
    "Harvest-Account-ID": HARVEST_ACCOUNT_ID,
    "Content-Type": "application/json"
}

request = urllib.request.Request(url=USERS_ME_URL, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)

print(json.dumps(jsonResponse, sort_keys=True, indent=4))

# add tasks
sis_rnd = {
    "project_id": ##########,
    "task_id": ###########,
    "spent_date": "2000-01-01",
    "hours": 1
}

admin = {
    "project_id": ########,
    "task_id": ##########,
    "spent_date": "2000-01-01",
    "hours": 1
}


def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr, min(curr + delta, end)
        curr += delta

for s, e in perdelta(datetime(2019, 4, 1), datetime(2019, 12, 20), timedelta(days=1)):
    if s.weekday() not in (5,6):
        print(s)
        sis_rnd.update({"spent_date": str(s)[:10], "hours":7})
        admin.update({"spent_date": str(s)[:10]})
        print(sis_rnd)
        print(admin)
        r = requests.post(TIME_ENTRIES_URL, headers=headers, data=json.dumps(sis_rnd))
        print(r.content.decode())
        r = requests.post(TIME_ENTRIES_URL, headers=headers, data=json.dumps(admin))
        print(r.content.decode())
