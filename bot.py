import os
import time
import re
from slackclient import SlackClient

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACKBOTTOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None


