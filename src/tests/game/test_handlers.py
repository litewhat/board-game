from unittest import TestCase

from game.handlers import Handler


class HandlerTestCase(TestCase):
    def test_create_handler_from_args(self):
        handler = Handler("id test handler", id)
        self.assertEqual(handler.name, "id test handler")
        self.assertEqual(handler.callable, id)

    def test_create_handler_from_kwargs(self):
        handler = Handler(name="print test handler", callable=print)
        self.assertEqual(handler.name, "print test handler")
        self.assertEqual(handler.callable, print)
