# Smart Attendance System - Complete Installation & Usage Guide

## 📋 Project Overview

This is a complete **Smart Attendance System with Face Recognition** built with Flask, OpenCV, and SQLite. It provides:

- ✅ **Student Features**: Face recognition attendance marking, dashboard, email notifications
- ✅ **Admin Features**: Attendance management, student management, bulk operations, reporting
- ✅ **System Features**: Secure authentication, time-based sessions, automated emails, responsive UI

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
cd d:\face
pip install -r requirements.txt
```

**For Windows users with dlib issues:**
```bash
pip install cmake
pip install dlib
pip install face_recognition
```

### Step 2: Configure Environment
Edit `.env` file with your Gmail credentials:
```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
SECRET_KEY=change-me-in-production
```

### Step 3: Run Application
```bash
python app.py
```

Visit: **http://localhost:5000**

---

## 🔑 Default Credentials

**Admin Account:**
- Email: `admin@attendance.com`
- Password: `admin123`

**⚠️ Important:** Change these credentials before production deployment!

---

## 📁 Project Structure

```
d:\face/
│
├── app.py                          # Main Flask application (250+ lines)
├── initialize.py                   # Database initialization script
├── requirements.txt                # Python dependencies
├── .env                            # Environment configuration (create/edit this)
├── .gitignore                      # Git ignore rules
│
├── config/
│   ├── __init__.py
│   └── config.py                   # Configuration class (50+ lines)
│
├── database/
│   ├── __init__.py
│   └── db_manager.py               # Database management (200+ lines)
│
├── face_recognition/
│   ├── __init__.py
│   └── face_detector.py            # Face recognition engine (180+ lines)
│
├── email_service/
│   ├── __init__.py
│   └── email_sender.py             # Email service (120+ lines)
│
├── static/
│   ├── css/
│   │   └── style.css               # Bootstrap + custom styles (80+ lines)
│   ├── js/
│   │   └── script.js               # JavaScript utilities (60+ lines)
│   └── images/
│       └── students/               # Student photos storage
│
├── templates/
│   ├── base.html                   # Base template with navbar
│   ├── index.html                  # Home page
│   ├── login_page.html             # Login form
│   ├── register_page.html          # Registration with photo upload
│   ├── student_dashboard.html      # Student dashboard (attendance marking)
│   ├── admin_dashboard.html        # Admin dashboard
│   ├── admin_students.html         # Student list
│   ├── attendance_report.html      # Report generation
│   ├── 404.html                    # Error page
│   └── 500.html                    # Error page
│
└── readme.md                       # Original project specification
```

---

## 🎯 Feature Guide

### For Students

#### 1. Registration
- Navigate to `/register`
- Enter: Student ID, Name, Email, Password
- Upload a clear face photo
- System extracts and stores face encoding

#### 2. Login
- Email & password authentication
- Redirects to student dashboard

#### 3. Mark Attendance
- Click "Start Face Recognition" during active session
- Allow camera access
- Look at webcam
- Face recognized → Attendance marked automatically
- Receive confirmation email

#### 4. Dashboard
- View attendance statistics (total, present, absent, percentage)
- Recent attendance history
- Current session information

### For Administrators

#### 1. Admin Dashboard
- Total students count
- Today's attendance count
- Current session information
- Quick action buttons

#### 2. Student Management
- View all registered students
- See student photos
- View student details (email, registration date)

#### 3. Attendance Management
- Mark absent students for a session
- Automatically sends email to absent students
- Bulk operations available

#### 4. Reports
- Select date range
- Generate attendance reports
- View per-student attendance statistics
- See present/absent counts

---

## ⚙️ Configuration

### Email Setup (Gmail)

1. Go to: https://myaccount.google.com/security
2. Enable "2-Step Verification"
3. Create "App Password" (Select Mail, Windows/PC)
4. Copy the generated password
5. Update `.env` file

### Attendance Sessions (Edit config/config.py)

```python
ATTENDANCE_SESSIONS = {
    'morning': {'start': '08:00', 'end': '09:00'},
    'afternoon': {'start': '13:00', 'end': '14:00'},
    'evening': {'start': '17:00', 'end': '18:00'}
}
```

### Face Recognition Tolerance (config/config.py)

```python
TOLERANCE = 0.6  # Range: 0.0-1.0, lower = stricter
```

---

## 🔌 API Endpoints

### Authentication
- `POST /login` - Student/Admin login
- `POST /register` - Student registration
- `GET /logout` - Logout and clear session

### Student Routes
- `GET /student/dashboard` - View dashboard
- `POST /mark_attendance` - Mark attendance (JSON with base64 image)

### Admin Routes
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/students` - List all students
- `POST /admin/mark_absent` - Mark absent & send emails
- `GET /attendance_report` - Report page
- `GET /api/attendance_data` - Get report data (JSON)

---

## 🗄️ Database Schema

### Users Table
- id, student_id, name, email, password (hashed), face_encoding, photo_path, role, created_at

### Attendance Table
- id, user_id, date, session, status, time_marked

### Sessions Table
- id, name, date, start_time, end_time, created_at

---

## 🐛 Troubleshooting

### Face Recognition Not Working
- ✓ Good lighting required
- ✓ Look directly at camera
- ✓ Remove masks/sunglasses
- ✓ Check webcam access permission
- ✓ Try multiple angles
- ✓ Adjust tolerance in config if needed

### Email Issues
- ✓ Verify Gmail app password in .env
- ✓ Check email is correct
- ✓ Ensure 2-Step Verification is enabled
- ✓ Check spam folder
- ✓ Wait 10-15 seconds for delivery

### Database Errors
- ✓ Delete attendance.db file
- ✓ Restart Flask app
- ✓ Check write permissions

### dlib Installation
- ✓ Install cmake: `pip install cmake`
- ✓ Then install: `pip install dlib`
- ✓ May require C++ build tools on Windows

---

## 🔒 Security Checklist

Before Production:
- [ ] Change admin credentials
- [ ] Generate strong SECRET_KEY
- [ ] Enable HTTPS
- [ ] Set DEBUG=False
- [ ] Use PostgreSQL instead of SQLite
- [ ] Add .env to .gitignore
- [ ] Use environment variables for sensitive data
- [ ] Add password validation rules
- [ ] Implement rate limiting
- [ ] Add CSRF protection

---

## 📦 Dependencies

```
Flask==2.3.0                      # Web framework
Flask-Session==0.5.0              # Session management
python-dotenv==1.0.0              # Environment variables
opencv-python==4.8.0.76           # Computer vision
face-recognition==1.3.5           # Face detection/recognition
numpy==1.24.0                     # Numerical computations
Pillow==10.0.0                    # Image processing
Werkzeug==2.3.0                   # Password hashing
```

---

## 🎨 UI Features

- Bootstrap 5 responsive design
- Dark navbar with navigation
- Cards with hover effects
- Tables with striping
- Progress indicators
- Flash messages with auto-dismiss
- Badge status indicators
- Camera integration
- Real-time statistics

---

## 📊 Data Flow

```
Student Registration
    ↓
[Upload Photo] → [Extract Face Encoding] → [Store in DB]
    ↓
Student Login → [Face Recognition] → [Mark Attendance]
    ↓
[Email Confirmation] ← [Database Update]

Admin Dashboard
    ↓
[View Statistics] ← [Database Query]
    ↓
[Generate Reports] → [Export Data]
    ↓
[Mark Absent] → [Send Bulk Emails]
```

---

## 🚀 Deployment Tips

### Local Testing
```bash
python app.py
# Access at http://localhost:5000
```

### Production Deployment
1. Use production WSGI server (Gunicorn, uWSGI)
2. Set up Nginx reverse proxy
3. Use PostgreSQL database
4. Enable HTTPS with SSL certificates
5. Set environment variables securely
6. Use process manager (systemd, supervisor)
7. Implement logging and monitoring

### Example with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📞 Support

### Common Issues & Solutions

**Q: Camera not found**
A: Check browser permissions, ensure webcam is not in use

**Q: Face not recognized**
A: Ensure good lighting, clear face visibility, try from different angle

**Q: Emails not sending**
A: Verify Gmail credentials, check spam folder, wait 10-15 seconds

**Q: Database locked**
A: Delete attendance.db and restart

---

## 📝 Notes

- Face encodings are stored as text (for simplicity)
- Photos stored in static/images/students/
- Session timeout: 1 hour
- All passwords are hashed using Werkzeug
- Email notifications are sent immediately
- Database auto-creates on first run

---

## 🎓 Learning Resources

- Flask: https://flask.palletsprojects.com/
- face_recognition: https://github.com/ageitgey/face_recognition
- OpenCV: https://opencv.org/
- Bootstrap: https://getbootstrap.com/

---

**Version:** 1.0  
**Last Updated:** January 2026  
**Status:** ✅ Complete & Ready for Use

