import requests
from collections import Counter, defaultdict
from Config.config import TestData


def get_filter_data(self):
    client = requests.Session()
    all_players_data = {}
    data_all = []  # get list of objects with id, gender, username
    for i in range(0, 6):
        r = client.post('https://localhost/api/players/find', data={"page": i + 1, "type": "all"}, verify=False)
        players_all = r.json()["players"]["data"]
        for j in range(len(players_all)):
            id = players_all[j]["id"]
            all_players_data["id"] = id
            username = players_all[j]["profile"]["username"]
            all_players_data["username"] = username
            gender = players_all[j]["profile"]["gender"]
            all_players_data["gender"] = gender
            data_all.append({
                "id": all_players_data["id"],
                "username": all_players_data["username"],
                "gender": all_players_data["gender"]
            })
    return data_all

def get_user_video_info(self, user_id):
    payload = {
        "id" : user_id,
        "page" : 1
    }
    response = requests.post(TestData.BASE_URL + "api/videos/user/" + str(user_id), data=payload, verify=False)
    return (response.json())

def get_user_id(self, username):
    client = requests.Session()
    payload = {
        "username": username
    }
    response = client.post(TestData.BASE_URL + 'api/players/get', data=payload, verify=False)
    print(response.json()["player"]["id"])
    return response.json()["player"]["id"]

def get_followers_ids(self, fb_cookie):
    cookie = { "fb_session": fb_cookie }
    id_notifications = []
    r = requests.get(TestData.BASE_URL + 'auth/init', cookies=cookie, verify=False)
    for i in range(len(r.json()["notifications"]["list"])):
        try:
            notification_mode = (r.json()["notifications"]["list"][i]["data"]["mode"])
            if notification_mode == "follow":
                follower_id = (r.json()["notifications"]["list"][i]["data"]["user_id"])
                id_notifications.append(follower_id)
        except KeyError:
            print("No such key")
    return id_notifications

def new_players_all(self): # returns username and last_name in key:value pair
    response = requests.post(TestData.BASE_URL + "api/app/present", verify=False)
    new_users = (response.json()["users"]["new"])
    new_users_list = {}
    for i in range(len(new_users)):
        username = (new_users[i]["username"])
        lastName = (new_users[i]["profile"]["lastName"])
        new_users_list[username] = lastName
    return new_users_list

def all_videos(self):
    payload = {
        "filters":{},
        "page": 1,
        "type": "all"
    }
    response = requests.post(TestData.BASE_URL + "api/videos/find", data=payload, verify=False)
    total_active_videos = response.json()["videos"]["total"]
    return total_active_videos
