from testrail.client import TestRail
client = TestRail('audible-testrail.aka.amazon.com', 'ayshwarb@amazon.com', 'Bala@1962')

runId = '00000000' # Enter your RunId here inside '####' 

result = client.get_run(runId)
print(result)