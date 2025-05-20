import unittest
from unittest.mock import patch, MagicMock
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    @patch('app.get_db_connection')
    def test_register_user_success(self, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = None  # Usuario no existe

        response = self.client.post('/register', data={
            'usuario': 'testuser',
            'password': '1234',
            'nombre': 'Test User'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'login', response.data)

    @patch('app.get_db_connection')
    def test_register_user_duplicate(self, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = (1,)  # Usuario ya existe

        response = self.client.post('/register', data={
            'usuario': 'existinguser',
            'password': '1234',
            'nombre': 'Existing User'
        })

        self.assertIn(b"El usuario ya existe", response.data)

    @patch('app.get_db_connection')
    def test_login_success(self, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = (1, 'testuser', 'hashedpwd')  # Simula usuario encontrado

        response = self.client.post('/login', data={
            'usuario': 'testuser',
            'password': '1234'
        }, follow_redirects=True)

        self.assertIn(b'Bienvenido', response.data)

    @patch('app.get_db_connection')
    def test_login_failure(self, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = None  # Usuario no encontrado

        response = self.client.post('/login', data={
            'usuario': 'baduser',
            'password': 'wrong'
        })

        self.assertIn(b'Credenciales incorrectas', response.data)

    def test_home_requires_login(self):
        response = self.client.get('/home', follow_redirects=True)
        self.assertIn(b'login', response.data)

    def test_logout_clears_session(self):
        with self.client as client:
            with client.session_transaction() as session:
                session['usuario'] = 'testuser'

            response = client.get('/logout', follow_redirects=True)
            self.assertIn(b'login', response.data)

if __name__ == '__main__':
    unittest.main()
