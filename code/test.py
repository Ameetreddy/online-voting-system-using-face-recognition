import unittest
import pymysql
from main import mydb

class DatabaseTests(unittest.TestCase):

    def setUp(self):
        # Connect to the test database
        self.conn = pymysql.connect(host='localhost', user='root', password='', database='smart_voting_system')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the connection
        self.conn.close()

    def test_insert_nominee(self):
        # Test inserting a nominee
        sql = "INSERT INTO nominee (member_name, party_name, symbol_name) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, ('John Doe', 'Party A', 'logo.png'))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM nominee WHERE member_name='John Doe'")
        nominee = self.cursor.fetchone()
        self.assertIsNotNone(nominee)

    # Additional database tests...

if __name__== '_main_':
    unittest.main()