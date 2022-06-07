"""
CLASS: CREATE PUBLIC CHANNELS
"""

import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from slack.errors import SlackApiError


class CreateChannel:
    def __init__(self):
        # Load environment variables:-
        env_path = Path('./app_config') / '.env'
        load_dotenv(dotenv_path=env_path)

        # Initialize the Slack WebClient:-
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    def create_public_channel(self, channel_name: str):
        # TODO: Create a new public channel:-
        try:
            self.client.conversations_create(name=channel_name)
            print("Channel created: Success")
        except SlackApiError as e:
            logging.error(e.response)
