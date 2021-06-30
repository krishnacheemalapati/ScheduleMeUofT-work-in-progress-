import itertools
from courses import Course
from variables import course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24 

courses = [course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22, course23, course24]
print(courses)

for i0 in courses[0]:
  for i1 in courses[1]:
    for i2 in courses[2]:
      for i3 in courses[3]:
        for i4 in courses[4]:
          for i5 in courses[5]:
            for i6 in courses[6]:
              for i7 in courses[7]:
                for i8 in courses[8]:
                  for i9 in courses[9]:
                    for i10 in courses[10]:
                      for i11 in courses[11]:
                        for i12 in courses[12]:
                          possible = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12]
                          x = itertools.combinations(possible, len(courses))
                          for i in x:
                            print(i)
                            print("\n")