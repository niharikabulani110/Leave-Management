from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import LeaveRequest
from datetime import date
from django.utils import timezone

class LeaveRequestViewTests(TestCase):
    def setUp(self):
        # Create test users
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        
        # Create some test leave requests
        self.leave_request = LeaveRequest.objects.create(
            user=self.user,
            start_date=date(2024, 1, 1),
            end_date=date(2024, 1, 5),
            reason="Test leave request",
            status='pending'
        )

    def test_login_view_get(self):
        """Test login page loads correctly"""
        response = self.client.get(reverse('leave_requests:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave_requests/login.html')

    def test_login_view_post_success(self):
        """Test successful login"""
        response = self.client.post(reverse('leave_requests:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertRedirects(response, reverse('leave_requests:home'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_view_post_failure(self):
        """Test failed login"""
        response = self.client.post(reverse('leave_requests:login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_logout_view(self):
        """Test logout functionality"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('leave_requests:logout'))
        self.assertRedirects(response, reverse('leave_requests:login'))
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_home_view_authenticated(self):
        """Test home view shows correct leave requests for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('leave_requests:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave_requests/home.html')
        self.assertIn(self.leave_request, response.context['leave_requests'])

    def test_home_view_unauthenticated(self):
        """Test home view redirects for unauthenticated user"""
        response = self.client.get(reverse('leave_requests:home'))
        self.assertRedirects(response, f"{reverse('leave_requests:login')}?next={reverse('leave_requests:home')}")

    def test_create_leave_request_get(self):
        """Test create leave request page loads correctly"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('leave_requests:create_leave_request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave_requests/create_leave_request.html')

    def test_create_leave_request_post_success(self):
        """Test successful leave request creation"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('leave_requests:create_leave_request'), {
            'start_date': '2024-02-01',
            'end_date': '2024-02-05',
            'reason': 'New test leave request'
        })
        self.assertRedirects(response, reverse('leave_requests:home'))
        self.assertTrue(LeaveRequest.objects.filter(
            user=self.user,
            start_date='2024-02-01',
            end_date='2024-02-05'
        ).exists())

    def test_create_leave_request_post_invalid_form(self):
        """Test leave request creation with invalid data"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('leave_requests:create_leave_request'), {
            'start_date': 'invalid-date',
            'end_date': '2024-02-05',
            'reason': 'New test leave request'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave_requests/create_leave_request.html')
        self.assertFalse(LeaveRequest.objects.filter(reason='New test leave request').exists())
