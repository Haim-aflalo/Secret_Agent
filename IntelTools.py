class IntelTools:

    @staticmethod
    def encrypt_message(msg):
       return msg[::-1]

    @staticmethod
    def log_transmission(agent_name,message):
        print(agent_name,"sent encrypted message:",message)


