class Course:
    def __init__(self, name, semester, section_timings):
        self.name = name
        self.semester = semester
        self.section_timings = section_timings
        self.section_integers = self.get_sections_integers(section_timings)
# note to self:
# timings = [[name], [day start end], [day start end]]
    def get_sections_integers():
        sections_integers = []
        for index1 in range(1, len(self.section_timings)):
            meetings = []
            for index2 in range(1, len(self.section_timings[index])):
                unconverted = self.section_timings[index1]
                weekday_int = self.weekday_to_number(unconverted[0])
                start_time = weekday_int*10000 + unconverted[1]
                end_time = weekday_int*10000 + unconverted[2]
                meetings.append([start_time, end_time])
            section_integers.append(meetings)
        return section_integers

    def weekday_to_number(self, weekday):
        if weekday == "Monday":
            return 1
        if weekday == "Tuesday":
            return 2
        if weekday == "Wednesday":
            return 3
        if weekday == "Thursday":
            return 4
        if weekday == "Friday":
            return 5
        else:
            print("Bad weekday entered for " + self.name)
            raise ValueError

    def convert_to_semesters(self):
        if self.semester == "Year":
            fall_version = Course(self.name + " FALL", "Fall", self.section_timings)
            winter_version = Course(self.name + " WINTER", "Winter", self.section_timings)
            return [fall_version, winter_version]
        else:
            print(self.name + " is not a year-long course")
            raise ValueError

    def doesnt_overlap(section1_times, section2_times):
        for meeting1 in section1_times:
            for meeting2 in section2_times:
        #if one starts/ends during the other or they take place at the exact same timings
                if(meeting1[0] < meeting2[0] < meeting1[1]) or (meeting1[0] < meeting2[1] < meeting1[1]) or (meeting1[0] == meeting2[0] and meeting1[1] == meeting2[1]):
                    return False
                else:
                    return True
