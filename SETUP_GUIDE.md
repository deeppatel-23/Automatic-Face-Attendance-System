# Smart Attendance System with Face Recognition

This is the fully implemented Smart Attendance System with Face Recognition.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

**Note for Windows users:** If you have issues installing face_recognition, try:
```bash
pip install cmake
pip install dlib
pip install face_recognition
```

### 2. Configure Environment

Edit the `.env` file with your settings:
- Set your Gmail credentials for email notifications
- Configure a strong SECRET_KEY

### 3. Run the Application
```bash
python app.py
```

The application will be available at: **http://localhost:5000**

## Default Login Credentials

**Admin Account:**
- Email: `admin@attendance.com`
- Password: `admin123`

⚠️ **Important:** Change these credentials before deploying to production!

## Project Structure

The project is organized as follows:

```
d:\face\
├── app.py                          # Main Flask application
├── requirements.txt                # Dependencies
├── .env                            # Environment variables
│
├── config/
│   └── config.py                   # Configuration settings
│
├── database/
│   └── db_manager.py               # Database models and operations
│
├── face_recognition/
│   └── face_detector.py            # Face detection and recognition
│
├── email_service/
│   └── email_sender.py             # Email notification service
│
├── static/
│   ├── css/
│   │   └── style.css               # CSS styles
│   ├── js/
│   │   └── script.js               # JavaScript utilities
│   └── images/
│       └── students/               # Student photos directory
│
├── templates/
│   ├── base.html                   # Base template
│   ├── index.html                  # Home page
│   ├── login_page.html             # Login page
│   ├── register_page.html          # Registration page
│   ├── student_dashboard.html      # Student dashboard
│   ├── admin_dashboard.html        # Admin dashboard
│   ├── admin_students.html         # View all students
│   ├── attendance_report.html      # Attendance reports
│   ├── 404.html                    # 404 error page
│   └── 500.html                    # 500 error page
│
└── attendance.db                   # SQLite database (auto-created)
```

## Features Implemented

### ✅ Student Features
- User registration with face photo upload
- Face recognition-based attendance marking
- Personal dashboard with attendance statistics
- View attendance history
- Email notifications for attendance confirmation
- Real-time session tracking

### ✅ Admin Features
- Complete attendance management
- View all registered students
- Mark absent students and send bulk emails
- Generate attendance reports with date range selection
- Dashboard with real-time statistics
- View student photos and details

### ✅ System Features
- **Face Recognition**: Using face_recognition library with OpenCV
- **Time-based Sessions**: Morning (08:00-09:00), Afternoon (13:00-14:00), Evening (17:00-18:00)
- **Email Notifications**: Automated emails for attendance confirmation and absence notifications
- **Secure Authentication**: Password hashing using Werkzeug
- **SQLite Database**: For data persistence
- **Responsive Bootstrap UI**: Modern, mobile-friendly interface
- **Session Management**: Flask session management with 1-hour timeout

## Configuration

### Attendance Sessions
Edit `config/config.py` to modify session times:

```python
ATTENDANCE_SESSIONS = {
    'morning': {'start': '08:00', 'end': '09:00'},
    'afternoon': {'start': '13:00', 'end': '14:00'},
    'evening': {'start': '17:00', 'end': '18:00'}
}
```

### Face Recognition Tolerance
Adjust recognition strictness (0.0-1.0, lower = more strict):

```python
TOLERANCE = 0.6
```

## Email Configuration

To enable email notifications:

1. **Gmail Setup:**
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification
   - Create an App Password
   - Copy the password to `.env` file

2. **Environment Variables (.env):**
   ```env
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   SECRET_KEY=your-secret-key
   ```

## API Endpoints

### Public Routes
- `GET /` - Home page
- `GET/POST /login` - Login
- `GET/POST /register` - Student registration
- `GET /logout` - Logout

### Student Routes
- `GET /student/dashboard` - Student dashboard
- `POST /mark_attendance` - Mark attendance via face recognition

### Admin Routes
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/students` - View all students
- `POST /admin/mark_absent` - Mark absent students and send emails
- `GET /attendance_report` - Attendance report page
- `GET /api/attendance_data` - Get attendance data for reports

## Troubleshooting

### Face Recognition Issues
- Ensure good lighting
- Look directly at the camera
- Avoid masks or sunglasses
- Check webcam is accessible

### Email Not Working
- Verify Gmail app password in .env
- Check spam folder
- Ensure 2-Step Verification is enabled

### Camera Access Issues
- Check browser permissions
- Try another browser
- Ensure webcam is not in use by another app

### Database Issues
- Delete `attendance.db` to reset the database
- Check file permissions in the directory

## Security Notes

Before deploying to production:

1. Change admin default credentials
2. Generate a strong SECRET_KEY
3. Use HTTPS only
4. Set Flask DEBUG=False
5. Use PostgreSQL instead of SQLite
6. Secure the `.env` file (add to .gitignore)

## Dependencies

- Flask 2.3.0
- Python-dotenv
- OpenCV
- face_recognition
- Pillow
- Werkzeug

## Support & Issues

For troubleshooting, refer to:
- Check logs in Flask console
- Verify `.env` file configuration
- Ensure all packages are installed
- Check database connectivity

## Future Enhancements

- [ ] Multi-camera support
- [ ] Mobile app
- [ ] Advanced analytics
- [ ] Export to Excel/PDF
- [ ] SMS notifications
- [ ] Geolocation verification
- [ ] Integration with LMS

---

**Created:** 2026  
**Smart Attendance System with Face Recognition**
