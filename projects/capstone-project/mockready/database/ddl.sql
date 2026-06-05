
# Create users table
CREATE TABLE users(

	  user_id Serial PRIMARY KEY ,
    NAME VARCHAR(50) not null,
    email VARCHAR(50) UNIQUE,
  	hashed_passward BIGINT not NULL,
    ROLE TEXT not NULL,
    campus_id INTEGER,
 	is_active BOOLEAN,
 	at_created BOOLEAN,

  user_id Serial PRIMARY KEY ,
  NAME VARCHAR(50) not null,
  email VARCHAR(50) UNIQUE,
  hashed_password VARCHAR(250) Not NULL,
  ROLE TEXT not NULL,
  campus_id INTEGER,
  is_active BOOLEAN,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

  
  FOREIGN key (campus_id) REFERENCES campus(campus_id)
);


# Create capmus table
CREATE TABLE campus(
          campus_id serial PRIMARY key,
          name VARCHAR(200) not NULL,
          city VARCHAR(50),
          address VARCHAR(200),
          cabin_count INTEGER,
          is_active BOOLEAN,
          created_at date 
);

# Create cabin table
CREATE TABLE cabin(
	cabin_id serial PRIMARY key,
    campus_id INTEGER,
  	cabin_number int not null,
    is_active BOOLEAN,
  
   FOREIGN key (campus_id) REFERENCES campus(campus_id)
);

# Create batch table
CREATE TABLE batch(
         batch_id serial PRIMARY KEY,
         campus_id INT, 
         name VARCHAR(200),
         course VARCHAR(50),
         start_date date,
         end_date date, 
         is_active BOOLEAN,
         FOREIGN key (campus_id) REFERENCES campus(campus_id)
);

# Create student_profile table
CREATE TABLE student_profile (
    student_id serial PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    batch_id INT REFERENCES batch(batch_id),
    enrollment_number VARCHAR(100),
    skills VARCHAR(200)
  );

# Create trainer_profile table
  CREATE TABLE trainer_profile (
    trainer_id serial PRIMARY KEY,
    user_id INT,
    skills TEXT,
    experience_years INT,
    rating DECIMAL(3, 2),
    total_sessions INT,
  
    FOREIGN KEY (user_id) REFERENCES users(user_id) 
);

# Create trainer_availability table
CREATE TABLE trainer_availability (
     trainer_availability_id serial PRIMARY KEY,
     trainer_id INT,
     campus_id INT,
     date DATE,
     start_time TIME,
     end_time TIME,
  
     FOREIGN KEY (trainer_id) REFERENCES trainer_profile(trainer_id),
     FOREIGN key (campus_id) REFERENCES campus(campus_id)
);

# Create file_metadata table
CREATE TABLE file_metadata(

          id serial PRIMARY KEY,
          student_id INT,
          student_name VARCHAR(100),
          stored_path VARCHAR(100),
          file_type VARCHAR(100),
          size_bytes INT,
          uploaded_at DATE,
        
         FOREIGN key (student_id) REFERENCES student_profile(student_id)

        file_metadata_id serial PRIMARY KEY,
        student_id INT,
        student_name VARCHAR(100),
        stored_path VARCHAR(100),
        file_type VARCHAR(100),
        size_bytes INT,
        uploaded_at DATE,
        is_active BOOLEAN,
        FOREIGN key (student_id) REFERENCES student_profile(student_id)

          
);

# Create notification table 
CREATE TABLE notification (
    notification_id serial PRIMARY KEY,
    user_id INT ,
    type TEXT,
    title TEXT,
    message TEXT,
    is_read BOOLEAN,
    metadata VARCHAR(200),
    created_at date,
  
    FOREIGN key (user_id) REFERENCES users(user_id)
);

# Create booking table 
CREATE TABLE booking (
    booking_id serial PRIMARY KEY,
    student_id INT,
    trainer_id INT,
    cabin_id INT,
    campus_id INT,
    interview_type VARCHAR(50),
    status VARCHAR(50),
    scheduled_at DATE,
    decline_count INT,
    created_at DATE,

    -- Foreign Keys
    FOREIGN KEY (student_id) REFERENCES student_profile(student_id),
    FOREIGN KEY (trainer_id) REFERENCES trainer_profile(trainer_id),
    FOREIGN KEY (cabin_id) REFERENCES cabin(cabin_id),
    FOREIGN KEY (campus_id) REFERENCES campus(campus_id)
);

 # Create booking_history table
CREATE TABLE booking_history (
    booking_history_id serial PRIMARY KEY,
    booking_id INT NOT NULL,
    trainer_id INT NOT NULL,
    action_data VARCHAR(100),
    reason TEXT,
    actioned_at DATE,
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id),
    FOREIGN KEY (trainer_id) REFERENCES trainer_profile(trainer_id)
);