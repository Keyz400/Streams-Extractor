#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6676098160:AAFgh8IZqWubQC-tmO4gYRFkzCbZiXfgYa8")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "27188447"))
    API_HASH = os.environ.get("API_HASH", "42a7205daefacde8e9ba22232deab028")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1318663278").split())
    
