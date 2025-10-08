import pytest
from unittest.mock import patch, MagicMock
from omdb.omdb_client import OMDbClient

@pytest.fixture
def omdb_client():
    return OMDbClient(api_key="fake_api_key")

# Helper to create a mock requests response.
def mock_response(json_data, status=200):
    mock = MagicMock()
    mock.json.return_value = json_data
    mock.status_code = status
    return mock

# Test search_movies with successful response
@patch("omdb.omdb_client.requests.get")
def test_search_movies_success(mock_get, omdb_client):
    mock_get.return_value = mock_response({
        "Response": "True",
        "Search": [{
            "Title": "Inception",
            "Year": "2010",
            "imdbID": "tt1375666"
        }]
    })

    result = omdb_client.search_movies("Inception")
    
    mock_get.assert_called_once()
    assert isinstance(result, list)
    assert result[0]["Title"] == "Inception"
    assert result[0]["Year"] == "2010"

# Test search_movies when API returns error or no results
@patch("omdb.omdb_client.requests.get")
def test_search_movies_no_results(mock_get, omdb_client):
    mock_get.return_value = mock_response({
        "Response": "False",
        "Error": "Movie not found"
    })

    result = omdb_client.search_movies("nonexistent")
    
    mock_get.assert_called_once()
    assert result == []

# Test get_movie_details with imdb_id
@patch("omdb.omdb_client.requests.get")
def test_get_movie_details_by_id_success(mock_get, omdb_client):
    mock_get.return_value = mock_response({
        "Response": "True",
        "Title": "Inception",
        "Year": "2010"
    })

    result = omdb_client.get_movie_details(imdb_id="tt1375666")
    
    mock_get.assert_called_once()
    assert result["Title"] == "Inception"
    assert result["Year"] == "2010"

# Test get_movie_details with title
@patch("omdb.omdb_client.requests.get")
def test_get_movie_details_by_title_success(mock_get, omdb_client):
    mock_get.return_value = mock_response({
        "Response": "True",
        "Title": "Inception",
        "Year": "2010"
    })

    result = omdb_client.get_movie_details(title="Inception")
    
    mock_get.assert_called_once()
    assert result["Title"] == "Inception"

# Test get_movie_details returns None when movie not found
@patch("omdb.omdb_client.requests.get")
def test_get_movie_details_not_found(mock_get, omdb_client):
    mock_get.return_value = mock_response({
        "Response": "False",
        "Error": "Movie not found"
    })

    result = omdb_client.get_movie_details(title="nonexistent")
    
    mock_get.assert_called_once()
    assert result is None

# Test get_movie_details returns None when neither id nor title provided
def test_get_movie_details_no_args(omdb_client):
    with pytest.raises(ValueError):
        omdb_client.get_movie_details()
