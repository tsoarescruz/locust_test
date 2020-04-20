from locust import HttpLocust, TaskSet, task

class PublicTaskSet(TaskSet):

    @task(1)
    def alternativa(self):
        self.client.get('/experiments/premium-highlight/GLOBOPLAY-HOME-destaque-premium-com-recomendacao/:alternativa/')

class PrivateTaskSet(TaskSet):

    @task(1)
    def recommendation(self):
        self.client.get('/experiments/premium-highlight/GLOBOPLAY-HOME-destaque-premium-com-recomendacao/recommendation?web=X1&tablet=X1,X1_5&tv=X1&mobile=X1,X1_5')

class WebsiteTasks(TaskSet):
    tasks = {
        PublicTaskSet: 20,
        PrivateTaskSet: 10,
    }

class BasicTasks(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 10000
