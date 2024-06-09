from Course import Course

def bachelor(course):
    print('type | 0:專業 1:通識 2:外語 3:體育')
    type = input('type: ')
    name = input('name: ')
    print('========================================')
    if (type == '0'): response = course.get_major(CourseName=name)
    elif (type == '1'): response = course.get_general(CourseName=name)
    elif (type == '2'): response = course.get_foreign_lang(CourseName=name)
    elif (type == '3'): response = course.get_pe(CourseName=name)
    else: exit("type error")
    message = course.analyze(response)
    print(message)

def master(course):
    file = './data.txt'
    try:
        with open(file, 'r') as f:
            CourseNos = f.read().splitlines()
    except:
        exit("file not found")
    data = []
    for CourseNo in CourseNos:
        data += course.get_master(CourseNo=CourseNo)
    message = course.analyze(data)
    print(message)

if __name__ == '__main__':
    course = Course(Semester="1131")
    # bachelor(course)
    master(course)
