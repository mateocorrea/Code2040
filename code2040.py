__author__ = 'mateocorrea'
import json
import requests

token = 'e559400e1fe8b4dc7febda02e73efc28'
github = 'https://github.com/mateocorrea/Code2040'

def step_1():
    json_dict = {'token': token, 'github':github}
    req = requests.post('http://challenge.code2040.org/api/register', json = json_dict)
    print req.text

def step_2():
    normal = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': token}).text
    reverse = normal[::-1]
    json_dict = {'token': token, 'string': reverse}
    req = requests.post('http://challenge.code2040.org/api/reverse/validate', json = json_dict)
    print req.text

def step_3():
    response = requests.post('http://challenge.code2040.org/api/haystack', data = {'token': token})
    data = json.loads(response.text)
    index = data["haystack"].index(data["needle"])
    json_dict = {'token': token, 'needle': index}
    req = requests.post('http://challenge.code2040.org/api/haystack/validate', json = json_dict)
    print req.text

def step_4():
    response = requests.post('http://challenge.code2040.org/api/prefix', data = {'token': token})
    data = json.loads(response.text)
    len_pre = len(data['prefix'])
    prefix = data['prefix']
    array = [str(x) for x in data['array'] if len(x) >= len_pre and x[:len_pre] != prefix]
    json_dict = {'token': token, 'array': array}
    req = requests.post('http://challenge.code2040.org/api/prefix/validate', json = json_dict)
    print req.text

#Although this code works most times, it doesn't work if the time passes to the next month (or further) (which is not very often with the random
# numbers that the code gives) For example, the final output might say November 33rd, which is obviously wrong. I could fix this, for the specific
# scenario of going from November to December, but in order to have an elegant and robust solution, an external library is needed.
def step_5():
    response = requests.post('http://challenge.code2040.org/api/dating', data = {'token': token})
    data = json.loads(response.text)
    dateinfo = data['datestamp'].split('-')
    day = dateinfo[2][0:2]
    timeinfo = str(dateinfo[2])
    time = timeinfo.split(':')
    hour = time[0][3:5]
    minute = time[1]
    second = time[2][0:2]
    minutes = (int(data['interval']) + int(second)) / 60
    leftover_secs = (data['interval'] + int(second)) % 60
    hours = (minutes + int(minute)) / 60
    leftover_mins = (minutes + int(minute)) % 60
    days = (hours + int(hour)) / 24
    leftover_hours = (hours + int(hour)) % 24
    new_day = int(day) + days
    if new_day < 10:
        new_day = "0" + str(new_day)
    if leftover_hours < 10:
        leftover_hours = "0" + str(leftover_hours)
    if leftover_mins < 10:
        leftover_mins = "0" + str(leftover_mins)
    if leftover_secs < 10:
        leftover_secs = "0" + str(leftover_secs)
    new_datestamp = str(dateinfo[0]) + "-" + str(dateinfo[1]) + "-" + str(new_day) + "T" + str(leftover_hours) + ":" + str(leftover_mins) + ":" + str(leftover_secs) + "Z"
    print data['datestamp']
    print data['interval']
    print new_datestamp
    data2 = {'token': token, 'datestamp': new_datestamp}
    r = requests.post('http://challenge.code2040.org/api/dating/validate', json = data2)
    print r.text



step_5()