from database.db_manager import db
import os
import glob
from config.config import Config

print('🎓 FACE RECOGNITION ATTENDANCE SYSTEM - TEST DEMO')
print('=' * 60)

# 1. Check test student
print('\n1️⃣ TEST STUDENT INFO:')
user = db.get_user_by_student_id('TEST001')
if user:
    print(f'   ✅ Student ID: {user["student_id"]}')
    print(f'   ✅ Name: {user["name"]}')
    print(f'   ✅ Email: {user["email"]}')
    print(f'   ✅ Role: {user["role"]}')
    print(f'   ✅ Registered: {user["created_at"]}')
    print(f'   ✅ Has Photo: {"Yes" if user["photo_path"] else "No"}')
else:
    print('   ❌ Test student not found')

# 2. Check admin
print('\n2️⃣ ADMIN ACCOUNT:')
admin = db.get_user('admin@attendance.com')
if admin:
    print(f'   ✅ Admin Email: {admin["email"]}')
    print(f'   ✅ Admin Password: admin123')
else:
    print('   ❌ Admin not found')

# 3. Check photos
print('\n3️⃣ STUDENT PHOTOS:')
photos = glob.glob('static/images/students/10_*.jpg')
print(f'   📸 Test student has {len(photos)} photos:')
for photo in photos[:3]:  # Show first 3
    print(f'      - {os.path.basename(photo)}')

# 4. Check attendance sessions
print('\n4️⃣ ATTENDANCE SESSIONS:')
for session_name, times in Config.ATTENDANCE_SESSIONS.items():
    print(f'   🕐 {session_name.capitalize()}: {times["start"]} - {times["end"]}')

print('\n' + '=' * 60)
print('🚀 HOW TO TEST THE SYSTEM:')
print('1. Login as admin: admin@attendance.com / admin123')
print('2. Go to Admin Students page')
print('3. Click on "John Doe (Test)" to view profile')
print('4. Check photos and attendance stats')
print('5. Login as student: test@example.com / test123')
print('6. Try marking attendance during active session')
print('7. Check admin dashboard for attendance reports')
print('\n⚠️  Note: Face recognition may need debugging')
print('=' * 60)