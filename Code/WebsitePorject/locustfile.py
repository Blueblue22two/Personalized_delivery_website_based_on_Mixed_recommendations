import json
from locust import HttpUser, between, task, events
from locust.event import Events
from bs4 import BeautifulSoup
import time


class WebsiteUser(HttpUser):
    wait_time = between(1, 4)

    # extract CSRF token from HTML
    def extract_csrf_token(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
        return token


    @task(3)
    def login_view(self):
        with self.client.get("login/", timeout=10, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Login page failed to load")

    @task(1)
    def login_customer_and_logout(self):
        response = self.client.get("accounts/login/customer/", timeout=20)
        if response.status_code == 200:
            csrf_token = self.extract_csrf_token(response)
            with self.client.post("accounts/login/customer/", {
                'username': 'james',
                'password': '123456789',
                'userType': '1',
                'csrfmiddlewaretoken': csrf_token
            }, headers={'Referer': "accounts/login/customer/", 'Content-Type': 'application/x-www-form-urlencoded'},
                                  timeout=15, catch_response=True) as post_response:
                if post_response.status_code != 200:
                    # Extracting error message from JSON response if available
                    error_message = json.loads(post_response.text).get('message', 'No error message provided')
                    post_response.failure(f"Login customer failed or timed out: {error_message}")
                else:
                    post_response.success()
        else:
            error_message = json.loads(response.text).get('message', 'No error message provided')
            response.failure(f"Failed to get login customer page: {error_message}")
        self.client.get("accounts/logout/")


    @task(1)
    def login_merchant_and_logout(self):
        response = self.client.get("accounts/login/merchant/", timeout=20)
        if response.status_code == 200:
            csrf_token = self.extract_csrf_token(response)
            with self.client.post("accounts/login/merchant/", {
                'username': 'TestMerchant',
                'password': '987654321',
                'userType': '2',
                'csrfmiddlewaretoken': csrf_token
            }, headers={'Referer': "accounts/login/merchant/", 'Content-Type': 'application/x-www-form-urlencoded'},
                                  timeout=15, catch_response=True) as post_response:
                if post_response.status_code != 200:
                    # Extracting error message from JSON response if available
                    error_message = json.loads(post_response.text).get('message', 'No error message provided')
                    post_response.failure(f"Login merchant failed or timed out: {error_message}")
                else:
                    post_response.success()
        else:
            error_message = json.loads(response.text).get('message', 'No error message provided')
            response.failure(f"Failed to get login merchant page: {error_message}")
        self.client.get("accounts/logout/")

    @task(2)
    def register_customer(self):
        self.client.get("accounts/register/customer/")

    @task(2)
    def register_merchant(self):
        self.client.get("accounts/register/merchant/")

    @task(1)
    def search_view(self):
        self.client.get("accounts/search/")

    @task(1)
    def category_burger_view(self):
        self.client.get("products/product_category/Burger/")

    @task(1)
    def popular_shop_view(self):
        self.client.get("recommend/popular_view/")

    @task(1)
    def recommendation_view(self):
        self.client.get("recommend/recommend_view/")

    @task(1)
    def pizza_shop_view(self):
        self.client.get("store/shop/Pizza_shop/")

    @task(1)
    def product_view(self):
        self.client.get("products/product_view/42/")


    @staticmethod
    @events.request.add_listener
    def on_request(request_type, name, response_time, response_length, response, context, exception=None, **kwargs):
        if response and response.status_code != 200:
            print(f"Failed request {name} with status code {response.status_code}")
        if response and response.status_code == 200:
            print(f"Successful request {name} after failure")
        if exception:
            print(f"Request {name} raised an exception: {exception}")
