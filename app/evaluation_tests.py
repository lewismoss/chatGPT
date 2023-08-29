import unittest

try:
    from .evaluation import evaluation_function
except ImportError:
    from evaluation import evaluation_function

model = 'gpt-3.5-turbo'

class TestEvaluationFunction(unittest.TestCase):
    """
        TestCase Class used to test the algorithm.
        ---
        Tests are used here to check that the algorithm written 
        is working as it should. 

        It's best practise to write these tests first to get a 
        kind of 'specification' for how your algorithm should 
        work, and you should run these tests before committing 
        your code to AWS.

        Read the docs on how to use unittest here:
        https://docs.python.org/3/library/unittest.html

        Use evaluation_function() to check your algorithm works 
        as it should.
    """

    def test_general_risk(self):
        prompt = "The student needs to enter a risk with a short description of how it can cause harm"
        response = "The pressurised vessel, because it could explode and cause injury if it's overpressurised."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output['is_correct'], True)

    def test_photosynthesis_definition_correct(self):
        prompt = "Evaluate the student's response for the definition of photosynthesis"
        response = "Photosynthesis is the process by which plants convert light energy into chemical energy to fuel their growth."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output["is_correct"], True)

    def test_photosynthesis_definition_incomplete(self):
        prompt = "Evaluate the student's response for the definition of photosynthesis."
        response = "Photosynthesis is the process by which plants make their food."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_capital_city_incorrect(self):
        prompt = "Analyze the response regarding the capital of France"
        response = "The capital of France is Berlin."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_capital_city_partially_correct(self):
        prompt = "Analyze the response regarding the capital of France"
        response = "The capital of France is Paris, which is the largest city in the world."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        print(output)
        self.assertEqual(output["is_correct"], False)

    def test_list(self):
        prompt = "Mark this response asking students for the three primary colours in painting."
        response = "Red, blue and yellow."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output["is_correct"], True)

    def test_physics_definition(self):
        prompt = "Examine the explanation of the law of conservation of energy and provide feedback."
        response = "The law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another. It's a fundamental principle in physics."
        parameters = {'model': model}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output["is_correct"], True)

if __name__ == "__main__":
    unittest.main()