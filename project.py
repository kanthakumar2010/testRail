from testrail.client import TestRail
client = TestRail('audible-testrail.aka.amazon.com', 'ayshwarb@amazon.com', 'Bala@1962')

projectId = '00000000' # Enter your ProjectId here inside '####' 

result = client.get_project(projectId)
print(result)