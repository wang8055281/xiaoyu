class BaseXiaoyu(object):

    def __init__(self, name):
        self.name = name

    def _sayHello(self, name):
        print "hello, %s" % name