import unittest
from nlp_utils import is_sufficient_for_decision
from llm_utils import get_socratic_questions

class TestDecisionMode(unittest.TestCase):
    def test_insufficient_decision_text(self):
        self.assertFalse(is_sufficient_for_decision("yes"))
        self.assertFalse(is_sufficient_for_decision("no"))
        self.assertFalse(is_sufficient_for_decision(""))

    def test_sufficient_decision_text(self):
        self.assertTrue(is_sufficient_for_decision("I am thinking of switching jobs for better pay."))

    def test_socratic_fallback_without_api_key(self):
        result = get_socratic_questions("Should I learn Rust or Go?")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
