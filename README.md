# GitHub Informer <sup>v 0.0.2</sup>

***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/saneksking/githubinformer)](https://github.com/saneksking/githubinformer/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/githubinformer?label=pypi%20downloads)](https://pypi.org/project/githubinformer/)
![GitHub top language](https://img.shields.io/github/languages/top/saneksking/githubinformer)
[![PyPI](https://img.shields.io/pypi/v/githubinformer)](https://pypi.org/project/githubinformer)
[![GitHub](https://img.shields.io/github/license/saneksking/githubinformer)](https://github.com/saneksking/githubinformer/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/githubinformer)](https://pypi.org/project/githubinformer)

---

## Short description:
GithubInformer --> A library to get data of open users repositories GitHub.

---

## Author - [Saneksking](https://github.com/saneksking)

---


***

## Help:

`pip install githubinformer`

```python
from githubinformer.github_informer import GitHubInformer

github_informer = GitHubInformer(user='saneksking')
github_informer.get_all_info() # Returns full information about open repositories of user
github_informer.get_repositories_count() # Returns a count of user open repositories 
```

***

## Disclaimer of liability:
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
