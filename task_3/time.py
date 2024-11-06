import unittest

def cyclic_time_difference(hour1, hour2):
    direct_diff = abs(hour1 - hour2)
    cyclic_diff = 24 - direct_diff
    return min(direct_diff, cyclic_diff)

class TestCyclicTimeDifference(unittest.TestCase):
    def test_same_time(self):
        result = cyclic_time_difference(10, 10)
        print(f"Time 1: 10, Time 2: 10, Difference: {result}")
        self.assertEqual(result, 0)

    def test_midnight_difference(self):
        result = cyclic_time_difference(23, 1)
        print(f"Time 1: 23, Time 2: 1, Difference: {result}")
        self.assertEqual(result, 2)

    def test_half_day_difference(self):
        result = cyclic_time_difference(6, 18)
        print(f"Time 1: 6, Time 2: 18, Difference: {result}")
        self.assertEqual(result, 12)

    def test_near_boundaries(self):
        result_1 = cyclic_time_difference(23, 0)
        print(f"Time 1: 23, Time 2: 0, Difference: {result_1}")
        self.assertEqual(result_1, 1)

        result_2 = cyclic_time_difference(1, 23)
        print(f"Time 1: 1, Time 2: 23, Difference: {result_2}")
        self.assertEqual(result_2, 2)

if __name__ == "__main__":
    unittest.main()

