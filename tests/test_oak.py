import unittest
from oak.runtime import run_script

class TestOakScript(unittest.TestCase):
    def test_import_section(self):
        source = '''
        BEGIN PROJ "oak.project"
            BEGIN SECTION "math"
                var x := eval mathexp "5 * 2"
            END SECTION "math"

            BEGIN SECTION "main"
                import math
                ret x
            END SECTION "main"
        END PROJ "oak.project"
        '''
        result = run_script(source)
        self.assertEqual(result, 10.0)

    def test_loop(self):
        source = '''
        BEGIN PROJ "oak.project"
            BEGIN SECTION "main"
                var count := eval mathexp "3"
                loop 2
                    print count
                ret count
            END SECTION "main"
        END PROJ "oak.project"
        '''
        result = run_script(source)
        self.assertEqual(result, 3.0)

    def test_if(self):
        source = '''
        BEGIN PROJ "oak.project"
            BEGIN SECTION "main"
                var result := eval mathexp "5"
                if result > 3
                    print result
                ret result
            END SECTION "main"
        END PROJ "oak.project"
        '''
        result = run_script(source)
        self.assertEqual(result, 5.0)

if __name__ == '__main__':
    unittest.main()
