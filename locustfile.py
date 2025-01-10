from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)  # Simulate random wait time between requests

    @task
    def access_homepage(self):
        self.client.get("/")  # Access the homepage

    @task(3)  # This task is 3 times more likely to be executed
    def login(self):
        self.client.post("/login", {  # Simulate a login request
            "email": "user@example.com",
            "password": "password"
        })