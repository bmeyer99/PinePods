import requests

def call_clean_expired_sessions(url, headers):
    print(f'in clean expired call {headers}')
    response = requests.post(url + "/clean_expired_sessions/", headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error calling clean_expired_sessions:", response.status_code)

def call_check_saved_session(url, headers):
    response = requests.get(url + "/check_saved_session/", headers=headers)
    if response.status_code == 200:
        user_id = response.json()
        print("User ID:", user_id)
        return user_id
    else:
        print("No saved session found")

def call_guest_status(url, headers):
    response = requests.get(url + "/guest_status", headers=headers)
    if response.status_code == 200:
        is_active = response.json()
        print("Guest status:", is_active)
        return is_active
    else:
        print("Error fetching guest status:", response.status_code)
        return None

def call_get_user_details(url, headers, username):
    response = requests.get(url + f"/user_details/{username}", headers=headers)
    if response.status_code == 200:
        user_details = response.json()
        print("User details:", user_details)
        return user_details
    else:
        print("Error fetching user details:", response.status_code)
        return None

def call_get_user_details_id(url, headers, user_id):
    response = requests.get(url + f"/user_details_id/{user_id}", headers=headers)
    if response.status_code == 200:
        user_details = response.json()
        print("User details:", user_details)
        return user_details
    else:
        print("Error fetching user details:", response.status_code)
        return None


def call_create_session(url, headers, user_id):
    response = requests.post(url + f"/create_session/{user_id}", headers=headers)
    if response.status_code == 200:
        print("Session created successfully")
    else:
        print("Error creating session:", response.status_code)

def call_verify_password(url, headers, username, password):
    response = requests.post(url + "/verify_password/", json={"username": username, "password": password}, headers=headers)
    if response.status_code == 200:
        is_password_valid = response.json()["is_password_valid"]
        print("Is password valid:", is_password_valid)
        return is_password_valid
    else:
        print("Error verifying password:", response.status_code)
        return None


def call_return_episodes(url, headers, user_id):
    response = requests.get(url + f"/return_episodes/{user_id}", headers=headers)
    if response.status_code == 200:
        episodes = response.json()["episodes"]
        if episodes:
            print("Episodes:", episodes)
        else:
            print("No episodes found.")
            return None
        return episodes
    else:
        print("Error fetching episodes:", response.status_code)
        return None


def call_check_episode_playback(url, headers, user_id, episode_title, episode_url):
    payload = {
        "user_id": user_id,
        "episode_title": episode_title,
        "episode_url": episode_url
    }
    response = requests.post(url + "/check_episode_playback", json=payload, headers=headers)
    if response.status_code == 200:
        playback_data = response.json()
        print("Playback data:", playback_data)
        return playback_data
    else:
        print("Error checking episode playback:", response.status_code)
        return None

def call_get_user_details_id(url, headers, user_id):
    response = requests.get(url + f"/user_details_id/{user_id}", headers=headers)
    if response.status_code == 200:
        user_details = response.json()
        print("User details:", user_details)
        return user_details
    else:
        print("Error fetching user details:", response.status_code)
        return None

def call_get_theme(url, headers, user_id):
    response = requests.get(url + f"/get_theme/{user_id}", headers=headers)
    if response.status_code == 200:
        theme = response.json()["theme"]
        print("Theme:", theme)
        return theme
    else:
        print("Error fetching theme:", response.status_code)
        return None

def call_add_podcast(url, headers, podcast_values, user_id):
    response = requests.post(url + "/add_podcast", headers=headers, json={"podcast_values": podcast_values, "user_id": user_id})
    if response.status_code == 200:
        success = response.json()["success"]
        if success:
            print("Podcast added successfully")
            return True
        else:
            print("Podcast already exists for the user")
            return False
    else:
        print("Error adding podcast:", response.status_code)
        return None

def call_enable_disable_guest(url, headers):
    response = requests.post(url + "/enable_disable_guest", headers=headers)
    if response.status_code == 200:
        success = response.json()["success"]
        if success:
            print("Guest account status changed successfully")
            return True
        else:
            print("Error changing guest account status")
            return False
    else:
        print("Error changing guest account status:", response.status_code)
        return None

def call_enable_disable_self_service(url, headers):
    response = requests.post(url + "/enable_disable_self_service", headers=headers)
    if response.status_code == 200:
        success = response.json()["success"]
        if success:
            print("Self-service status changed successfully")
            return True
        else:
            print("Error changing self-service status")
            return False
    else:
        print("Error changing self-service status:", response.status_code)
        return None

def call_self_service_status(url, headers):
    response = requests.get(url + "/self_service_status", headers=headers)
    if response.status_code == 200:
        status = response.json()["status"]
        print(f'status should be 0 1 or true false: {status}')
        return status
    else:
        print("Error fetching self-service status:", response.status_code)
        return None

def call_increment_listen_time(url, headers, user_id):
    response = requests.put(url + f"/increment_listen_time/{user_id}", headers=headers)
    if response.status_code == 200:
        print("Listen time incremented.")
    else:
        print("Error incrementing listen time:", response.status_code)

def call_increment_played(url, headers, user_id):
    response = requests.put(url + f"/increment_played/{user_id}", headers=headers)
    if response.status_code == 200:
        print("Played count incremented.")
    else:
        print("Error incrementing played count:", response.status_code)

def call_record_podcast_history(url, headers, episode_title, user_id, episode_pos):
    data = {
        "episode_title": episode_title,
        "user_id": user_id,
        "episode_pos": episode_pos,
    }
    response = requests.post(url + f"/record_podcast_history", headers=headers, json=data)
    if response.status_code == 200:
        print("Podcast history recorded.")
    else:
        print("Error recording podcast history:", response.status_code)

def call_download_podcast(url, headers, episode_url, title, user_id):
    data = {
        "episode_url": episode_url,
        "title": title,
        "user_id": user_id,
    }
    response = requests.post(url + f"/download_podcast", headers=headers, json=data)
    if response.status_code == 200:
        print("Podcast downloaded.")
        return True
    else:
        print("Error downloading podcast:", response.status_code)
        return False

def call_delete_podcast(url, headers, episode_url, title, user_id):
    data = {
        "episode_url": episode_url,
        "title": title,
        "user_id": user_id,
    }
    response = requests.post(url + f"/delete_podcast", headers=headers, json=data)
    if response.status_code == 200:
        print("Podcast deleted.")
    else:
        print("Error deleting podcast:", response.status_code)

def call_save_episode(url, headers, episode_url, title, user_id):
    data = {
        "episode_url": episode_url,
        "title": title,
        "user_id": user_id,
    }
    response = requests.post(url + f"/save_episode", headers=headers, json=data)
    if response.status_code == 200:
        print("Episode saved.")
    else:
        print("Error saving episode:", response.status_code)

def call_remove_saved_episode(url, headers, episode_url, title, user_id):
    data = {
        "episode_url": episode_url,
        "title": title,
        "user_id": user_id,
    }
    response = requests.post(url + f"/remove_saved_episode", headers=headers, json=data)
    if response.status_code == 200:
        print("Saved episode removed.")
    else:
        print("Error removing saved episode:", response.status_code)

def call_record_listen_duration(url, headers, episode_url, title, user_id, listen_duration):
    data = {
        "episode_url": episode_url,
        "title": title,
        "user_id": user_id,
        "listen_duration": listen_duration
    }
    response = requests.post(url + f"/record_listen_duration", headers=headers, json=data)
    if response.status_code == 200:
        print("Listen duration recorded.")
    else:
        print("Error recording listen duration:", response.status_code)

def call_refresh_pods(url, headers):
    response = requests.get(url + f"/refresh_pods", headers=headers)
    if response.status_code == 200:
        print("Podcasts refreshed.")
    else:
        print("Error refreshing podcasts:", response.status_code)

def call_get_stats(url, headers, user_id):
    response = requests.get(url + f"/get_stats?user_id={user_id}", headers=headers)
    if response.status_code == 200:
        stats = response.json()
        return stats
    else:
        print("Error getting stats:", response.status_code)
        return None

def call_get_user_episode_count(url, headers, user_id):
    response = requests.get(url + f"/get_user_episode_count?user_id={user_id}", headers=headers)
    if response.status_code == 200:
        episode_count = response.json()
        return episode_count
    else:
        print("Error getting user episode count:", response.status_code)
        return None

def call_get_user_info(url, headers):
    response = requests.get(url + "/get_user_info", headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print("Error getting user information:", response.status_code)
        return None

def call_check_podcast(url, headers, user_id, podcast_name):
    data = {"user_id": user_id, "podcast_name": podcast_name}
    response = requests.post(url + "/check_podcast", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["exists"]
    else:
        print("Error checking podcast:", response.status_code)
        return False

