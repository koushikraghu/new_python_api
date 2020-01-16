from model import mycol

class Common:
    def find_record(self,name):
        '''check if record exists in the database'''
        if mycol.count_documents({"id":name}) > 0 :
            return 1
        else:
            return 0
    #show all records
    def show_records(self):
        '''method to show all records'''
        List = []
        for i in mycol.find():
            List.append(i)
        return List

