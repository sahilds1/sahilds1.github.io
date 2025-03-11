Title: TIL: `git log` commands Cheatsheet
Date: 2025-02-14
Tags: git
Summary: Today I Learned: Small tools and facts I've learned
Status: published


```
git log --oneline	Show history in compact form (one commit per line)

git log --stat	Show file changes in each commit

git log --grep="<keyword>"	Search commit messages for a keyword

git log --after="2024-01-01"	Show commits after a specific date
git log --before="2024-01-01"	Show commits before a specific date

git log develop..main	Show commits in main but not in develop
git log -- <file>	Show history of a specific file
```