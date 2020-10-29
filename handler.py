import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

def wins(event, context):
    year = 2019
    url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html)

    east_soup = soup.find_all('table', {"id": "confs_standings_E"})[0]
    west_soup = soup.find_all('table', {"id": "confs_standings_W"})[0]

    rows = east_soup.findAll('tr')[1:] + west_soup.findAll('tr')[1:]
    team_names = [rows[i].find('th').getText() for i in range(len(rows))]
    team_wins = [rows[i].findAll('td')[0].getText() for i in range(len(rows))]

    team_names = [name.upper().replace(' ', '_').replace('*', '') for name in team_names]
    wins = {team_names[i]: team_wins[i] for i in range(len(team_names))}

    body = wins

    response = {
        "statusCode": 200,
        "headers": {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps(body)
    }

    return response

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "headers": {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """