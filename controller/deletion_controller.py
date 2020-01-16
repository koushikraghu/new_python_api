from model import mycol
from . import common_functions

c = common_functions.Common()

class Deletion_function(object):
    def delete(self,name,addr):
        '''delete a record'''
        if c.find_record(name):
            my_query = {"id":name}
            mycol.delete_one(my_query)
            return c.show_records()
        else:
            return "No record to delete"
