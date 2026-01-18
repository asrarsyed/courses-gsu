INSERT INTO students (stu_id, firstname, lastname, classify, address, city, state, zip, dept_id) 
VALUES
(1, 'Grace', 'Hopper', 'FRESHMAN', '8 Peachtree St. apt A-1', 'Atlanta', 'GA', '30303', 'CIS'),
(2, 'Charles', 'Babbage', 'SENIOR', '16 Appletree St. apt C-3', 'Hapeville', 'GA', '30305', 'MA'),
(3, 'Alan', 'Turing', 'JUNIOR', '32 Pecantree St. apt B-2', 'Lilburn', 'GA',  '30304', 'CS'),
(4, 'Ada', 'Lovelace', 'FRESHMAN', '64 Avacadotree St. apt d-4', 'Alpharetta', 'GA', '30306', 'CS');


INSERT INTO current_enrollments (dept_id, course_id, student_id) 
VALUES
('CIS', 1001, 1),
('MA', 101, 1),
('CS', 201, 4), 
('CS', 2301, 4),
('MA', 101, 3),
('EE', 1702, 3),
('MA', 101, 2),
('CIS', 1001, 2);

INSERT INTO course (dept_id, course_id, course_name, hours) 
VALUES
('CS', 101, 'CS Principles', 4),
('CS', 201, 'Algorithms', 4),
('CS', 202, 'Software Dev', 4),
('MA', 101, 'Algebra', 3),
('MA', 201, 'Calculus', 4),
('MA', 301, 'Analysis', 4),
('CIS', 312, 'Project Management', 4),
('EE', 102, 'Circuits', 4);


INSERT INTO current_enrollments 
VALUES
('CIS', 1001, 1),
('MA', 101, 1),
('CS', 201, 4),
('CS', 2301, 4),
('MA', 101, 3),
('EE', 1702, 3),
('MA', 101, 2),
('CIS', 1001, 2);

INSERT INTO department (dept_id, dept_name, chair, building, room) 
VALUES
('CS', 'computer science', 'Mikler', '25 Park Place', '700'),
('CIS', 'computer info systems', 'Robinson', '55 Park Place', '40'),
('MA', 'mathematics', 'Strange', '25 Park Place', '1500'),
('EE', 'electrical engineering', 'Codd', 'Petit Science Center', '400')
;