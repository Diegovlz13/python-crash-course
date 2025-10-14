import unittest
from survey import AnonymusSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Pruebas para la clase AnonymousSurvey."""
    
    def setUp(self):
        """Crea una encuesta y un conjunto de respuestas para usar en todos los métodos de prueba."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymusSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    
    def test_store_single_response(self):
        """Comprueba si una respuesta simple se guarda bien."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Comprueba que se guardan correctamente tres respuestas individuales."""
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
    
    
if __name__ == '__main__':
    unittest.main()