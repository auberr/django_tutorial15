from django.urls import reverse
from rest_framework.test import APITestCase
# Create your tests here.

class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username":"testuser1",
            "password":"password",
            "email":"test@user.com",
            "fullname":"kim"
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data['message'], "가입 완료!!")