from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(5, 9)

    @task
    def view_cfo(self):
        self.client.get("")
