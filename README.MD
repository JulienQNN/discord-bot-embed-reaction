<div align ="center">
<h1>discord-bot-embed-reaction</h1>

[![Python](https://img.shields.io/badge/-PYTHON%203.10-yellow?style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![Discord.py 2.0](https://img.shields.io/badge/-discord.py%202.0-9cf?style=for-the-badge&logo=discord)](https://github.com/Rapptz/discord.py)
[![GitHub forks](https://img.shields.io/github/forks/JulienQHN/discord-bot-embed-reaction?style=for-the-badge)](https://github.com/JulienQHN/discord-bot-embed-reaction/network)
[![GitHub stars](https://img.shields.io/github/stars/JulienQHN/discord-bot-embed-reaction?style=for-the-badge)](https://github.com/JulienQHN/discord-bot-embed-reaction/stargazers)
[![GitHub license](https://img.shields.io/github/license/JulienQHN/discord-bot-embed-reaction?style=for-the-badge)](https://github.com/JulienQHN/discord-bot-embed-reaction)

<h2>An easy to use system for your discord server !</h2>

This repository is a Python project based on <a href="https://github.com/Rapptz/discord.py">Discord.py 2.0</a>, it will run a discord bot to send vouchers (or anything else) to users using the reactions of a pre-defined <img align="top" width="25" height="25" src="https://cdn.rawgit.com/NNTin/discord-logo/f4333344/src/assets/animateddiscord.svg"> embed or message. This project is <b>extremely customizable and just waiting for your ideas and creativity</b>, feel free to browse the excellent <a href="https://discordpy.readthedocs.io/en/latest/index.html">documentation</a> and join the official discord.py server ! <a href="https://discord.gg/r3sSKJJ"><img align="top" src="https://discord.com/api/guilds/336642139381301249/embed.png"></img></a>

</div>

## Features

- Bot reacts according to precise reaction
- Restriction based on discord roles
- Bot sends private messages in the form of an fully customizable discord embed
- Using the new buttons

## Installing

### Requirements

- <a href="https://www.python.org/downloads/">Python 3.8</a> or higher, to use Python !
- <a href="https://github.com/Rapptz/discord.py">Discord.py 2.0</a> :warning: if you already have an old discord.py version (like the `1.7.3` version) you need to uninstall it first with : `pip uninstall discord`

<a>Install the Discord.py 2.0 library :</a>

```
git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .[voice]
```

<a>Install this repository :</a>

```
git clone git@github.com:JulienQHN/discord-bot-embed-reaction.git
$ cd discord-bot-embed-reaction
$ python3 -m pip install -U .[voice]
```

- <a href="https://pypi.org/project/python-dotenv/">Dotenv</a> package to load environnements variables `pip install python-dotenv`

## First implementation

### Fill `.env`

- Rename `.env.example` file to `.env` to make it usable.
- Fill `DISCORD_TOKEN="YOUR TOKEN"` with your bot token, you can create one on your <a href="https://discord.com/developers/applications">discord developer portal</a>, if needed a step by step wiki is <a href="https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token"> available here</a>, don't forget to enable the <b>Privileged Gateway Intents</b> in the bot category on your <a href="https://discord.com/developers/applications">discord developer portal</a> and <b>invite your bot</b> on your discord server !
- Fill `CHANNEL_ID = 999999999999999999` by replacing the 18 digit number with the desired channel id where your embed will arrive. You can find it by <b>right clicking on it</b> in the channel list of a discord server.
<div align="center">
<a><img width="143"  src="https://i.ibb.co/XbMyB1k/Capture-d-cran-2022-05-10-102345.png" alt="Capture-d-cran-2022-05-10-102345" border="0"> <img src="https://i.ibb.co/j4zPjKx/Capture-d-cran-2022-05-10-103800.png" alt="Capture-d-cran-2022-05-10-102345" border="0"></a>
<a></a>
</div>

### Fill `helpers.py` (Optional)

- Customize the different options of embeds, styles, role restrictions and more. Everything is explained in comments in the file.

### Start `setup.py`

At the root of the project :

```
$ python3 setup.py
```

If everything worked correctly you should receive a message in the channel you have chosen like on the GIF below !

<div align="center">
<img width="357" height="255" src="https://s8.gifyu.com/images/discord-bot-embed-reaction.gif" alt="discord-bot-embed-reaction.gif" border="0" />
<img width="357" height="255" src="https://i.ibb.co/ws5jn5w/Capture-d-cran-2022-05-10-113216.png" border="0" />
</div>

### Fill again `.env` file

- Fill `MESSAGE_ID = 999999999999999999` by replacing the 18 digit number with the created message id. You can find it by <b>right clicking on it</b> as in the picture above.

### Start `main.py`

At the root of the project :

```
$ python3 main.py
```

If everything worked correctly, the bot should react and send a message to users that adds a reaction to the message you defined earlier. Don't forget to populate your `vouchers.json` file with a list of vouchers or any other data ! The GIF below show you what this code does with the basic parameters, customize them as you wish !

<div align="center">
<img width="357" height="255" src="https://s8.gifyu.com/images/22e0e195205d81752.gif" alt="22e0e195205d81752.gif" border="0" /></img>
<img width="357" height="255" src="https://i.ibb.co/Sssr0P7/Capture-d-cran-2022-05-10-115335.png" border="0" /></img>
</div>

## License

Licensed under the terms of the MIT License.
