import os
from jira import Jira


LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('BASE_URL')
PROJECT = os.getenv('PROJECT')
ISSUE_TYPE = os.getenv('ISSUE_TYPE')



j= Jira(login=LOGIN, password=PASSWORD, base_url=BASE_URL)
print(j.create(project=PROJECT, issuetype=ISSUE_TYPE))