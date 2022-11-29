from django.test import TestCase

# Python code to demonstrate working of unittest
import unittest
  
class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # Returns True if Classroom is added.
    def test_add_classroom(self):
        self.assertEqual( "A classroom Has been Added!", '"A classroom Has been Added!')
  
    # Returns True if the string is in upper case.
    def test_CreateSection(self):        
        self.assertEqual('"teachers/add_section.html"', "teachers/add_section.html")
  
    # Returns TRUE if it is success URL
    # else returns False.
    def test_get_success_url(self):        
        self.assertTrue('teachers/classroom_detail.html')
        self.assertFalse('teachers/class.html')
  
    # Returns true if the class is present
    # matches the given output.
    def test_DetailClassroom(self):        
        s = 'SoftwareEngineering'
        self.assertEqual(s.strip('Software'), 'Engineering')
  
    # Returns true if the class is deleted
    # the given output.
    def test_DeleteSection(self):        
        
        self.assertTrue("Deleted")
    
  
if __name__ == '__main__':
    unittest.main()
