# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:00:28 2023

@author: pulik
"""

#%%

# Create dictionaries for course information

# Create a dictionary for course numbers and room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Create a dictionary for course numbers and instructor names
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Create a dictionary for course numebrs and meeting times
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompt the user for a course number
course_number = input("Enter a course number (e.g., CSC101):\n ")

# Display course information
if course_number in room_numbers:
    print("\nRoom Number:", room_numbers[course_number])
    print("\nInstructor:", instructors[course_number])
    print("\nMeeting Time:", meeting_times[course_number])
else:
    print("\nCourse not found.")
