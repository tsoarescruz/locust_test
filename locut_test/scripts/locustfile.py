from locust import HttpLocust, TaskSet, task, between
from locust.log import setup_logging
from locust.contrib.fasthttp import FastHttpLocust
import requests
class PublicTaskSet(TaskSet):
    @task(1)
    def alternativa(self):
        self.client.get("/mve-api/globo-play-beta/experiments/premium-highlight/GLOBOPLAY-HOME-destaque-premium-com-recomendacao/multiplos-destaques-com-recomendacao/")
class PrivateTaskSet(TaskSet):
    @task(1)
    def recommendation(self):
       self.client.get("/mve-api/globo-play/experiments/premium-highlight/GLOBOPLAY-HOME-destaque-premium-com-recomendacao/recommendation?web=X1&mobile=X1",
            headers = {
                "authorization": "Bearer 1b36a0531234bf250529d5f21eaf6ccec4561495544634738424f725532582d7839554e4e575671426956704e6c45307a467267683731565948543073724575763653317958534e58317a6c7264724f664d367931437962364d5170425571624b66314a6771773d3d3a303a756b687776716f75726a6f78737578747077726e"
            })
class WebsiteTasks(TaskSet):
    tasks = {
        PublicTaskSet: 20,
        PrivateTaskSet: 10,
    }
class BasicTasks(FastHttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0.1, 1)