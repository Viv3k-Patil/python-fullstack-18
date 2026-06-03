# Insert users data
INSERT INTO users(name, email, hashed_passward, role, campus_id, is_active, at_created)
VALUES
('Akshata', 'akshata@gmail.com', 123456, 'student', 1, true, true),
('Rahul', 'rahul@gmail.com', 456789, 'trainer', 1, true, true),
('Sneha', 'sneha@gmail.com', 789456, 'student', 2, true, true),
('Amit', 'amit@gmail.com', 852369, 'trainer', 3, true, true),
('Sameer', 'sameer@gmail.com', 963258, 'student', 1, true, true);
select * from users;

#--------------------------------------------------------------------------------------------------
# Insert campus data
INSERT INTO campus(name, city, address, cabin_count, is_active, created_at)
VALUES
('Pune Campus', 'Pune', 'Shivaji Nagar Pune', 20, true, CURRENT_DATE),
('Mumbai Campus', 'Mumbai', 'Andheri Mumbai', 15, true, CURRENT_DATE),
('Kolhapur Campus', 'Kolhapur', 'Rajarampuri Kolhapur', 10, true, CURRENT_DATE),
('Nagpur Campus', 'Nagpur', 'Sitabuldi Nagpur', 12, true, CURRENT_DATE),
('Nashik Campus', 'Nashik', 'College Road Nashik', 18, true, CURRENT_DATE);
select * from campus;

#--------------------------------------------------------------------------------------------------
# Insert cabin data
INSERT INTO cabin(campus_id, cabin_number, is_active)
VALUES
(1, 101, true),
(1, 102, true),
(2, 201, true),
(3, 301, true),
(4, 401, true);
select * from cabin;

#--------------------------------------------------------------------------------------------------
# Insert batch data
INSERT INTO batch(campus_id, name, course, start_date, end_date, is_active)
VALUES
(1, 'Python Batch A', 'Python Full Stack', '2026-01-01', '2026-06-01', true),
(2, 'Java Batch B', 'Java Full Stack', '2026-02-01', '2026-07-01', true),
(3, 'Data Science Batch', 'Data Science', '2026-03-01', '2026-08-01', true),
(4, 'MERN Stack Batch', 'MERN Stack', '2026-04-01', '2026-09-01', true),
(5, 'Testing Batch', 'Software Testing', '2026-05-01', '2026-10-01', true);
select * from batch;

#--------------------------------------------------------------------------------------------------
#  Insert student_profile data
INSERT INTO student_profile(user_id, batch_id, enrollment_number, skills)
VALUES
(1, 1, 'ENR101', 'Python, SQL'),
(3, 2, 'ENR102', 'Java, JDBC'),
(1, 3, 'ENR103', 'Machine Learning'),
(3, 4, 'ENR104', 'React, Node'),
(1, 5, 'ENR105', 'Manual Testing');
select * from student_profile;

#--------------------------------------------------------------------------------------------------
# Insert trainer_profile data 
INSERT INTO trainer_profile(user_id, skills, experience_years, rating, total_sessions)
VALUES
(2, 'Python, Django', 5, 4.5, 120),
(4, 'Java, Spring Boot', 7, 4.7, 150),
(2, 'SQL, PostgreSQL', 4, 4.3, 90),
(4, 'React, NodeJS', 6, 4.6, 110),
(2, 'Testing, Selenium', 3, 4.2, 80);
select * from trainer_profile;

#--------------------------------------------------------------------------------------------------
# Insert trainer_availability data
INSERT INTO trainer_availability(
    trainer_id,
    campus_id,
    date,
    start_time,
    end_time
)
VALUES
(1, 1, '2026-05-20', '10:00:00', '12:00:00'),
(2, 2, '2026-05-21', '11:00:00', '01:00:00'),
(3, 3, '2026-05-22', '09:00:00', '11:00:00'),
(4, 4, '2026-05-23', '02:00:00', '04:00:00'),
(5, 5, '2026-05-24', '03:00:00', '05:00:00');
select * from trainer_availability;

#--------------------------------------------------------------------------------------------------
# Insert file_metadata data
INSERT INTO file_metadata(
    student_id,
    student_name,
    stored_path,
    file_type,
    size_bytes,
    uploaded_at,
    is_active
)
VALUES
(1, 'Akshata', '/resume/akshata.pdf', 'pdf', 2048, CURRENT_DATE),
(2, 'Sneha', '/resume/sneha.pdf', 'pdf', 3024, CURRENT_DATE),
(3, 'Rahul', '/documents/rahul.docx', 'docx', 4096, CURRENT_DATE),
(4, 'Amit', '/certificates/amit.pdf', 'pdf', 5096, CURRENT_DATE),
(5, 'Priya', '/resume/priya.pdf', 'pdf', 2560, CURRENT_DATE);
select * from file_metadata;

#--------------------------------------------------------------------------------------------------
# Insert notification data 
INSERT INTO notification(
    user_id,
    type,
    title,
    message,
    is_read,
    metadata,
    created_at
)
VALUES
(1, 'Booking', 'Interview Scheduled', 'Your mock interview is scheduled.', false, 'Technical Round', CURRENT_DATE),
(2, 'Alert', 'Session Reminder', 'You have an interview session today.', false, 'Trainer Reminder', CURRENT_DATE),
(3, 'Booking', 'Interview Completed', 'Your interview has been completed.', true, 'HR Round', CURRENT_DATE),
(4, 'Update', 'Schedule Changed', 'Interview timing updated.', false, 'Rescheduled', CURRENT_DATE),
(5, 'Notice', 'Profile Updated', 'Your profile was updated successfully.', true, 'System Notification', CURRENT_DATE);
Select * from notification;

#--------------------------------------------------------------------------------------------------
# Insert booking data
INSERT INTO booking(
    student_id,
    trainer_id,
    cabin_id,
    campus_id,
    interview_type,
    status,
    scheduled_at,
    decline_count,
    created_at
)
VALUES
(1, 1, 1, 1, 'Technical', 'Scheduled', '2026-05-20', 0, CURRENT_DATE),
(2, 2, 2, 2, 'HR', 'Completed', '2026-05-21', 1, CURRENT_DATE),
(3, 3, 3, 3, 'Technical', 'Pending', '2026-05-22', 0, CURRENT_DATE),
(4, 4, 4, 4, 'Mock', 'Scheduled', '2026-05-23', 0, CURRENT_DATE),
(5, 5, 5, 5, 'Final', 'Completed', '2026-05-24', 2, CURRENT_DATE);
select * from booking;

#--------------------------------------------------------------------------------------------------
# Insert booking_history data
INSERT INTO booking_history(
    booking_id,
    trainer_id,
    action_data,
    reason,
    actioned_at
)
VALUES
(1, 1, 'Approved', 'Interview Scheduled', CURRENT_DATE),
(2, 2, 'Completed', 'Interview Successfully Completed', CURRENT_DATE),
(3, 3, 'Pending', 'Trainer Not Available', CURRENT_DATE),
(4, 4, 'Rescheduled', 'Student Request', CURRENT_DATE),
(5, 5, 'Rejected', 'Technical Issue', CURRENT_DATE);
select * from booking_history;