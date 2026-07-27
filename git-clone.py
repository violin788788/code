import os,shutil
import subprocess
file_path = 'git-clone.txt'
try:
    with open(file_path, 'r') as file:
        user_and_repo = file.read().strip().replace("\n", "").replace(" ", "")
    if not user_and_repo:
        print("The file is empty or does not contain a valid repo.")
    else:
        repo_url = f"https://github.com/{user_and_repo}.git"
        print(f"Cloning repository: {repo_url}")
        subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository {repo_url} has been cloned successfully.")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except subprocess.CalledProcessError:
    print("Failed to clone the repository. Please check the URL or your Git configuration.")
except Exception as e:
    print(f"An error occurred: {e}")

iden = "/"
iden_location = user_and_repo.find(iden)
only_repo_name = user_and_repo[iden_location+len(iden):len(user_and_repo)]

print("only_repo_name",only_repo_name)

token_file_name = "token.txt"
shutil.copy(token_file_name, only_repo_name+"\\"+token_file_name)
print("token.txt pasted as well")