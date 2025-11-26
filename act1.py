class myClass:
    _privateVar=27
    def _privMeth(self):
        print("I am inside class myClass ")
    def hello(self):
        print("Private Variable value:",myClass._privateVar)
foo=myClass()
foo.hello()
foo._privMeth