from django.test import Client, TestCase


class DynamicUrlTests(TestCase):
    def test_negative_numbers(self):
        response = Client().get('/catalog/-1')
        self.assertEqual(response.status_code, 404)

    def test_zero_number(self):
        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)

    def test_underscore(self):
        response = Client().get('/catalog/_')
        self.assertEqual(response.status_code, 404)

    def test_number_contains_string(self):
        response = Client().get('/catalog/str')
        self.assertEqual(response.status_code, 404)

    def test_number_with_ubderscore_and_string(self):
        response = Client().get('/catalog/str_123')
        self.assertEqual(response.status_code, 404)

    def test_string_and_numbers(self):
        response = Client().get('/catalog/123str')
        self.assertEqual(response.status_code, 404)

    def test_big_number_with_leading_zeroes(self):
        response = Client().get('/catalog/003456')
        self.assertEqual(response.status_code, 404)

    def test_number_starts_with_zero(self):
        response = Client().get('/catalog/01')
        self.assertEqual(response.status_code, 404)

    def test_number_starts_with_a_lot_of_zeroes(self):
        response = Client().get('/catalog/001')
        self.assertEqual(response.status_code, 404)

    def test_number_starts_with_two_zeroes(self):
        response = Client().get('/catalog/00')
        self.assertEqual(response.status_code, 404)

    def test_number_starts_with_underscore(self):
        response = Client().get('/catalog/_01')
        self.assertEqual(response.status_code, 404)

    def test_strings_and_then_numbers(self):
        response = Client().get('/catalog/str123')
        self.assertEqual(response.status_code, 404)

    def test_string_with_leading_zeroes(self):
        response = Client().get('/catalog/00str')
        self.assertEqual(response.status_code, 404)

    def test_number_contains_string_inside(self):
        response = Client().get('/catalog/123str456')
        self.assertEqual(response.status_code, 404)

    def test_number_contains_underscore(self):
        response = Client().get('/catalog/123_455')
        self.assertEqual(response.status_code, 404)

    def test_underscope_at_the_end_of_number(self):
        response = Client().get('/catalog/123_')
        self.assertEqual(response.status_code, 404)

    def test_float_numbers_that_equals_to_integer(self):
        response = Client().get('/catalog/1.0')
        self.assertEqual(response.status_code, 404)

    def test_float_numbers(self):
        response = Client().get('/catalog/1.123')
        self.assertEqual(response.status_code, 404)

    def test_right_number(self):
        response = Client().get('/catalog/123')
        self.assertEqual(response.status_code, 200)

    def test_number_with_zeroes_at_the_end(self):
        response = Client().get('/catalog/100')
        self.assertEqual(response.status_code, 200)


class StaticUrlTests(TestCase):
    def test_catalog_init(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)
