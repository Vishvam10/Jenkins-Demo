from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title='Test Todo')

    def test_todo_str_method(self):
        self.assertEqual(str(self.todo), 'Test Todo')

    # def test_fake_failure(self):
    #     self.assertEqual('', 'Test Todo')

    def test_index_view(self):
        response = self.client.get(reverse('todos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/index.html')
        self.assertContains(response, 'Test Todo')

    def test_add_todo(self):
        response = self.client.post(reverse('todos:add'), {'title': 'New Todo'})
        self.assertEqual(response.status_code, 302)  # Redirect status
        todos = Todo.objects.filter(title='New Todo')
        self.assertEqual(todos.count(), 1)

    def test_delete_todo(self):
        response = self.client.post(reverse('todos:delete', args=(self.todo.id,)))
        self.assertEqual(response.status_code, 302)  # Redirect status
        todos = Todo.objects.filter(title='Test Todo')
        self.assertEqual(todos.count(), 0)

    def test_update_todo(self):
        response = self.client.post(reverse('todos:update', args=(self.todo.id,)), {'isCompleted': 'on'})
        self.assertEqual(response.status_code, 302)  # Redirect status
        updated_todo = Todo.objects.get(id=self.todo.id)
        self.assertTrue(updated_todo.isCompleted)
