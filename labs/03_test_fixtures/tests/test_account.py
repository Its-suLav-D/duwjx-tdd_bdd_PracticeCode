"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):     # runs once before test case 
        """ Connect and load data needed by tests """
        global ACCOUNT_DATA 

        with open('tests/fixtures/account_data.json') as json_data: 
            ACCOUNT_DATA = json.load(json_data)

        db.create_all() 

    @classmethod
    def tearDownClass(cls):  # runcs once after test case 
        """Disconnect from database"""
        db.session.close()

    def setUp(self): # runs before each test 
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self): # runs after each test 
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_account(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        account.create()
        self.assertIsNotNone(account.id)
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_accounts(self):
        for account in ACCOUNT_DATA:
            account = Account(**account)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))
