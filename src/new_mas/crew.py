from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Potential future custom tools
# from new_mas.tools.ingredient_database_tool import IngredientDatabaseTool

@CrewBase
class FoodSafetyIntelligenceCrew():
    """Food Ingredient Safety Multi-Agent System"""

    @agent
    def ingredient_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['ingredient_researcher'],
            verbose=True
        )

    @agent
    def allergen_identifier(self) -> Agent:
        return Agent(
            config=self.agents_config['allergen_identifier'],
            verbose=True
        )

    @agent
    def additive_risk_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config['additive_risk_assessor'],
            verbose=True
        )

    @agent
    def safety_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['safety_reporter'],
            verbose=True
        )

    @task
    def ingredient_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['ingredient_research_task'],
        )

    @task
    def allergen_identification_task(self) -> Task:
        return Task(
            config=self.tasks_config['allergen_identification_task'],
        )

    @task
    def additive_risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['additive_risk_assessment_task'],
        )

    @task
    def safety_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['safety_reporting_task'],
            output_file='food_safety_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Food Safety Intelligence Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )