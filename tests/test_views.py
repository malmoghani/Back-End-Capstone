from django.contrib.auth.models import User  
from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # 1. Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # 2. Authenticate the client
        self.client.force_authenticate(user=self.user)
        
        # 3. Add test instances
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Bruschetta", Price=15, Inventory=50)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data
        
        # Ensure the URL matches your path exactly
        response = self.client.get('/restaurant/menu/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)