import unittest
from src.task import Task
from src.task_decider import *

class TestDecider(unittest.TestCase):
    def setUp(self):
        self.task1=Task("Wash the Dishes",60)
        self.task2=Task("Cook Dinner",40)
        self.task3=Task("Clean Windows",30)

        # self.preferred_option={
        # (self.task1,self.task2):self.task1.description,
        #  (self.task3,self.task2):self.task2.description,
        #   (self.task1,self.task3):self.task3.description
    

    def test_can_get_description(self):
         self.assertEqual("Wash the Dishes", self.task1.description)

    def test_can_get_description(self):
         self.assertEqual(60, self.task1.duration)

    def test_task_decider(self):
        result=get_preferred_option(self.task1,self.task2)
        self.assertEqual("Wash the Dishes", result)