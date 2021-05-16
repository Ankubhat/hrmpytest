import csv
class Utils:
    EnvVars={}

    @classmethod
    def InitialiseEnvVars(cls):
        with open('D:\\frameworkImplementation\\EnvVars.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                Utils.EnvVars[row[0]]=row[1]

    @classmethod
    def ReadLoginTestData(cls):
        LoginDataList=[]
        i=0
        with open('D:\\frameworkImplementation\\DataFiles\\LoginTestData.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                LoginData= {}
                LoginData["UserName"]=row[0]
                LoginData["Password"]=row[1]
                LoginData["Error"]=row[2]
                LoginDataList.append(LoginData)
                i=i+1

        return LoginDataList