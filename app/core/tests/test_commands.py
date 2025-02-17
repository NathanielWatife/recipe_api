"""Test custom Django managements commands"""
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from djang.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test for commands"""
    def test_wait_for_db_ready(self, patched_check):
        """Wating for db"""
        patched_check.return_value = True

        call_command('wait_for_db')
        patched_check.assert_called_once_with(database=['default'])
    