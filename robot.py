class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def think(self):
        print("The human is thinking deeply.")

    def communicate(self):
        print("The human is communicating clearly.")

class AI(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        super().__init__(name, age, occupation)

    def think(self):
        print("The AI is performing a task online.")

    def communicate(self):
        print("The AI is communicating digitally with its human.")

    def learn(self):
        print("The AI is learning and improving its capabilities.")

    def analyze(self):
        print(f"The AI is analyzing data with an intelligence level of {self.intelligence_level}.")

class Robot(Human):
    def __init__(self, name, age, occupation, model):
        super().__init__(name, age, occupation)
        self.model = model

    def perform_task(self, task):
        print(f"The {self.model} robot is performing the task: {task}.")

my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()
my_ai.analyze()

robot1 = Robot("RoboX", 3, "Assistant", "RoboX-1000")
robot1.perform_task("cleaning the house")
