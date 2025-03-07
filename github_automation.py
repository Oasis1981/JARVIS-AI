
from github import Github

def crea_repository(nome_repo):
    g = Github("your_github_token")
    user = g.get_user()
    repo = user.create_repo(nome_repo)
    return repo.html_url
