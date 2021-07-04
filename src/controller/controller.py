import pandas as pd
from copy import deepcopy
from src.constants import (
    BOTH_MATCH_POINT,ONE_MATCH_POINT,NO_MATCH_POINT
    )
class Controller:
    def __init__(self,**kwargs) -> None:
        """
        Unpacking the data
        """
        self.student_preference= kwargs['student_preference']
        self.company_preference= kwargs['company_preference']
        self.time=kwargs['time']
        self.sortlist=kwargs['sortlist']
    
    def execute(self):
        """
            Computations Logic - used decision matrix
            company and student preference got equal weitage
            when so based on weitage we can give score and decide priority list

            2 extra input parameter used that didnt mention in input taking part
            to take the priority list from company and students. have used the 
            exception handling so it will hold in some extra scenario as well

            Written by : Junedrajbhara for interview process in unifynd
        """
        studf = pd.DataFrame(self.student_preference)
        comdf = pd.DataFrame(self.company_preference)
        comdf = comdf[['students','companys']]
        studf.sort_values(['students'], ascending=[True])
        comdf.sort_values(['students'], ascending=[True])
        temp = []
        tempvalues = deepcopy(comdf.values.tolist())
        for stu in studf.values:
            flag = True
            for ind,com in enumerate(tempvalues):
                if stu[0] == com[0] and stu[1] == com[1] and flag:
                    temp.append(BOTH_MATCH_POINT)
                    tempvalues.pop(ind)
                    flag = False
                elif stu[0] == com[0] or stu[1] == com[1] and flag:
                    temp.append(ONE_MATCH_POINT)
                    flag = False
                    tempvalues.pop(ind)
                elif stu[0] != com[0] and stu[1] != com[1] and flag:
                    temp.append(NO_MATCH_POINT)
                    flag = False
                    tempvalues.pop(ind)
            if flag: temp.append(ONE_MATCH_POINT)
        studf['score'] = temp
        comdf['score'] = temp[:len(comdf)]
        if len(comdf[comdf['score'] <=ONE_MATCH_POINT]) > 0:
            studf[studf['score'] <=ONE_MATCH_POINT] = comdf[comdf['score'] <=50]
        print('\n Priority List \n')
        print(studf)