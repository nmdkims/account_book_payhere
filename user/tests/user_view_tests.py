from django.test import TestCase
from django.urls import resolve

from user.views import LoginView, UserSignupApiView


class UserViewTestCase(TestCase):
    """
    Assignee : 훈희
    user view와 url 연결에 대한 테스트를 합니다.
    """

    def test_url_resolves_to_sign_up_view(self):
        """sign_up url과 view가 잘 매치되었는지 Test"""

        found = resolve("/users/signup")

        self.assertEqual(found.func.__name__, UserSignupApiView.as_view().__name__)

    def test_url_resolves_to_sign_in_view(self):
        """Login url과 view가 잘 매치되었는지 Test"""

        found = resolve("/users/login")

        self.assertEqual(found.func.__name__, LoginView.as_view().__name__)
