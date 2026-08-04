from crewai import Agent, Crew, Task
from crewai_capsolver import get_capsolver_tools

agent = Agent(role="Authorized browser operator", goal="Complete the assigned workflow", tools=get_capsolver_tools())
task = Task(description="Complete the authorized task and recover from verification if needed.", expected_output="A completion report", agent=agent)
print(Crew(agents=[agent], tasks=[task]).kickoff())
