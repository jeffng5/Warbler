"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import db, User, Message, Follows

bcrypt = Bcrypt()

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-new"


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
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)


    def test_authenticate_user(self):
        """"Does user authentication check for valid user"""

        u = User.signup(
            "testuser",
            "test@test.com",
            "HASHED_PASSWORD", 
            'me.png'
        )

        self.assertEqual(User.authenticate("testuser", "HASHED_PASSWORD"), u)


    def test_invalid_user(self):
        """"Does user authentication check for invalid user"""

        u = User.signup(
            "testuser",
            "test@test.com",
            "HASHED_PASSWORD", 
            'me.png'
        )

        self.assertFalse(User.authenticate("testuser", "nothing"), u)