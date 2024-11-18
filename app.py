from githubinformer.github_informer import GitHubInformer


def main():
    informer = GitHubInformer('saneksking')
    print(informer.get_repo_data(name='saneksking'))


if __name__ == '__main__':
    main()
