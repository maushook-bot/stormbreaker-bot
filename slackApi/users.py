"""
CLASS: Get the List of Users using Slack under a Workspace
"""
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from slack.errors import SlackApiError


class Users:
    def __init__(self):
        # Load environment variables:-
        env_path = Path('./app_config') / '.env'
        load_dotenv(dotenv_path=env_path)

        # Initialize the Slack WebClient:-
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
        self.users_store = {}

    def get_users_list(self):
        return self.client.users_list()

    @staticmethod
    def search_user_id(usr_name, user_list):
        print('usr_name => ', usr_name)
        usr_list = []
        # TODO: Get User Id list for Matching name
        for name in usr_name:
            for usr in user_list:
                if usr['name'] == name:
                    print('User: Found!')
                    usr_list.append(usr['id'])
        print('user_id_list => ', usr_list)
        return usr_list

    def save_users(self, users_array):
        for user in users_array:
            user_id = user['id']
            self.users_store[user_id] = user
        print('USERS-LIST => ', self.users_store)