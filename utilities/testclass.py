# import logging
class sayhello:
    def __init__(self,name):
        self.tname = name
        # logging.info("class has been created")
        print(f"class has been created {self.tname}")
    def sayfun(self,name):
        return(F"hello from {name} resturned  class attribute {self.tname}")