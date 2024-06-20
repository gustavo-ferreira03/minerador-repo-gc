from pydriller import Repository

repo = Repository('https://github.com/ishepard/pydriller')
for commit in repo.traverse_commits():
    print(f"{commit.hash}")
    for file in commit.modified_files:
        print(f"\t{file.filename}")