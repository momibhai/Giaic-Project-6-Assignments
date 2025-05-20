class Logger:
    def __init__(self):
        print("Object is Created via Constructor")

    def __del__(self):
        print("Object is Destroyed via Destructor")

l1 = Logger()
del l1 


