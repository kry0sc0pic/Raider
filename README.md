# Raider

### A discord bot to delete all channels , roles , custom emojis and ban all members from a discord server. In short raiding a server.

<br>

## *Disclaimer:*
```This is for educational purposes only. Use this only if you have the consent of the server owner. I am not responsible for any damage done by this bot.```

<br>

## Setup
- Make sure you have [Python](https://www.python.org/) and [Git](https://git-scm.com/)
- Create a new app on the [Developer Portal](https://discord.com/developers/applications)
- Download repo using `git clone https://github.com/krishaayjois21/raider.git`

- Open the raider folder 
- Open the `config.json` file
- Copy and paste the code block and fill in necessary details
    - `TOKEN` bot token from the developer page
    - `TRIGGER` Trigger word to initiate deletion
    - `INVITE_LINK` Invite link for the bot with required permissions integer , used to invite bot to the server to be deleted
    - `BAN_MESSAGE` Message used as reason for ban
    - `NEW_NAME` Name the server name has to be edited to be
    - `IMAGE_PATH` Path to the new server icon you want
```json
{
    "TOKEN": "<YOUR-BOT-TOKEN>",
    "TRIGGER": "<TRIGGER-WORD>",
    "INVITE_LINK": "<INVITE-LINK>",
    "BAN_MESSAGE": "<BAN-REASON>",
    "NEW_NAME": "<NEW-SERVER-NAME>",
    "IMAGE_PATH": "<PATH-TO-NEW-LOGO-FILE>"
}
```

## Install Dependencies
### With virtual environment
- Install virtualenv module `pip install virtualenv` (only required for using virtual environments)
- Create a new virtual environment with `virtualenv venv` (optional)
- Activate with `.\venv\Scripts\activate` for windows
- Activate with `source ./venv/bin/activate` for macOS and linux
- Follow Steps for w/o env

### Without virtual environment
- Install dependecies with `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
- Run the bot using `python bot.py` or `python3 bot.py`

## Use the bot
- Invite the bot to the server with the invite link printed out in the console. *Note: This requires you to have the `Manage Server` permissions on the server* 

- Grant all permissions the bot requires or else some operations of the bot may fail

- Find the role for your bot (same as bot username) in `Server Settings >> Roles`

- Move it up to the highest possible position in the role hiearchy

- Give any other necessary roles to the bot to view channels etc.

- Wait for you or anyone else to type the trigger message in any of the channels and let the bot do its work

## Deploying to [Heroku](https://heroku.com)
- Only use this if you want your bot to be online at all times
- In the project folder create a `Procfile` without any file extensions or use the one included
- Open the file and copy the following text: `worker: python bot.py` and paste it in.
- Create a new application on Heroku and follow the steps on the deploy tab.


## License
### [MIT](https://choosealicense.com/licenses/mit/) 

