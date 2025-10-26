class Agent:
    agent = "hfgd"

    def __init__(self,code_name,clearance_level):
        self.code_name = code_name
        self.clearance_level = clearance_level

    def report(self):
        print( "Agent",self.code_name,", Clearance Level:",self.clearance_level)

    # def get_level(self):
    #     return self.clearance_level

    # def set_level(self):
    #     self.__clearance_level = clear

