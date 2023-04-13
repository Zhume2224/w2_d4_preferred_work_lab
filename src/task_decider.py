
#method1
# def get_preferred_option(task1,task2):
#     if task1.description=="Wash the Dishes" and task2.description=="Cook Dinner":
#         return task1.description

#method2
def get_preferred_option(task1,task2):
   
    preferred_option ={(task1.description,task2.description):task1.description}


    # return result=preferred_option[self.task1,self.task2]
    
    return preferred_option[(task1.description,task2.description)]


