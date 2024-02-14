# ======================================================================
import requests, json

class Course:
    def __init__(self, Semester="1122"):
        self.__Semester = Semester
        self.__URL = "https://querycourse.ntust.edu.tw/querycourse/api/courses"
        self.__USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        self.__HEADERS = {"user-agent": self.__USERAGENT, "content-type": "application/json; charset=utf-8"}
        self.__PAYLOAD = {
            'GE': {"Semester":"","CourseNo":"","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":1,"OnleyNTUST":0,"OnlyMaster":0,"Language":"zh"},
            'LANG': {"Semester":"","CourseNo":"","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":1,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyMaster":0,"Language":"zh"},
            'PE': {"Semester":"","CourseNo":"PE","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyMaster":0,"Language":"zh"},
            'MAJOR': {"Semester":"","CourseNo":"","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyUnderGraduate":0,"OnlyMaster":0,"Language":"zh"}
        }

    # ========================================
    def __get_RemoteData(self, Type, KeyWord):
        payload = self.__PAYLOAD[Type]
        payload["Semester"] = self.__Semester
        payload["CourseName"] = KeyWord
        request = json.dumps(payload).encode("utf-8")
        try:
            response = requests.post(self.__URL, headers=self.__HEADERS, data=request)
            courses = json.loads(response.text)
            return courses
        except Exception:
            return None

    # ========================================
    def get_General_Data(self, KeyWord=''):
        return self.__get_RemoteData('GE', KeyWord)

    def get_ForeignLang_Data(self, KeyWord=''):
        return self.__get_RemoteData('LANG', KeyWord)

    def get_PE_Data(self, KeyWord=''):
        return self.__get_RemoteData('PE', KeyWord)

    def get_Major_Data(self, KeyWord='', Major='ET', OnlyMaster=1):
        self.__PAYLOAD['MAJOR']["CourseNo"] = Major
        self.__PAYLOAD['MAJOR']["OnlyMaster"] = OnlyMaster
        return self.__get_RemoteData('MAJOR', KeyWord)

# ======================================================================