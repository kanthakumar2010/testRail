from testrail.client import TestRail
client = TestRail('audible-testrail.aka.amazon.com', 'ayshwarb@amazon.com', 'Bala@1962')

caseId = '00000000' # Enter your caseId here inside '####' 

case = client.get_case(caseId)
print(case)