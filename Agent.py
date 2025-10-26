class Agent:
    agent = None

    def __init__(self,code_name,clearance_level):
        self.code_name = code_name
        self.__clearance_level = clearance_level

    def report(self):
        print( "Agent",self.code_name,", Clearance Level:",self.__clearance_level)

    def get_level(self):
        return self.__clearance_level

    def set_level(self,level):
        if 1 < level < 5:
            self.__clearance_level = level
        else:
            print("level doesn't exist")

