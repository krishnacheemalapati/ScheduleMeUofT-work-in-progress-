from courses import Course

class Course_list:
    def __init__(self, course_array):
        self.possible_schedules = []
        self.schedule_count = 1
        self.course_list = course_array
        all_timings = self.split_semesters()
        self.fall_courses = all_timings[0]
        self.winter_courses = all_timings[1]
        self.fall_integers = self.get_integers(self.fall_courses)
        self.winter_integers = self.get_integers(self.winter_courses)

    def split_semesters(self):
        fall_classes = []
        winter_classes = []
        for unconverted_class in self.course_list:
            if unconverted_class.semester == "Fall":
                fall_classes.append(unconverted_class)
            elif unconverted_class.semester == "Winter":
                winter_classes.append(unconverted_class)
            elif unconverted_class.semester == "Year":
                semester_halves = unconverted_class.convert_to_semesters()
                fall_classes.append(semester_halves[0])
                winter_classes.append(semester_halves[1])
            else:
                print("Bad semester value entered for " + unconverted_class.name)
                raise ValueError
        return [fall_classes, winter_classes]

    def get_integers(self, classes):
        integers = []
        for course in classes:
            integers.append(course.get_sections_integers())
        return integers

    def meeting_to_string(self, meeting):
        meeting_string = ""
        start = str(meeting[0])
        end = str(meeting[1])
        if start[0] == "1":
            meeting_string += "Monday "
        elif start[0] == "2":
            meeting_string += "Tuesday "
        elif start[0] == "3":
            meeting_string += "Wednesday "
        elif start[0] == "4":
            meeting_string += "Thursday "
        elif start[0] == "5":
            meeting_string += "Friday "
        else:
            print("Bad weekday")
            raise ValueError
        meeting_string += "from " + start[1:] + " to " + end[1:]
        return meeting_string

    def print_schedule(self, sections, semester):
        if self.schedule_count < 5:
            print("***********************************")
            print("POSSIBLE " + semester.upper() + " SCHEDULE #" + str(self.schedule_count))
            for index in range(len(sections)):
                if semester == "Fall":
                    course = self.fall_courses[index]
                elif semester == "Winter":
                    course = self.winter_courses[index]
                else:
                    print("Bad semester entered")
                    raise ValueError
                print(course.name)
                for meeting in sections[index]:
                    print(self.meeting_to_string(meeting))
                print("")

    def create_schedules(self, classes, semester):
        working_schedule = True
        self.schedule_count = 1
        for class1_sections in classes[0]:
            for class2_sections in classes[1]:
                for class3_sections in classes[2]:
                    for class4_sections in classes[3]:
                        for class5_sections in classes[4]:
                            for class6_sections in classes[5]:
                                for class7_sections in classes[6]:
                                    for class8_sections in classes[7]:
                                        for class9_sections in classes[8]:
                                            for class10_sections in classes[9]:
                                                for class11_sections in classes[10]:
                                                    for class12_sections in classes[11]:
                                                        possible_schedule = [class1_sections, class2_sections, class3_sections, class4_sections, class5_sections, class6_sections, class7_sections, class8_sections, class9_sections, class10_sections, class11_sections, class12_sections]
                                                        possible_schedule[:] = (section for section in possible_schedule if section != [])
                                                        for section in possible_schedule:
                                                            other_sections = possible_schedule.copy()
                                                            other_sections.remove(section)
                                                            for other_section in other_sections:
                                                                working_schedule = not Course.overlaps(section, other_section)
                                                                if not working_schedule:
                                                                    break
                                                            if not working_schedule:
                                                                break
                                                        if working_schedule:
                                                            self.print_schedule(possible_schedule, semester)
                                                            self.schedule_count += 1
                                                            possible_schedule = []
                                                        else:
                                                            working_schedule = True
        if self.schedule_count == 1:
          print("No schedule can be created with these courses.")
