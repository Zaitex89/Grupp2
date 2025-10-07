import pytest
from unittest.mock import patch, MagicMock
from omdb.omdb_client import OMDbClient

@pytest.fixture
def omdb_client():
    return OMDbClient(api_key="fake_api_key")

def mock_response(json_data, status=200):
    mock = MagicMock()
    mock.json.return_value = json_data
    mock.status.code = status
    return mock

#Replaces requests.get only in this module, @patch where name is imported/used
@patch("omdb.omdb_client.requests.get") 
def test_make_request_calls_api(mock_get, omdb_client):
    mock_get.return_value = mock_response({"Response": "True","Title": "Inception"}) #Defines fake response

    result = omdb_client._make_request({"t": "Inception"}) #gets mocked response

    mock_get.assert_called_once()
    assert result["Response"] == "True"
    assert result["Title"] == "Inception"
    #Checks _make_request returns same JSON data as our mock

@patch("omdb.omdb_client.requests.get")
def test_search_movies_handles_error(mock_get, omdb_client, capsys):
    #Simulates OMDb answer where "Response" is False & we got an Error
    mock_get.return_value = mock_response({"Response": "False", "Error": "Movie not found"})
    omdb_client.search_movies("nonexistent")
    captured = capsys.readouterr()
    #capsys captures standard output & standard errors
    assert "Error:" in captured.out
    #checks that function wrote error message to standard output