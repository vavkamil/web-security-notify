# web-security-notify.py
Telegram bot to notify me about new [Web Security Academy](https://portswigger.net/web-security) labs

---

### Example

![PoC](/screenshot.png?raw=true "PoC")

---

### Usage

Run is the *screen*, or modify the script to use *cron*

```
$ screen -S web-security-notify
$ python web-security-notify.py
$ Ctrl-a + d
```

---

### Settings

Change ID of the last **Web Security Academy** topic

```
# last_category_id = 19
```

Change [schedule](https://schedule.readthedocs.io/en/stable/examples.html) interval
```
# schedule.every(10).seconds.do(check_new_categories)
# schedule.every(10).minutes.do(check_new_categories)
# schedule.every().hour.do(check_new_categories)
```

---

### Installation

`$ pip3 install -r requirements.txt`

1) On Telegram, contact [@BotFather](https://telegram.me/botfather), send him a "/start" message
2) Send another "/newbot" message, then follow the instructions
3) Replace "telegram_token" with your API token
4) On Telegram, contact [@userinfobot](https://t.me/userinfobot), send him a "/start" message
5) Replace "telegram_chat_id" with your ID
