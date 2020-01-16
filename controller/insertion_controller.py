from model import mycol
from . import common_functions

c = common_functions.Common()

class Insertion_Controller(object):

    def insert(self,name,addr):
        if not c.find_record(name):
            mydict = {"name":name,"address":addr}
            mycol.insert_one(mydict)
            return c.show_records()
        else:
            return "Name Exists, please insert another name"


