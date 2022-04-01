from django.test import Client, TestCase
from django.urls import reverse

#Create your tests here.


class GroupTaskTest(TestCase):

    # 01. Test the index page.
    def test_index_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Crime details in San Francisco between 01/01/2015 and 29/03/2015")

    # 02. Test the login page.
    def test_login_text(self):
        client = Client()
        response = client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Login Page")

    # 03. Test the registration page.
    def test_register_text(self):
        client = Client()
        response = client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Registration")

    # 04. Test the date search page.
    def test_date_search_text(self):
        client = Client()
        response = client.get('/date_search/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Date search")
        self.assertContains(response, "January:")
        self.assertContains(response, "February:")
        self.assertContains(response, "March:")
    
    # 05. Test the position search page.
    def test_position_search_text(self):
        client = Client()
        response = client.get('/position_search/' )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Date search")
    
    # 06. Test the position search page.
    def test_coorinates_search_text(self):
        client = Client()
        response = client.get('/coordinates_search/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Accurate coordinates search")
    
    # 07. Test the total database page.
    def test_data_total_text(self):
        client = Client()
        response = client.get('/total/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Date Details")
    
    # login required
    # 08. Test the data edit page.
    # def test_data_edit_text(self):
    #    client = Client()
    #    response = client.get('/data_edit/')
    #    self.assertEqual(response.status_code, 200)
    #    self.assertContains(response, "*First, search a row of data you want. Then, you could edit the data (add, modify or delete).")
    #    self.assertContains(response, "Enter a id number then this row will be deleted")
    #    self.assertContains(response, "*If you enter a outindex ID number, the system will create the row.")
