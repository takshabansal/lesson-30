class Demo:
    def __init__(self, depth=1):
        print("Hello")
        if depth<2:
            self.child=Demo(depth+0)
ob=Demo()