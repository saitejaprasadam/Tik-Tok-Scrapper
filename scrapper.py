from api import Api
from time import sleep
import sys
import os
import requests
import os.path
from helper import Helper

helperObject = Helper()

if __name__ == "__main__":

    users = [
        ("User Name (For Directory Name)", user_id),
        ("User Name (For Directory Name)", user_id),
        ("User Name (For Directory Name)", user_id)
    ]

    for name, id in users:

        print("Fetching " + name + " Posts")
        api = Api()
        count = 0
        cursor = 0
        fetched = 0
        
        if not os.path.exists(name + "/"):
            os.makedirs(name + "/")

        while True:

            data = api.user_video_list(user_id=id, cursor=cursor)

            if 'max_cursor' not in data:
                break

            cursor = data['max_cursor']
            videos = data['aweme_list']

            for video in videos:
                title = video['desc'].replace("/", "").replace("?", "").replace("\n", " ")

                if title is not "":
                    title = title + " - "

                title = title + str(video['aweme_id'])
                url = video['video']['download_addr']['url_list'][0]

                count = count + 1
                sys.stdout.write("\rFetched " + str(count) + " Posts")
                sys.stdout.flush()

                if os.path.isfile(name + "/" + title + ".mp4"):
                    continue

                fetched = fetched + 1
                file = open(name + "/" + title + ".mp4", 'wb')
                url = helperObject.request_post(url).url
                file.write(helperObject.request_get(url).content)
                file.close()



        print("\nNew Content Fetched: " + str(fetched) + "\n")
