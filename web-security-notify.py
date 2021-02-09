#!/usr/bin/env python3

import json
import time
import requests
import schedule

last_category_id = 20

telegram_chat_id = "*REDACTED*"
telegram_token = "*REDACTED*"
telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&disable_web_page_preview=0&parse_mode=html&text="


def get_all_categories():
    response = requests.get(
        "https://portswigger.net/web-security/hall-of-fame/categories"
    )
    return response.json()


def send_telegram_message(msg):
    response = requests.get(f"{telegram_url}{msg}")
    # print(response.text)


def check_new_categories():
    global last_category_id
    json_categories = get_all_categories()

    if len(json_categories) > last_category_id:
        last_category_id = last_category_id + 1
        for category in json_categories:
            if category.get("Id") == last_category_id:
                print(f"[{last_category_id}] New one: {category['DisplayName']}")
                new_category_name = f"{category['DisplayName']}"
                new_category_url = (
                    f"https://portswigger.net/web-security/{category['Url']}"
                )
                msg = f"<b>{new_category_name}</b>%0A{new_category_url}"
                send_telegram_message(msg)
    else:
        print(f"[{last_category_id}] No new categories :(")


schedule.every().hour.do(check_new_categories)

while True:
    schedule.run_pending()
    time.sleep(1)
