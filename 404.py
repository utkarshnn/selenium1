import urllib2
for url in ['https://stage.raptorsupplies.com/p/%s' % page for page in xrange(0,300000)]:
    try:
        connection = urllib2.urlopen(url)
        print connection.getcode()
        connection.close()
    except urllib2.HTTPError, e:
        print e.getcode()
