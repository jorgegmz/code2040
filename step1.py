from urllib2
import Request, urlopen, URLError

request = Request('http://challenge.code2040.org/api/register')
apiTkn = 92126c5c427966f9f5e8e7dcdb6d7a3b
try:
    response = urlopen(request)
    kit = response.read()
    print kit[559:1000]
