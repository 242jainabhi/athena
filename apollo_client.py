import requests

print(requests.get("http://127.0.0.1:5002/tasks/task_1").text)
requests.post("http://127.0.0.1:5002/tasks/task_1", data={"data": "Buy groceries"})
print(requests.get("http://127.0.0.1:5002/tasks/task_1").text)
requests.post("http://127.0.0.1:5002/tasks/task_2", data={"data": "Pay bills"})
print(requests.get("http://127.0.0.1:5002/tasks/task_2").text)
requests.delete("http://127.0.0.1:5002/tasks/task_1")
print(requests.get("http://127.0.0.1:5002/tasks/task_1").text)

