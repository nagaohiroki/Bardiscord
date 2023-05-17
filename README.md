# Bardiscord

this is a Bard Discrod Bot

## Bard Authentication
Go to https://bard.google.com/  

* F12 for console
* Copy the values
** Session: Go to Application ¨ Cookies ¨ __Secure-1PSID. Copy the value of that cookie.

## Discrod Setting(enable Intents)

https://discordpy.readthedocs.io/ja/latest/discord.html

MyApplications -> SETTINGS/Bot -> Privileged Gateway Intents  
[PRESENCE INTENT]  
[SERVER MEMBERS INTENT]  
[MESSAGE CONTENT INTENT]  


## Server Setting

replace your-discord-token and your-[__Secure-1PSID]  

```
git clone 
SETX /M BARD_DISCORD_TOKEN "your-discord-token"
SETX /M BARD_TOKEN "your-[__Secure-1PSID]"
python -m pip install -r requirements.txt
python main.py
```