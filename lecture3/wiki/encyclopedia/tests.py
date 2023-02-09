from django.test import TestCase, Client

# Create your tests here.
class TestView(TestCase):
    def test_client(self):
        self.client = Client()


    def test_entry(self):
        response = self.client.get('/wiki/css')
        self.assertEqual(response.status_code, 200)

    def test_newpage(self):
        response = self.client.get('/newpage/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/newpage.html')

    def test_editEntry(self):
        response = self.client.get('/edit/Javascript')
        self.assertEqual(response.status_code, 200)