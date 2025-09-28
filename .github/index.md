---
abstract: Basic information about the CI/CD processes in this repo.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-02-19
title: GitHub Actions configuration
---

## Dependabot

Stay away from zero days with Dependabot.

```{autoyaml} .github/dependabot.yml
```

## Workflows

GitHub Actions provides a pretty complete CI/CD system and they'll let you
run a lot of pipelines for free.

### documentation

This workflow produces the GitHub Pages site.

```{autoyaml} .github/workflows/documentation.yml
```

### pylint

I still like to run things through PyLint anyway.

```{autoyaml} .github/workflows/pylint.yml
```

### shell

And ShellCheck never hurt anybody either.

```{autoyaml} .github/workflows/shell.yml
```
