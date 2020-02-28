from typing import Dict, List

import slack


def post_message():
    client = slack.WebClient(token="some-token-value")
    return client.chat_postMessage(channel="#general", blocks=[])
