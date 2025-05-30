import unittest
from oak.runtime import run_script

class TestOakScript(unittest.TestCase):
    def test_basic_math(self):
        source = '''
        BEGIN PROJ "oak.project"
            BEGIN SECTION "main"
                var result := eval mathexp "2 + 2"
                ret result
            END SECTION "main"
        END PROJ "oak.project"
        '''
        result = run_script(source)
        self.assertEqual(result, 4.0)

    def test_multiple_sections(self):
        source = '''
        BEGIN PROJ "oak.project"
            BEGIN SECTION "main"
                var a := eval mathexp "10"
                print a
                ret a
            END SECTION "main"
            BEGIN SECTION "math"
                var b := eval mathexp "5 + 5"
                print b
            END SECTION "math"
        END PROJ "oak.project"
        '''
        result = run_script(source)
        self.assertEqual(result, 10.0)

    def test_print_literal(self):
        source = '''
        BEGIN PROJ "oak.project"
            BEGIN SECTION "main"
                print 3 + 2
                ret 0
            END SECTION "main"
        END PROJ "oak.project"
        '''
        result = run_script(source)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()