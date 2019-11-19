import os
import slack

def list_channels(slack_client):
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

token = '<your_slack_token>'
client = slack.WebClient(token=token)
for l in list_channels(client):
    message = "Hello to channel " + str(l["name"])
    print(message)
    client.chat_postMessage(
    channel=l["id"],
    text=message
    )
   