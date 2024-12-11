#!/usr/bin/env python
import sys
from new_mas.crew import FoodSafetyIntelligenceCrew

def run():
    """
    Run the food safety intelligence crew.
    """
    inputs = {
        'product_ingredients': 'Whole wheat flour,Sugar,Salt',
        'product_name': 'Honey Bunches of Oats'
    }
    FoodSafetyIntelligenceCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'product_ingredients': 'Training ingredients list',
        'product_name': 'Training Product'
    }
    try:
        FoodSafetyIntelligenceCrew().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Training error: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FoodSafetyIntelligenceCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Replay error: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'product_ingredients': 'Test ingredients list',
        'product_name': 'Test Product'
    }
    try:
        FoodSafetyIntelligenceCrew().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Test error: {e}")