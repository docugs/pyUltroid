# py-Ultroid Library

Core library of [The Ultroid](https://github.com/docugs/Ultroid), a python based telegram userbot.

[![CodeFactor](https://www.codefactor.io/repository/github/docugs/pyultroid/badge)](https://www.codefactor.io/repository/github/docugs/pyultroid)
[![PyPI - Version](https://img.shields.io/pypi/v/py-Ultroid?style=round)](https://pypi.org/project/py-Ultroid)    
[![PyPI - Downloads](https://img.shields.io/pypi/dm/py-Ultroid?label=DOWNLOADS&style=round)](https://pypi.org/project/py-Ultroid)    
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/docugs/Ultroid/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/docugs/Ultroid)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

# Installation
```bash
pip3 install -U py-Ultroid
```

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-Ultroid-blue)](http://ultroid.tech/)

# Usage
- Create folders named `plugins`, `addons`, `assistant` and `resources`.   
- Add your plugins in the `plugins` folder and others accordingly.   
- Create a `.env` file with following mandatory Environment Variables
   ```
   API_ID
   API_HASH
   SESSION
   REDIS_URI
   REDIS_PASSWORD
   ```
- Check
[`.env.sample`](https://github.com/docugs/Ultroid/blob/main/.env.sample) for more details.   
- Run `python3 -m pyUltroid` to start the bot.   

## Creating plugins
 - ### To work everywhere

```python
@ultroid_cmd(
    pattern="start"
)   
async def _(e):   
    await e.eor("Ultroid Started!")   
```

- ### To work only in groups

```python
@ultroid_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "Ultroid Started.")   
```

- ### Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("Ultroid Started.")   
```

See more working plugins on [the offical repository](https://github.com/docugs/Ultroid)!

> Integrated and improved with 💕 by [@Dr.ugs](https://t.me/doctor_ugs).   

> Credits to the owner of this source code @TeamUltroidDevs