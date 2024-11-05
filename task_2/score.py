import unittest
from task_2 import calculate_company_threat
from gen_random import generate_random_data

class TestCompanyThreatScore(unittest.TestCase):
    def test_equal_threat_and_importance(self):
        departments = [
            {"scores": generate_random_data(30, 5, 50), "importance": 3},
            {"scores": generate_random_data(30, 5, 50), "importance": 3},
            {"scores": generate_random_data(30, 5, 50), "importance": 3}
        ]
        result = calculate_company_threat(departments)
        self.assertAlmostEqual(result, 30, delta=5)

    def test_high_threat_in_one_department(self):
        departments = [
            {"scores": generate_random_data(20, 5, 50), "importance": 2},
            {"scores": generate_random_data(80, 5, 50), "importance": 5}
        ]
        result = calculate_company_threat(departments)
        self.assertGreater(result, 50)

    def test_varied_user_counts(self):
        departments = [
            {"scores": generate_random_data(30, 5, 100), "importance": 3},
            {"scores": generate_random_data(50, 10, 10), "importance": 4}
        ]
        result = calculate_company_threat(departments)
        self.assertLess(result, 50)

    def test_boundaries(self):
        departments_all_zero = [{"scores": [0] * 50, "importance": 3}]
        departments_all_max = [{"scores": [90] * 50, "importance": 3}]
        
        self.assertEqual(calculate_company_threat(departments_all_zero), 0)
        self.assertEqual(calculate_company_threat(departments_all_max), 90)

if __name__ == '__main__':
    unittest.main()
