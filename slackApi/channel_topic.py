"""
CLASS: SET CHANNEL TOPIC
"""

import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from slack.errors import SlackApiError


class ChannelTopic:
    def __init__(self):
        # Load environment variables:-
        env_path = Path('./app_config') / '.env'
        load_dotenv(dotenv_path=env_path)

        # Initialize the Slack WebClient:-
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    def set_public_channel_topic(self, channel_id, topic):
        # TODO: Set public channel Topic:-
        try:
            self.client.conversations_setTopic(channel=channel_id, topic=topic)
            print('Channel Topic: SET')
        except SlackApiError as e:
            logging.error(e.response)