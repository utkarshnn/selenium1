from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def world(self):
        self.client.get('')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 200000
