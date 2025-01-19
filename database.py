import sqlite3
import os

class Database:
    def __init__(self):
        self.db_file = 'mydatabase.db'
        self.initialize_database()
        
    def initialize_database(self):
        """Initialize the database with required tables"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                
                # Create users table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    mobile TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                ''')
                
                # Create skintypes table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS skintypes (
                    skintype_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    skintype TEXT NOT NULL,
                    ingredient TEXT NOT NULL
                )
                ''')
                
                # Create concerns table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS concerns (
                    concern_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    concern TEXT NOT NULL,
                    ingredient TEXT NOT NULL
                )
                ''')

                conn.commit()
                
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}") 
            
            
    def add_user(self, username, email, password, mobile):
        """Add a new user to the database"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO users (username, email, password, mobile)
                VALUES (?, ?, ?, ?)
                ''', (username, email, password, mobile))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False  # Username or email already exists
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            return False 
        
    def authenticate_user(self, username, password):
        """Authenticate a user's login credentials"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                SELECT user_id FROM users 
                WHERE username = ? AND password = ?
                ''', (username, password))
                result = cursor.fetchone()
                return result is not None
        except sqlite3.Error as e:
            print(f"Authentication error: {e}")
            return False  
        
    def update_password(self, email, new_password):
        """Update a user's password"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                UPDATE users 
                SET password = ?
                WHERE email = ?
                ''', (new_password, email))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Password update error: {e}")
            return False  
        
    def check_email_exists(self, email):
        """Check if email exists in database"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT email FROM users WHERE email = ?', (email,))
                return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Error checking email: {e}")
            return False
        
    def add_skintype_ingredient(self, skintype, ingredient):
        """Add a skintype-ingredient relationship"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO skintypes (skintype, ingredient)
                VALUES (?, ?)
                ''', (skintype, ingredient))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error adding skintype ingredient: {e}")
            return False
        
    def add_concern_ingredient(self, concern, ingredient):
        """Add a concern-ingredient relationship"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO concerns (concern, ingredient)
                VALUES (?, ?)
                ''', (concern, ingredient))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error adding concern ingredient: {e}")
            return False
        
    def get_ingredients_by_type(self, skintype):
        """Get ingredients for a specific skin type"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                SELECT DISTINCT ingredient FROM skintypes 
                WHERE skintype = ?
                ''', (skintype,))
                return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting skintype ingredients: {e}")
            return []
        
    def get_ingredients_by_concern(self, concern):
        """Get ingredients for a specific skin concern"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                SELECT DISTINCT ingredient FROM concerns 
                WHERE concern = ?
                ''', (concern,))
                return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting concern ingredients: {e}")
            return []
        
# Create global database instance
db = Database()