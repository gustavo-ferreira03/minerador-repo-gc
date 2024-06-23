from pydriller import Repository

repo = Repository('https://github.com/ishepard/pydriller')
for commit in repo.traverse_commits():
    print(f"{commit.hash} - {commit.author_date} - {commit.committer_date}")
    commit.committer_date