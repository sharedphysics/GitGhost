# GitGhost
GitGhost is a python/shell script lets you automate git-based .html backups of your Ghost CMS content and metadata.

I created GitGhost after noticing that a lapsed card on my AWS account meant that my entire Ghost installation was almost erased. My server-based backups would have been erased too, which drove home the need for 3rd-party backups.

# Getting Started
GitGhost works by accessing your Ghost API to pull down JSON content, then iterating through that content to create a browsable directory with .html files. It also creates a full .json backup for you to manipulate later if needed.

### Create a Custom API
In the `Custom Integrations` area (yourdomain/ghost/#/settings/integrations), click on `+ add a custom integration` and give it a name. 

Copy the Content API Key and the API URL. 

### Set Up the Python Script
1. In `GitGhost.py` line 6, set your request.get() url to be: `[YOUR DOMAIN]/ghost/api/v3/content/posts/?key=[CONTENT API KEY]&include=tags,authors&limit=all' `

2. GitGhost has a few dependencies. Run `pip install -r requirements.txt` in your GitGhost directory to set them up.

3. If you want to configure what metadata is being written, you can adjust it from available variables here: (https://ghost.org/docs/api/v3/content/)

### Running the Script Locally
To run the script one time & save locally, type the following in your GitGhost directory:
```python3 GitGhost.py```

### Running & Committing to GitHub
To run the script & commit to github, clone this GitGhost repo & give it a new name. I recommend [YOURSITE-Backups] because that will make it super clear what you're pushing to.

Copy/open the new repo to your computer and `cd` into it.

Make the automate.sh script actionable by typing:
```chmod +x automate.sh```
Then run the script as `./automate.sh`

# Coming Soon
* Update API URL with variables
* Create folder structure for scripts/published posts/draft posts
* Write a full backup `backup.json` for full restores
* Pull down and save actual images from post
* Pull down drafts as well
* Pull down 
* Writing more metadata from posts.
* Writing settings as a backup.
* Creating a .html index to navigate your posts locally, because why not?