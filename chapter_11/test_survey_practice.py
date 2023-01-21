import unittest

import language_survey_practice
from language_survey_practice import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def setUp(self):
        question = "What language did you speak, growing up?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']    
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question=question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        
    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question=question)
        responses = ['English', 'Mandarin', 'French']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
    
    def test_store_single_response_withSetUP(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses_WithSetUP(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)    

if __name__ == '__main__':
    unittest.main()
    
