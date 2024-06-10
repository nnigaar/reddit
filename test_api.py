import pytest
import requests

@pytest.mark.parametrize("subreddit", ["python", "learnpython"])
def test_get_posts_from_subreddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    response = requests.get(url, headers={"User-Agent": "pytest"})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "children" in data["data"]

def test_invalid_subreddit():
    url = "https://www.reddit.com/r/invalidsubreddit/top.json"
    response = requests.get(url, headers={"User-Agent": "pytest"})
    assert response.status_code == 404

def test_user_agent():
    url = "https://www.reddit.com/r/python/top.json"
    response = requests.get(url, headers={"User-Agent": "invalid_user_agent"})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "children" in data["data"]
