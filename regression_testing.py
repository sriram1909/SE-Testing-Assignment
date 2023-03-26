import unittest
import sqlite3
import index

class TestPublicArtRegistration(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('art.db')
        self.c = self.conn.cursor()
        self.c.execute('DELETE FROM art')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_submit_form(self):
        # Submit a registration form
        index.city_entry.insert(0, 'Delhi')
        index.artist_entry.insert(0, 'Jack Dorsy')
        index.title_entry.insert(0, 'Test Artwork')
        index.image_entry.insert(0, 'test_image.jpg')
        index.submit_form()

        # Check if the form was submitted successfully
        self.c.execute('SELECT * FROM art')
        result = self.c.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Delhi')
        self.assertEqual(result[2], 'Jack Dorsy')
        self.assertEqual(result[3], 'Test Artwork')
        self.assertEqual(result[4], 'test_img.jpg')

    def test_update_form(self):
        # Insert a record to be updated
        self.c.execute('''INSERT INTO art (city, artist_name, artwork_title, artwork_image)
                           VALUES (?, ?, ?, ?)''',
                      ('Kolkata', 'Jack Dorsy', 'Old Artwork', 'old_img.jpg'))
        self.conn.commit()

        # Update the record
        index.city_entry.insert(0, 'Mumbai')
        index.artist_entry.insert(0, 'Jane Doe')
        index.title_entry.insert(0, 'New Artwork')
        index.image_entry.insert(0, 'new_img.jpg')
        index.update_form()

        # Check if the record was updated successfully
        self.c.execute('SELECT * FROM art WHERE artwork_title = "New Artwork"')
        result = self.c.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Kolkata')
        self.assertEqual(result[2], 'Jack Dorsy')
        self.assertEqual(result[3], 'New Artwork')
        self.assertEqual(result[4], 'new_img.jpg')

if __name__ == '__main__':
    unittest.main()
