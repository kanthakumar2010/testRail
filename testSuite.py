from testrail.client import TestRail
# if u have to hit someother URL change URL & credintials below.
client = TestRail('audible-testrail.aka.amazon.com', 'ayshwarb@amazon.com', 'Bala@1962')

suiteId = '00000000' # Enter your Suite-Id here inside '####' 

result = client.get_suite(suiteId)
print(result)