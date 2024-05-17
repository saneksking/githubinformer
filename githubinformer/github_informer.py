# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""GitHub informer"""
import requests


class GithubInformer:

    def __init__(self, user):
        self._user = user
        self._data = self._init()

    def _init(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            github_data = response.json()
            return github_data
        else:
            return []

    @property
    def api_url(self):
        return f'https://api.github.com/users/{self._user}/repos'

    def get_all_info(self):
        return self._data

    def check_repositories_count(self):
        return len(self._data)
w