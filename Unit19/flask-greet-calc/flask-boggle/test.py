from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        with app.test_client() as client:
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test that the homepage is working correctly"""
        with app.test_client() as client:
            res = client.get("/")
            self.assertIn(None, session)
            self.assertIn("Let's Play Boggle!")
            self.assertEqual(res.status_code, 200)

    def test_play_boggle(self):
        """test that the /play page loads correctly"""
        with app.test_client() as client:
            res = client.get("/")
            self.assertIn("board", session)
            self.assertIn("nplays", session)

    def test_valid_word(self):
        """Test findword function with a real word that is on board. Should return 'ok'"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["board"] = [
                    [A, B, C, D, E]
                    [F, O, R, K, J]
                    [K, L, M, N, O]
                    [P, Q, R, S, T]
                    [U, V, X, Y, Z]
                ]
            res = client.get("/check-word?guess=fork")
            self.assertEqual(response.json["result"], "ok")

    def test_invalid_word(self):
        """Test findword function with word not on board. Should return 'not-on-board'"""
        with app.test_client() as client:
            self.client.get("/play")
            res = client.get("/check-word?guess=aardvark")
            self.assertEqual(response.json["result"], "not-on-board")

    def test_fake_word(self):
    """Test findword function with a fake word. Should return 'not-word'"""
    with app.test_client() as client:
        self.client.get("/play")
        res = client.get("/check-word?guess=aardichoke")
        self.assertEqual(response.json["result"], "not-word")
