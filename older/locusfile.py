from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    @task
    def index(self):
        self.client.get("/")
        
    @task
    def about(self):
        self.client.get("/about/")

class WebsiteUser(HttpLocust):
	host = "http://google.com.br"
    task_set = WebsiteTasks
    wait_time = between(5, 15)