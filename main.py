from jira import JIRA
from jira.exceptions import JIRAError

options = {'server': 'https://it.dengisrazy.ru/'}

usr = 'jira_tech'
pas = '1234567890'

try:
    jira = JIRA(options=options, basic_auth=(usr, pas))
except JIRAError as e:
    if e.status_code == 401:
        print ("Login to JIRA failed.")
print ("Login!!")

new_issue = jira.create_issue(
                            project='SD',
                            summary= 'test 2207',
                            description= 'Description',
                            issuetype={'name': 'Запрос на обслуживание'},
                            )
print ("Done!")