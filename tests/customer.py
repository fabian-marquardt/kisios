from mixer.backend.flask import mixer

from kisios.models import Customer
from tests.kisios_test_case import KisiosTestCase


class CustomerTestCase(KisiosTestCase):
    def test_create_customer(self):
        mixer.blend(Customer)

    def test_get_name_full(self):
        customer = mixer.blend(Customer, first_name="Test", last_name="Customer")
        self.assertEqual(customer.get_name(), "Test Customer")

    def test_get_name_first_only(self):
        customer = mixer.blend(Customer, first_name="Test")
        self.assertEqual(customer.get_name(), "Test")

    def test_get_name_last_only(self):
        customer = mixer.blend(Customer, first_name="Customer")
        self.assertEqual(customer.get_name(), "Customer")

    def test_get_name_anonymous(self):
        customer = mixer.blend(Customer)
        self.assertEqual(customer.get_name(), "Anonymous customer")

    def test_is_initialized_with_zero_balance(self):
        customer = mixer.blend(Customer)
        self.assertEqual(customer.balance, 0)

    def test_is_direct_access_to_balance_forbidden(self):
        customer = mixer.blend(Customer)
        with self.assertRaises(RuntimeError):
            customer.balance = 100
