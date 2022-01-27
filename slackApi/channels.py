"""
CLASS: Get the List of Channels in Slack under a Workspace
"""
import slack
import os
from pathlib import Path
from dotenv import load_dotenv


class Channels:
    def __init__(self):
        # Load environment variables:-
        env_path = Path('./app_config') / '.env'
        load_dotenv(dotenv_path=env_path)

        # Initialize the Slack WebClient:-
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
        self.channels_store = {}

    def get_channel_list(self):
        return self.client.conversations_list()

    @staticmethod
    def search_channel_id(channel_name, channel_list):
        # TODO: Get Channel Id for Matching Channel Name
        for ch in channel_list:
            if ch['name'] == channel_name:
                print('Channel: Found!')
                return ch['id']

    def save_channels(self, channel_array):
        for ch in channel_array:
            channel_id = ch['id']
            self.channels_store[channel_id] = ch
        print('CHANNEL-LIST =>', self.channels_store)
        return self.channels_store
