from jira import Jira


j= Jira(login='login', password='password', base_url='base_url')
print(j.create(project='SD', issuetype='Запрос на обслуживание'))