import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    repo_names = [repo['name'] for repo in r['items']]
    assert 'become-qa-auto' in repo_names

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_get_emojis(github_api):
    emojis = github_api.get_emojis()
    assert len(emojis) > 0
    assert 'thumbsup' in emojis

@pytest.mark.api
def test_list_commits(github_api):
    commits = github_api.list_commits('MrMockingbird', 'prometheus')
    assert len(commits) > 0
    assert 'sha' in commits[0]

@pytest.mark.api
def test_get_specific_emoji(github_api):
    emojis = github_api.get_emojis()
    assert 'grinning' in emojis

@pytest.mark.api
def test_get_commit_author(github_api):
    commits = github_api.list_commits('MrMockingbird', 'prometheus')
    assert 'author' in commits[0]
    assert 'login' in commits[0]['author']