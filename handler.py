from src.helper.utils import Utils
from src.controller.controller import Controller

if __name__=='__main__':
    """
        Starting point for program
        python version 3.7.9
        library used pandas==1.2.5
    """
    companys_no = Utils.get_input('total companys','int')
    companys = Utils.get_list_input(companys_no)
    students_no = Utils.get_input('total students','int')
    students = Utils.get_list_input(students_no)
    time = Utils.get_input('interview time','str')
    sortlist = Utils.get_input('sortlist per company','int')
    student_preference = Utils.get_preference_dict(students,companys,['students','companys'])
    company_preference = Utils.get_preference_dict(companys,students,['companys','students'])
    Controller(sortlist=sortlist,time=time,student_preference=student_preference,company_preference=company_preference).execute()
