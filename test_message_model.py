import os
from unittest import TestCase
import datetime
from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///postgres"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
   
        m = Message(
            text ="I am Sam",
            timestamp = datetime.datetime.now(),
            user_id = 
            
        )

        db.session.add(m)
        db.session.commit()

    
        self.assertEqual(len(m.text), 0)
        self.assertEqual(len(m.user_id), 0)