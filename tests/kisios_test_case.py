from unittest import TestCase
from kisios.app import app, activate_testing_mode


class KisiosTestCase(TestCase):

    def _clean_test_database(self):
        pass

    def __call__(self, result=None):
        self._pre_setup()
        super(KisiosTestCase, self).__call__(result)
        self._post_tearDown()

    def _pre_setup(self):
        activate_testing_mode()
        if app.config['TESTING'] is False:
            raise RuntimeError('Running unit test without TESTING=True in configuration. Aborting.')
        self.app = app
        self.client = app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()

    def _post_tearDown(self):
        self._ctx.pop()
        self._clean_test_database()
