import json
import requests

def get_repo(github_id):

    user_url = requests.get('https://api.github.com/users/{}/repos'.format(github_id)) #get access to the github ID
    get_user = json.loads(user_url.text)
    repo_commit_info = dict()

# check if the user ID is valid 
    try:
        get_user[0]['name']
    except:
        return 'No user found'

# iterate through each repository    
    for repos in get_user:
        repo_name = repos['name']
        repo_url = requests.get('https://api.github.com/repos/{}/{}/commits'.format(github_id, repo_name)) #access each repository
        get_repo_info = json.loads(repo_url.text)

        if repo_name in repo_url.text:
            num = len(get_repo_info)
        else:
            num = 0 

        repo_commit_info[repo_name] = num
    
    return [['Repo: {} Number of commits: {} '.format(k, v)] for k, v in repo_commit_info.items()]

def main():
    github_id = input('Please enter your github ID :' )
    print(get_repo(github_id))
    
main()






