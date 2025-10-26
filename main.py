from Agent import Agent
from Mission import Mission

agent = Agent("meir","10")
mission = Mission("run","tlv")
Mission.add_agent(agent)
Mission.brief()


# agent1 = Agent("James Bond","007")
# Agent.report(agent1)
# # print(agent1.clearance_level)
