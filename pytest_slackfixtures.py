import pytest
from slack.errors import SlackApiError

__all__ = ("slack_api_error", "patch_slack_client", "make_slack_response", "mock_slack")


@pytest.fixture
def slack_api_error(mocker):
    return SlackApiError("Failed Slack call", mocker.Mock())


@pytest.fixture
def patch_slack_client(mocker):
    """Patch the slack module with the provided Mock object."""

    def _make_slack_client(mock_client, path):
        """
        :param mock_client: The Mock object to use in place of the Slack client.
        :param path: The dot path to where the slack module should be patched.
        """
        mocker.patch(path, mocker.Mock(**{"WebClient.return_value": mock_client}))

    return _make_slack_client


@pytest.fixture
def make_slack_response(mocker, slack_api_error):
    """Used to construct a mock response from Slack."""

    def _make_slack_response(data: dict, validates=True):
        """
        :param data: The data to be returned with the response.
        :param validates: If the response should valid successfully or not.
        """

        def side_effect():
            if validates:
                return True
            raise slack_api_error

        mock_response = mocker.MagicMock(**{"validate.side_effect": side_effect})
        mock_response.__getitem__.side_effect = lambda key: data[key]
        type(mock_response).data = mocker.PropertyMock(return_value=data)

        return mock_response

    return _make_slack_response


@pytest.fixture
def mock_slack(mocker, patch_slack_client, make_slack_response):
    """
    Constructs a mock Slack client with a pre-configured response to the specified `method`
    and patches it at the target `path`.
    """

    def _mock_slack(path, method=None, response_data=None, validates=True):
        """
        :param path: The dot path to where the client should be patched.
        :param method: The Slack WebClient method to patch.
        :param response_data: The data to be returned by the mock response.
        :param validates: Whether or not the response should validate.
        :return: The mocked Slack WebClient.
        """
        if method:
            mock_response = make_slack_response(response_data or {}, validates)
            mock_client = mocker.Mock(**{f"{method}.return_value": mock_response})
        else:
            mock_client = mocker.Mock()

        patch_slack_client(mock_client, path)
        return mock_client

    return _mock_slack
