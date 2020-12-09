# Seekhou-Aur-Sikhaou
This repository will be used to share the git repo of my Seekhou Aur Sikhaou LMS solution

## Inspiration 

## What it does - This is a learning management system that helps connects students, teachers and parents with each other. 
In total, there are 4 different types of users of this applications:
a. Admin - representing school management
b. Teachers 
c. Students
d. Parents 

Each of these user type have different privilege's that grant them different capabilities within the application, even though they all use the same urls. For example, admin staff have special rights to create users, create courses, and also to create sections for those courses. 

The main classes that this application uses are Users, Courses, Sections, Lectures, Lecture notes, comments, Assignments, Marks and submissions. 
Courses objects represent the overarching concept of a course, whereas Section objects represent individual sections that students can be enrolled in for that course. 
Lecture notes objects that the User (of teacher type) object has uploaded for the students to review, and Comment objects are follow up questions posed by Users (of student type) objects. 
Assignment objects are created by User (of teacher type) object, and then the Users (of student type) objects sends in their Submission objects. Once received the User (of teacher type) object can then review the submission and then reward marks to the Student. 

## How I built it - I built it using the Django framework. 

## Challenges I ran into - I have deployed this application using Heroku with a postgres database. Based on Heroku's specifications, I can not save files submitted by users in the Heroku filesystem. Based on my research, I will need to use AWS S3 bucket for this, but due to time limitations I was not able to do this. Therefore, I have removed the file upload and download feature from the web application for now. 

## Accomplishments that I'm proud of - Being a self-taught developer with just over a month of experience working with Django, and working on this project solo, I am happy that I was able to complete the major specifications of the application that I wanted to create at the start of the hackathon. 

## What I learned - I have learned object oriented programming in more detail. 

## What's next for Seekhou Aur Sikhaou
I will be performing the following:
a. Updating feature set of the application to make it more affective
b. Learning more about the needs of the market by talking to educators working in Karachi and beyond
c. Research existing solutions available in the market in Pakistan
d. Making the UX more appealing 

LOGIN INFORMATION FOR TESTING:
1. Admin account 
username: admin.account@gmail.com
password: admin.account

2. Teacher account
username: teacher.account@gmail.com
password: teacher.account

3. Parent account 
username: parent.account@gmail.com
password: parent.account

4. Student account 
username: student.account@gmail.com
password: student.account
