from github import Github,Auth
import os
import subprocess
import shutil


auth = Auth.Token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

g = Github(auth=auth)
repo_name = "AbhashDas/devopsbatch5"
repo = g.get_repo(repo_name)

latest_commit = repo.get_commits()[0]

latest_commit_sha = latest_commit.sha
print(latest_commit_sha)

repo_url = repo.clone_url
destination_dir = "~/CICDPipeline/repo"

if os.path.exists("~/CICDPipeline/commit_hash.txt"):
    with open("~/CICDPipeline/commit_hash.txt", "r") as commit_hash_file:
        previous_commit_sha = commit_hash_file.read()

    if previous_commit_sha == latest_commit_sha:
        print("No new commits")
        exit(0)

else:
    print("Running for the first time")

with open("~/CICDPipeline/commit_hash.txt", "w") as file:
    file.write(latest_commit_sha)

if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir)

subprocess.run(["git", "clone", repo_url, destination_dir])
print("Cloned repo")

subprocess.run(["/bin/bash", "/home/ubuntu/CICDPipeline/deployment.sh"])


commit_hash_file = open("commit_hash.txt", "w")
commit_hash_file.write(latest_commit_sha)
commit_hash_file.close()

g.close()