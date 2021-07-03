from course_list import Course_list
#from variables import course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24
#from test2 import course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24
from test4 import course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24, course25

#For normal use
#courses = Course_list([course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24])

#For test1
#courses = Course_list([course1, course2, course3, course4, course5, course6, course13, course14, course15, course16, course17, course18, course7, course8, course9, course10, course11, course12, course19, course20, course21, course22, course23, course24])

#For test2
#courses = Course_list([course1, course2, course5, course6, course8, course11, course12, course3, course4, course7, course9, course10, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24])

#For test3/4
courses = Course_list([course1, course2, course5, course6, course8, course11, course12, course3, course4, course7, course9, course10, course25, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24])

courses.create_schedules(courses.fall_integers, "Fall")
courses.create_schedules(courses.winter_integers, "Winter")
