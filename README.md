#Building CI-CD Pipeline Tool
--------------------------------------------------------------------------------------

**Task1:**
- index.html is created at ~/CICDPipeline/index.html

**Task2: **
- Install NGINX
  - sudo apt-get update
  - sudo apt-get upgrade
  - sudo apt-get install nginx
  - sudo service nginx status --> active(running)

**Task3:**
- Python Script to Check for New Commits
  - py_get_pipeline.py for tracking the new commits made in Github using the GitHub API

**Task4:**
- Bash Script to Deploy the Code
  - deployment.sh --> bash file to copy the latest index.html from github repo to the nginx /var/www/html/index.html to deploy the changes to production

**Task5:**
- Cron Job to Run the Python Script
  - **crontab -e**
    * * * * * /usr/bin/python3 /home/ubuntu/CICDPipeline/py_git_pipeline.py >> /home/ubuntu/CICDPipeline/py_log.txt 2>&1
  - Enter the above line in "crontab -e" to keep track if any changes has been pushed to github every minute. The details log of the python file will be logged to py_log.txt

**Task6:**
- Push a change to index.html and this should trigger the python file to track the changes and deploy the changes in nginx server to see it in production.
