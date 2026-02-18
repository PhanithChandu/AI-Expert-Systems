% --------- STUDENT DATA ----------
student(s1, john).
student(s2, anna).
student(s3, rahul).

% --------- TEACHER DATA ----------
teacher(t1, smith).
teacher(t2, david).

% --------- SUBJECT DATA ----------
subject(cs101, 'Data_Structures').
subject(cs102, 'Operating_Systems').

% --------- TEACHES RELATION ----------
teaches(t1, cs101).
teaches(t2, cs102).

% --------- ENROLLMENT ----------
enrolled(s1, cs101).
enrolled(s2, cs101).
enrolled(s3, cs102).

% --------- RULES ----------

% Find teacher of a student
student_teacher(StudentName, TeacherName) :-
    student(SID, StudentName),
    enrolled(SID, SubCode),
    teaches(TID, SubCode),
    teacher(TID, TeacherName).

% Find subject taken by a student
student_subject(StudentName, SubjectName) :-
    student(SID, StudentName),
    enrolled(SID, SubCode),
    subject(SubCode, SubjectName).

% Find students taught by a teacher
teacher_students(TeacherName, StudentName) :-
    teacher(TID, TeacherName),
    teaches(TID, SubCode),
    enrolled(SID, SubCode),
    student(SID, StudentName).
