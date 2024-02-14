from Course import Course
print('==============================')
print('type | 0:專業 1:通識 2:外語 3:體育')
TYPE = input('type: ')
KEYWORD = input('關鍵字: ')
print('==============================')

def analysis_Course(courses):
    count = 0
    message = ''
    for course in courses:
        amount1 = int(course["Restrict1"]) - int(course["ChooseStudent"])
        amount2 = int(course["Restrict2"]) - int(course["ChooseStudent"])
        amount = min(amount1, amount2)
        if (amount > 0 and amount < 500):
            count += 1
            message += f'No.{count}  ({course["Node"]})  {course["CourseName"]}\n'
            message += f'{course["CourseNo"]}  {course["CourseTeacher"]}\n'
            message += f'残り: {amount} '
            message += f'今: {course["ChooseStudent"]}\n\n'
    if (message == ''): message = None
    return message

if __name__ == '__main__':
    courses = None
    remote = Course(Semester="1122")
    if (TYPE == '0'): courses = remote.get_Major_Data(KEYWORD)
    elif (TYPE == '1'): courses = remote.get_General_Data(KEYWORD)
    elif (TYPE == '2'): courses = remote.get_ForeignLang_Data(KEYWORD)
    elif (TYPE == '3'): courses = remote.get_PE_Data(KEYWORD)
    else: exit("type 輸入錯誤")
    print(analysis_Course(courses))
