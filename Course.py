import requests, json

class Course:
    def __init__(self, Semester="1131"):
        self.__URL = "https://querycourse.ntust.edu.tw/querycourse/api/courses"
        USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        self.__HEADERS = {"user-agent": USERAGENT, "content-type": "application/json; charset=utf-8"}
        self.__PAYLOAD = {
            'GE': {"Semester":Semester,"CourseNo":"","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":1,"OnleyNTUST":0,"OnlyMaster":0,"Language":"zh"},
            'LANG': {"Semester":Semester,"CourseNo":"","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":1,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyMaster":0,"Language":"zh"},
            'PE': {"Semester":Semester,"CourseNo":"PE","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyMaster":0,"Language":"zh"},
            'MAJOR': {"Semester":Semester,"CourseNo":"","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyUnderGraduate":0,"OnlyMaster":0,"Language":"zh"}
        }
    
    # ========================================
    def __get(self, payload):
        request = json.dumps(payload).encode("utf-8")
        try:
            response = requests.post(self.__URL, headers=self.__HEADERS, data=request)
            courses = json.loads(response.text)
            return courses
        except Exception:
            return None

    # ========================================
    def get_general(self, CourseName=''):
        payload = self.__PAYLOAD['GE']
        payload["CourseName"] = CourseName
        return self.__get(payload)
    
    def get_foreign_lang(self, CourseName=''):
        payload = self.__PAYLOAD['LANG']
        payload["CourseName"] = CourseName
        return self.__get(payload)

    def get_pe(self, CourseName=''):
        payload = self.__PAYLOAD['PE']
        payload["CourseName"] = CourseName
        return self.__get(payload)

    def get_major(self, CourseName='', CourseNo='ET'):
        payload = self.__PAYLOAD['MAJOR']
        payload["CourseName"] = CourseName
        payload["CourseNo"] = CourseNo
        return self.__get(payload)
    
    def get_master(self, CourseName='', CourseNo='ET'):
        payload = self.__PAYLOAD['MAJOR']
        payload["CourseName"] = CourseName
        payload["CourseNo"] = CourseNo
        payload["OnlyMaster"] = 1
        return self.__get(payload)
    
    # ========================================
    def analyze(self, courses):
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
    