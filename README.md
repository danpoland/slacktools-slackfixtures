# slacktools-slackfixtures

A pytest plugin that adds useful fixtures for testing Slack integrations.

#### Install:
`pip install slacktools-slackfixtures`

#### Example usage:
```python
from myapp.tasks import post_message


def test_post_message(mock_slack):
    response_data = {"status": "OK"}
    slack = mock_slack(path="myapp.tasks.slack", method="chat_postMessage", response_data=response_data)
    response = post_message()

    slack.chat_postMessage.assert_called_once()
    assert response.data == response_data
```

#### Test for failure:

```python
import pytest
from slack.errors import SlackApiError

from myapp.tasks import post_message


def test_post_message_failure(mock_slack):
    response_data = {"status": "Not OK"}
    slack = mock_slack(
        path="myapp.tasks.slack",
        method="chat_postMessage", 
        response_data=response_data, 
        validates=False
    )
    response = post_message()

    with pytest.raises(SlackApiError):
        response.validate()
```
