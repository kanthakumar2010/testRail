from testrail.client import TestRail
client = TestRail('audible-testrail.aka.amazon.com', 'ayshwarb@amazon.com', 'Bala@1962')
case = client.get_cases('21', '1849218')
print(case)