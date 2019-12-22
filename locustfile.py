from locust import HttpLocust, TaskSet, between, task


class UserBehavior(TaskSet):

    @task(1)
    def get_students(self):
        self.client.get('/api/students')

    @task(1)
    def get_student(self):
        self.client.get('/api/students/1')

    @task(2)
    def create_student(self):
        payload = {
            'name': 'Petr Petrov',
            'chair': 'IFTKN',
            'group': 223
        }
        self.client.post('/api/students', json=payload)

    @task(2)
    def update_student(self):
        payload = {
            'name': 'Volodymyr Peron upd',
            'chair': 'IFTKN upd',
            'group': 543
        }
        self.client.put('/api/students/1', json=payload)

    @task(2)
    def delete_student(self):
        self.client.delete('/api/students/2')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)