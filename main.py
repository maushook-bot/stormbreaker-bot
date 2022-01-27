"""
SLACK BOT: CLIENT AUTOMATION TESTING APPLICATION
Name: Bi-frost
Phase: Beta
version: 0.1
workspace: Neural Bots
"""

# Import the Packages:-
from slackApi.add_members import AddMembers
from slackApi.channel_topic import ChannelTopic
from slackApi.channels import Channels
from slackApi.create_channel import CreateChannel
from slackApi.users import Users
from app_config.data_injector import DataInjection

if __name__ == '__main__':
    # Instantiate the Class Objects:-
    di = DataInjection()
    cc = CreateChannel()
    usr = Users()
    ch = Channels()
    ct = ChannelTopic()
    am = AddMembers()

    # TODO: Get Setting.json loaded:-
    print('Resource => ', di.get_resource())
    data = di.get_resource()

    # TODO: CREATE PUBLIC SLACK CHANNELS:-
    cc.create_public_channel(channel_name=data['channel_name'])

    # TODO: SET Channel Topic:-
    channel_list = ch.get_channel_list()
    print(channel_list['channels'])
    channel_id = ch.search_channel_id(data['channel_name'], channel_list['channels'])
    print('channel-id => ', channel_id)
    ct.set_public_channel_topic(channel_id, data['channel_topic'])

    # TODO: Add Members to Channel:-d
    user_list = usr.get_users_list()
    print('User-list: ', user_list)
    user_id_list: list = usr.search_user_id(usr_name=data['channel_members'], user_list=user_list['members'])
    am.add_members(channel_id, user_id_list)

