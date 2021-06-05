import unittest
import sys
sys.path.append('..')

from apollo_client import TasksAPI


class TaskApiTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = TasksAPI()

    def test_post_request(self):
        response = self.client.post_task('task_1', 'remember the milk')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'task_1': 'remember the milk'})

    def test_get_request(self):
        response = self.client.get_task('task_1')
        self.assertEqual(response.json(), {'task_1': 'remember the milk'})

    def test_delete_request(self):
        response = self.client.delete_task('task_1')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

