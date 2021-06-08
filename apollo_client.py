import requests
import config


class TasksAPI:
    def __init__(self):
        self.url = "%s/tasks" % config.DOMAIN

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
