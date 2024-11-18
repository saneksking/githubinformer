# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""GitHub informer"""
import json
import urllib.request


class GitHubInformer:

    def __init__(self, user):
        self._user = user
        self._github_repos_data_api = f'https://api.github.com/users/{self._user}/repos?per_page=100'
        self._repos_data = self.get_github_data(self._github_repos_data_api)

    @classmethod
    def get_github_data(cls, url):
        try:
            repo_dict = {}
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            repositories_data = json.loads(response.read())
            for repository in repositories_data:
                repo_dict[repository['name']] = repository
            return repo_dict
        except Exception as e:
            print(e)
            return []

    def get_repo_data(self, name):
        return self._repos_data[name]

    @property
    def github_repos_api_url(self):
        return self._github_repos_data_api

    def get_github_repos_data(self):
        return self._repos_data

    def get_repositories_count(self):
        return len(self._repos_data)
