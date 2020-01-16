from model import mycol
from . import common_functions

c = common_functions.Common()

class Updation_controller(object):

    def update(self,name,new_address):
        '''updating the database'''
        if c.find_record(name):
            myquery = {"id":name}
            new_values = { "$set" : { "addr" :new_address } }
            mycol.update_one(myquery,new_values)
            return c.show_records()
        else:
            return "No record found fro updation"

