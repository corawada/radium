from django.test import TestCase
from .models import History


class HistoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        History.objects.create(title="first history", body="a body here")

    def test_title_content(self):
        history = History.objects.get(id=1)
        excepted_object_name = f'{history.title}'
        self.assertEqual(excepted_object_name, 'first history')

    def test_body_content(self):
        history = History.objects.get(id=1)
        excepted_object_name = f'{history.body}'
        self.assertEqual(excepted_object_name, 'a body here')
