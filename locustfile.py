from locust import HttpUser, task, between
from random import choice

item_ids = [173, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 
    155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 
    142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 
    130, 129, 128, 121, 107, 106, 105, 104, 102, 101, 100, 99, 
    98, 97, 96, 95, 94, 93, 92, 89, 88, 87, 85, 84, 83, 80, 79, 
    78, 77, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 
    44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 31, 30, 29, 
    28, 27, 26, 25, 24, 23, 22, 21, 20, 18, 17, 16, 15, 14, 13, 
    12, 11, 10, 9, 8, 7, 6]

pages = [
    '/map',
    '/timeline',
    '/exhibits/show/lifecareer',
    '/exhibits/show/scholarship',
    '/exhibits/show/teaching'
]

class OmekaUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def go_home(self):
        self.client.get("/")
    
    @task(3)
    def get_item(self):
        item_id = choice(item_ids)
        self.client.get(f'/items/show/{item_id}')

    @task(3)
    def get_page(self):
        page = choice(pages)
        self.client.get(page)
