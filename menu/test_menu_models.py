from django.test import TestCase
from .models import Menu, Category


class TestModels(TestCase):

    def setUp(self):
        Menu.objects.create(meal_name='Meal1', slug='meal_name', description='desc1', vegetarian_vegan='vegan', price='1', created_on='2022-03-01 12:00')
        Category.objects.create(meal_category='Category1')

    def test_meal_name_defaults_to_true(self):
        meal = Menu.objects.get(meal_name='Meal1')
        self.assertTrue(meal.meal_name)

    def test_menu_string_method_returns_meal_name(self):
        meal = Menu.objects.get(meal_name='Meal1')
        self.assertEqual(str(meal), 'Meal1')

    def test_category_defaults_to_true(self):
        category = Category.objects.get(meal_category='Category1')
        self.assertTrue(category.meal_category)

    def test_category_string_method_returns_meal_category(self):
        category = Category.objects.get(meal_category='Category1')
        self.assertEqual(str(category), 'Category1')