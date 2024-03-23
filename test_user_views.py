import os
from unittest import TestCase

from models import db, connect_db, Message, User

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-new"

from app import app, CURR_USER_KEY

db.create_all()



app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)

        db.session.commit()

    def login(self):
        

        # Since we need to change the session to mimic logging in,
        # we need to use the changing-session trick:

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

         
            self.assertIsNotNone(sess)

            
    def logout(self):

        self.assertIs(self.client, None)


    def users_profile(self):
        self.assertIsNotNone(self.client)
        with app.test_client() as client:
            resp = client.get("/users/profile")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIsNotNone(html)

    
    def users_following(self):
        self.assertIsNotNone(self.client)

    def users_delete(self):
        self.assertIsNotNone(self.client)
        with app.test_client() as client:
            resp = client.get("/signup")

            self.assertEqual(resp.status_code, 200)
        
        