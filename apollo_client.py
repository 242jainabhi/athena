import requests


class TasksAPI:
    def __init__(self):
        self.url = "http://127.0.0.1:5002/tasks"

    def post_task(self, task_id, task):
        try:
            response = requests.post("%s/%s" % (self.url, task_id), data={"data": task})
        except:
            raise Exception('')
        else:
            return response

    def get_task(self, task_id):
        response = requests.get("%s/%s" % (self.url, task_id))
        return response

    def delete_task(self, task_id):
        response = requests.delete("%s/%s" % (self.url, task_id))
        return response

# api = TasksAPI()
# print(api.get_task('task_1').text)