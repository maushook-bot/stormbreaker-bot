"""
CLASS: Add Members to Channel
"""

import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from slack.errors import SlackApiError


class AddMembers:
    def __init__(self):
        # Load environment variables:-
        env_path = Path('./app_config') / '.env'
        load_dotenv(dotenv_path=env_path)

        # Initialize the Slack WebClient:-
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    def add_members(self, channel_id: str, user_id_list: list):
        try:
            self.client.conversations_invite(channel=channel_id, users=user_id_list)
            print('Member: Added')
        except SlackApiError as e:
            logging.error(e.response)