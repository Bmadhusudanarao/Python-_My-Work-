from datetime import *
class Employee:
    def get(self,emp_list):
        self.EmployeeId=int(input('Enter the Employee Id:'))
        emp_list.append(self.EmployeeId)
        self.Ename=input('Enter Employee Name:')
        emp_list.append(self.Ename)
        self.Gender=input('Enter the Gender')
        emp_list.append(self.Gender)
        self.Salary=float(input('enter the salary'))
        emp_list.append(self.Salary)
        self.PerformanceRating=float(input('perforance Rating is out of 5:'))
        emp_list.append(self.PerformanceRating)
                        
class JoiningDetail:
    def getDoj(self):
        emp=[]
        no_emp=int(input('Enter the number of Employees:'))
        for i in range(no_emp):
            emp_list=[]
            Employee.get(self,emp_list)
            self.year,self.month,self.day=[int (x) for x in input('enter the Date of joining saprated by commas yyyy,mm,dd format').split(',')]
            DateOfJoining=date(self.year,self.month,self.day)
            emp_list.append(str(DateOfJoining))
            tp=tuple(emp_list)
            emp.append(tp)
        return emp
            
class Information(Employee, JoiningDetail):
    def __init__(self):
        self.emp=0
    def readData(self):
        self.emp=JoiningDetail.getDoj(self)
        print('THE EMPLOYEES DETAILS')
        print('______________________________________________________________________________________')
        print('Emp_Id\tEmp_Name\t\tGender\t Salary\t\tP_Rate\tDate of Joining')
        for record in self.emp:
            for field in record:
                print(field,'\t',end=' ')
            print()
        print('______________________________________________________________________________________')
    def sorted_list(self):
        sorted_emp=sorted(self.emp,key=lambda emp:emp[4], reverse=True)
        all_sorted=sorted_emp[:3]
        print('TOP THREE PERFORMENCE EMPLOYEES')
        print('______________________________________________________________________________________')
        print('Emp_Id\tEmp_Name\t\tGender\t Salary\t\tP_Rate\tDate of Joining')
        for record in all_sorted:
            for field in record:
                print(field,'\t',end=' ')
            print()
        print('______________________________________________________________________________________')
        sort_Joining=sorted(all_sorted,key=lambda all_sorted:all_sorted[5], reverse=True)
        print('SORT BY DATE OF JOINING DETAILS')
        print('______________________________________________________________________________________')
        print('Emp_Id\tEmp_Name\t\tGender\t Salary\t\tP_Rate\tDate of Joining')
        for record in sort_Joining:
            for field in record:
                print(field,'\t',end=' ')
       
#The Main programme           
        
if __name__ == '__main__':
    info = Information()
    info.readData()    # Collects data and displays all employees
    info.sorted_list() # Displays the top 3 performers
        
        
