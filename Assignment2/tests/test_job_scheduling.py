import unittest

from job_scheduling import job_scheduling


class TestJobScheduling(unittest.TestCase):

    def test_standard_example(self):

        jobs = [
            ("J1", 2, 100),
            ("J2", 1, 19),
            ("J3", 2, 27),
            ("J4", 1, 25),
            ("J5", 3, 15)
        ]

        scheduled, profit = job_scheduling(jobs)

        self.assertEqual(profit, 142)
        self.assertEqual(len(scheduled), 3)

    def test_empty_jobs(self):

        scheduled, profit = job_scheduling([])

        self.assertEqual(scheduled, [])
        self.assertEqual(profit, 0)

    def test_single_job(self):

        jobs = [
            ("J1", 1, 50)
        ]

        scheduled, profit = job_scheduling(jobs)

        self.assertEqual(scheduled, ["J1"])
        self.assertEqual(profit, 50)

    def test_invalid_deadline(self):

        jobs = [
            ("J1", 0, 50)
        ]

        with self.assertRaises(ValueError):
            job_scheduling(jobs)


if __name__ == "__main__":
    unittest.main()
