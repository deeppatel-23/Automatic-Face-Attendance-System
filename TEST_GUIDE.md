# 🎓 Face Recognition Attendance System - Test Guide

## 📋 Test Student Account
**Login Credentials:**
- Email: `test@example.com`
- Password: `test123`
- Student ID: `TEST001`
- Name: John Doe (Test)

## 🔍 What to Test

### 1. Admin Features
**Login as Admin:**
- Email: `admin@attendance.com`
- Password: `admin123`

**Admin Dashboard:**
- View total students count
- See today's attendance summary
- Check current active session

**Students Management:**
- Go to "All Students" page
- Click on "John Doe (Test)" row to view detailed profile
- Check student photos (should show 5 photos in gallery)
- View attendance statistics and history
- Test "Remove Student" functionality

### 2. Student Features
**Login as Student:**
- Use test credentials above

**Student Dashboard:**
- View attendance statistics (cards showing sessions, present, absent, percentage)
- Check recent attendance records table
- During active session times, see "Mark Attendance" section

**Mark Attendance:**
- Click "Start Face Recognition"
- Allow camera access
- Look at camera and click "Capture & Mark"
- Should show success message and update attendance

### 3. Attendance Sessions
Available sessions:
- **Morning:** 08:00 - 09:00
- **Afternoon:** 13:00 - 14:00
- **Evening:** 17:00 - 18:00

### 4. Email Features
- Registration sends welcome email
- Attendance marking sends confirmation email
- Admin can mark absent students (sends bulk emails)

## ⚠️ Known Issues to Check
1. **Face Recognition:** May need debugging (photos are copied but recognition might fail)
2. **Photo Display:** Check if photos load correctly in student profiles
3. **Attendance Marking:** Test during actual session times
4. **Email Sending:** Verify if emails are being sent (check console for errors)

## 🛠️ Admin Testing Checklist
- [ ] Login as admin
- [ ] View admin dashboard stats
- [ ] Browse all students
- [ ] Click student profile and view photos
- [ ] Check attendance statistics
- [ ] Login as test student
- [ ] View student dashboard
- [ ] Test attendance marking (during session time)
- [ ] Check email notifications
- [ ] Test bulk import functionality
- [ ] Test attendance reports

## 📸 Photos Location
Test student photos are stored in: `static/images/students/10_*.jpg`

## 🔧 Quick Fixes Needed
1. Fix face recognition library issues
2. Update photo display URLs
3. Test email configuration
4. Verify camera permissions for attendance marking