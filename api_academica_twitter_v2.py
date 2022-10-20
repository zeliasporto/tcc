import requests
import os
import json
import time
import datetime

from config_fas import *

endpoint = "https://api.twitter.com/2/tweets/search/all"

params = {
    'query': query,
    'expansions': 'author_id,referenced_tweets.id,geo.place_id,in_reply_to_user_id,referenced_tweets.id.author_id',
    'tweet.fields': 'created_at,author_id,lang,entities,geo,referenced_tweets,in_reply_to_user_id,public_metrics', 
    'user.fields': 'username,location,public_metrics,verified',
    
    
    'start_time': start_time,
    'end_time': end_time,
    'max_results': max_results,
    
}



headers = {"Authorization": "Bearer {}".format(bearer_token)}



num_request = 0
print('Arquivo gravado ' + str(num_request) )
# get next_token


directory = sys.argv[3:4][0]

try: 
  os.mkdir(directory) 
except OSError as error: 
  print(error)  
 

json_response = ""

print("Getting tweets")
response = requests.request("GET", endpoint, headers=headers, params=params)
json_response = response.json()

num_request = 1
with open(directory + "/tweet2019.2_"+ str(num_request) + ".json", "w", encoding="utf-8") as f:
  json.dump(json_response, f)


# def handle15MinOfReqs():  
while 'next_token' in json_response['meta']:
  start = time.time()

  if num_request % 300 == 0:
    print("300 requests done")

  
  next_token = json_response['meta']['next_token']
  params['next_token'] = next_token # add pagination key to query dict
  response = requests.request("GET", endpoint, headers=headers, params=params)
  if response.status_code != 200:
    print('Erro no indice ' + str(num_request))
    print(response.status_code)
    print(response.text)
  else:
    json_response = response.json()
    file_name = directory + "/tweet2019.2_"+ str(num_request) + ".json"
    with open(file_name, "w", encoding="utf-8") as f:
      json.dump(json_response, f)
    print('Saving content in the file ' file_name)
    num_request = num_request +1

  end = time.time()
  elapsed_time = end - start
  remaining_time = max(0, 3.5 - elapsed_time)
  print("Sleeping " + str(remaining_time) + " seconds. ZzzZzZz")
  time.sleep(remaining_time)
    
print('fim')