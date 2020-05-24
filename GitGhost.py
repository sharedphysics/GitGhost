#!/usr/bin/env python3
import requests
import json
import os

# curl to get data from your Ghost API.
# Make sure you've create an endpoint and API key in your yourdomain/ghost/#/settings/integrations area!
data = requests.get('[YOUR DOMAIN]/ghost/api/v3/content/posts/?key=[CONTENT API KEY]&include=tags,authors&limit=all')
response_data = data.json() # Makes the .json python-readable

# This will back up the JSON
print (" ... Backing up the full content.json data...") # Tooltip in terminal.
write_json_backup = json.dumps(response_data)
backup_json = open('content.json', 'w+')
backup_json.write(write_json_backup)
backup_json.close()


print (" ... Backing up individual posts:") # Tooltip in terminal.
for item in response_data['posts']: # This defines all the key data we're looking at. For a full list of items to back up, see here: https://ghost.org/docs/api/v3/content/
    post_title = item.get("title")
    post_slug = item.get("slug")
    post_slug_file = post_slug + "/" + post_slug + ".html"
    post_content = item.get("html")
    meta_slug_file = post_slug + "/meta.txt"
    meta_featured = item.get("featured")
    meta_visibility = item.get("visibility")
    meta_created = item.get("created_at")
    meta_updated = item.get("updated_at")
    meta_published = item.get("published_at")
    meta_excerpt = item.get("excerpt")

    print (" ... ... " + post_title) # Terminal tooltip to show what posts are being backed up
    
    # This will create the directories if they don't already exist.
    if not os.path.exists(post_slug):
        os.makedirs(post_slug)
    
    # This will create/write the core content
    backup_post = open(post_slug_file,"w+")
    backup_post.write(post_content)
    backup_post.close()

    # This will create/write the metadata
    backup_meta = open(meta_slug_file,"w+")
    backup_meta.write("Post Title: " + post_title + "\n")
    backup_meta.write("Featured: " + str(meta_featured) + "\n") # Visibility is a boolean so it needs to be processed as str()
    backup_meta.write("Visibility: " + meta_visibility + "\n")
    backup_meta.write("Excerpt: " + meta_excerpt + "\n")
    backup_meta.write("Created At: " + meta_created + "\n")
    backup_meta.write("Published At: " + meta_published + "\n")
    backup_meta.write("Updated At: " + meta_updated + "\n")
    backup_post.close()

'''
####################################
Additional Notes/References:
####################################
ghost endpoints: https://ghost.org/docs/api/v3/content/
curl with python: https://intellipaat.com/community/122/execute-curl-command-within-a-python-script
Set up requests: https://2.python-requests.org/en/master/user/install/#pipenv-install-requests
Complex json: https://www.haykranen.nl/2016/02/13/handling-complex-nested-dicts-in-python/ 
Open directory: https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
Not Scriptable: https://stackoverflow.com/questions/34508981/response-object-is-not-subscriptable-python-http-post-request/34509116
Writing json as a backup: https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python

'''