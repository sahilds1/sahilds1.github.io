Title: TIL: Git Commands Before Reading Code
Date: 2026-06-23
Category: Today I Learned
Status: published

I started contributing to the [Code for Philly PAX](https://github.com/Philadelphia-Lawyers-for-Social-Equity/PA_Expunger) project and inspected the codebase by running the git commands [Ally Piechowski](https://piechowski.io/)uses to identify code churn hotspots, bus factor, bug clusters, and crisis patterns. 

What Changes the Most:
```
git log --format=format: --name-only --since="1 year ago" | sort | uniq -c | sort -nr | head -20
```

Who Built This:
```
git shortlog -sn --no-merges
```

Where Do Bugs Cluster:
```
git log -i -E --grep="fix|bug|broken" --name-only --format='' | sort | uniq -c | sort -nr | head -20
```

Is This Project Accelerating or Dying:
```
git log --format='%ad' --date=format:'%Y-%m' | sort | uniq -c
```

How Often Is the Team Firefighting:
```
git log --oneline --since="1 year ago" | grep -iE 'revert|hotfix|emergency|rollback'
```


Via: [https://piechowski.io/post/git-commands-before-reading-code/](https://piechowski.io/post/git-commands-before-reading-code/)