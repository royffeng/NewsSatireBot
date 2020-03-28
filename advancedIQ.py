import praw
import json
import time
import os

#reddit api login credentials
reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username = 'AdvancedIQ',
                     password = 'AdvancedIQ',
                     user_agent = '')
