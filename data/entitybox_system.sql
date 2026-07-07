CREATE DATABASE IF NOT EXISTS Score_prediction;
USE Score_prediction;


CREATE TABLE STUDENT
(
  student_id INT AUTO_INCREMENT,
  gender ENUM("male","female","other"),
  age INT NOT NULL CHECK(age >= 150),
  student_code INT NOT NULL,
  PRIMARY KEY (student_id)
)AUTO_INCREMENT = 20001;

CREATE TABLE COURSE
(
  score_exam FLOAT NOT NULL CHECK(score_exam <= 100),
  course_name ENUM("b.com","b.sc","b.tech","ba","bba","bca","diploma")  NOT NULL,
  difficulty ENUM("easy","hard","moderate") NOT NULL,
  course_id INT AUTO_INCREMENT,
  PRIMARY KEY (course_id)
)AUTO_INCREMENT = 20001;



CREATE TABLE EXTERNAL_FACTOR
(
  sleep_hours FLOAT NOT NULL CHECK(sleep_hours <= 36),
  facility_rating ENUM("high","low","medium") NOT NULL,
  internet_access ENUM("yes","no") NOT NULL,
  sleep_quality ENUM("average","good","poor") NOT NULL,
  external_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  PRIMARY KEY (external_id),
  FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
)AUTO_INCREMENT = 20001;

CREATE TABLE HABITS
(
  study_method ENUM("coaching","group study","mixed","online videos","self-study") NOT NULL,
  study_hours FLOAT NOT NULL CHECK(study_hours <= 48),
  class_attendance FLOAT NOT NULL CHECK(class_attendance <= 100),
  habit_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  PRIMARY KEY (habit_id),
  FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
)AUTO_INCREMENT = 20001;

CREATE TABLE ENROLLING
(
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
  FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
);
