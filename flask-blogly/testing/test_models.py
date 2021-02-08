from unittest import TestCase

from app import app
from models import db, Users 


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False


app.config['TESTING'] = True


app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UsersModelTestCase(TestCase):
    """tests for model for Users"""
    

    def setUp(self):
        """clean up any existing pets"""
        Users.query.delete()

        user = Users(first_name="Daniel", last_name="Kim", img_url="shorturl.at/iFW07")
        db.session.add(user)
        db.session.commit()

        self.user_id=user.id
        # self.user=user

    def tearDown(self):
        """reset any changes made to db"""
        db.session.rollback()

    # def test_user_page(self):
    #     user = Users(first_name="Daniel", last_name="Kim", img_url="shorturl.at/iFW07")
    #     self.assertEquals(user.first_name = "Daniel")
    #     self.assertEquals(user.last_name = "Kim")
    #     self.assertEquals(user.img_url = "shorturl.at/iFW07")

    def test_user_page(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_test=True)
            self.assertEquals(res.status_code,200)
            self.asserIn('<ul id="user_list">',html)
    
    # # def test_new_user(self):
    # #     with app.test_client() as client:
    #         res = client.get('/users/new')
    #         html = res.get_data(as_test=True)
    #         self.assertEquals(res.status_code,200)
    #         self.asserIn('<input type="text" name="first" placeholder="First Name">',html)

    # def test_post_user(self):
    #     with app.test_client() as client:
    #         res = client.post('/users/new', data={"first_name":"Daniel", "last_name":"Kim", "img_url":"shorturl.at/iFW07"})
    #         html = res.get_data(as_test=True)
    #         self.assertEquals(res.status_code,301)
