# Last.fm scrobbler userbot for Telegram

This is a userbot (described better as an *account automation*) for **Telegram accounts** which will scrobble currently playing songs scrobbled from a linked **last.fm** account.

#### Installation & Requirements
- Python 3
- Installing the required libs with `pip install -r requirements.txt`
- You will need to put your [Telegram API Keys and hash](https://my.telegram.org/auth) in the two fields specified in `main.py`.
- You will need to put your [last.fm API key and username](https://www.last.fm/api) in the two fields specified in `Scrobbler.py`.

#### Usage
There are *two* main commands that can be used:

- `-np` command shows the *currently* playing track that is being scrobbled on last.fm as a message, or a placeholder if nothing is currently being played.
- `-scrobble` command is used to toggle dynamic scrobbling **on the profile**, using a mute sound with as title the name of the track that is currently playing or a placeholder if nothing is playing at the moment.


*Made using [Kurigram](https://github.com/KurimuzonAkuma/kurigram) and [lastfm-py](https://pypi.org/project/lastfm-py/)*. 