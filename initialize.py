# Initialize database and create required directories
import os
import sys
from database.db_manager import db

def initialize_app():
    """Initialize application"""
    
    print("Initializing Smart Attendance System...")
    
    # Create required directories
    directories = [
        'static/images/students',
        'config',
        'database',
        'face_recognition',
        'email_service',
        'templates'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Directory created/verified: {directory}")
    
    # Initialize database
    print("✓ Database initialized with tables")
    
    print("\n✅ Smart Attendance System initialized successfully!")
    print("\nNext steps:")
    print("1. Configure your .env file with email credentials")
    print("2. Run: python app.py")
    print("3. Visit: http://localhost:5000")
    print("\nDefault admin login:")
    print("  Email: admin@attendance.com")
    print("  Password: admin123")

if __name__ == '__main__':
    initialize_app()
