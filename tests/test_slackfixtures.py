import pytest
from slack.errors import SlackApiError

from tests.examples import post_message


def test_post_message(mock_slack):
    response_data = {"status": "OK"}
    slack = mock_slack(
        path="tests.examples.slack",
        method="chat_postMessage",
        response_data=response_data,
    )
    response = post_message()
    response.validate()

    slack.chat_postMessage.assert_called_once_with(channel="#general", blocks=[])
    assert response.data == response_data


def test_post_message_failure(mock_slack):
    response_data = {"status": "Not OK"}
    mock_slack(
        path="tests.examples.slack",
        method="chat_postMessage",
        response_data=response_data,
        validates=False,
    )
    response = post_message()

    with pytest.raises(SlackApiError):
        response.validate()
