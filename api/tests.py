from django.test import TestCase

from utils.calculator_notes import sum_return_note_semester
from django.core.exceptions import ValidationError

# Create your tests here.
class StudentNotesUtilsTestCase(TestCase):
    def test_raise_validation_error_if_len_list_note_is_minus_four(self):
        self.assertRaises(ValidationError)
            
    
    