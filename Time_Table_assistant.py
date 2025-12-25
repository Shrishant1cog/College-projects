# college python project
# This small app checks the current time and tells which class is going on now and shows next class.

from datetime import datetime

# This takes the current date and time.
today = datetime.now()
now = datetime.now()

found = False   # It is used later to check if any class matched.

print("Current class teller".center(50,"-"))
print(f"Note: 1] This app tells the current period and next period according to your time table\n"
      f"2] You should enter the time table: ")

# Asking user about number of classes and breaks in a day.
tclass = int(input("How many classes are there in one day: "))
rest = int(input("How many breaks are there in on day(ex: short break ,lunch etc): "))

# creating Lists to store all timings and subject data.
starttime = []
endtime = []
timings = []
subjects = []

# creating Lists for each day.
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []

# Asking whether all days have same timings.
ask = input("Do you have same timings of daily classes?(yes/no): ").upper()

# ------------------ SAME TIMINGS FOR ALL DAYS ------------------
if ask in ["YES","Y","YE","S"]:

    print("Enter the monday timetable")

    # asking the start time, end time and subject for monday.
    for i in range(tclass):
        n = input(f"Starting Time of class {i+1}(ex,09:00): ")
        n1 = input(f"Ending Time of class {i+1}: ")
        n2 = input(f"Enter the subject of class {i+1}: ")

        starttime.append(n)
        endtime.append(n1)
        subjects.append(n2)

        # storing start & end together.
        monday.append([starttime[i], endtime[i]])

    # I am copying the mondays subject beause the timings are same. 
    msubjects = subjects.copy()
    subjects.clear()

    print("Enter the tuesday's timetable")
    for i in range(tclass):
        n2 = input(f"Subject of class {i+1}: ")
        subjects.append(n2)
        tuesday.append([starttime[i], endtime[i]])

    tsubjects = subjects.copy()
    subjects.clear()

    print("Enter the wednesday's timetable")
    for i in range(tclass):
        n2 = input(f"Subject of class {i+1}: ")
        subjects.append(n2)
        wednesday.append([starttime[i], endtime[i]])

    wsubjects = subjects.copy()
    subjects.clear()

    print("Enter the thursday's timetable")
    for i in range(tclass):
        n2 = input(f"Subject of class {i+1}: ")
        subjects.append(n2)
        thursday.append([starttime[i], endtime[i]])

    thsubjects = subjects.copy()
    subjects.clear()

    print("Enter the friday's timetable")
    for i in range(tclass):
        n2 = input(f"Subject of class {i+1}: ")
        subjects.append(n2)
        friday.append([starttime[i], endtime[i]])

    fsubjects = subjects.copy()
    subjects.clear()

    print("Enter the saturday's timetable")
    for i in range(tclass):
        n2 = input(f"Subject of class {i+1}: ")
        subjects.append(n2)
        saturday.append([starttime[i], endtime[i]])

    ssubjects = subjects.copy()
    subjects.clear()

    # Checking the present time.
    current_time = datetime.now()
    current_times = current_time.strftime("%H:%M")

    # Finding the current day and subject.
    for i in range(tclass):
        if current_time.weekday() == 0 and monday[i][0] < current_times < monday[i][1]:
            print("Current subject is ", msubjects[i])

        elif current_time.weekday() == 1 and tuesday[i][0] < current_times < tuesday[i][1]:
            print("Current subject is ", tsubjects[i])

        elif current_time.weekday() == 2 and wednesday[i][0] < current_times < wednesday[i][1]:
            print("Current subject is ", wsubjects[i])

        elif current_time.weekday() == 3 and thursday[i][0] < current_times < thursday[i][1]:
            print("Current subject is ", thsubjects[i])

        elif current_time.weekday() == 4 and friday[i][0] < current_times < friday[i][1]:
            print("Current subject is ", fsubjects[i])

        elif current_time.weekday() == 5 and saturday[i][0] < current_times < saturday[i][1]:
            print("Current subject is ", ssubjects[i])

        elif current_time.weekday() == 6:
            print("Enjoy your holiday but don't forget to revise")
            found = True

    if not found:
        print("Enjoy your holiday but don't forget to revise")