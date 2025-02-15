# imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

class TaskList:
    """
    Class defining a task list object:
        Task List member fields = tasks [list of strings] : indicates tasks to be completed
                                  status [list of bool]   : indicates incomplete/completed task
    """
    def __init__(self):
        self.__tasks     = []
        self.__status    = []
        tasklist = {"Task":self.__tasks, "Task Status":self.__status}
        self._tasklist = pd.DataFrame(data=tasklist)
    def addTask(self, newTask:str):
        self.__tasks.append(newTask)
        self.__status.append(False)
        tasklist = {"Task":self.__tasks, "Task Status":self.__status}
        self._tasklist = pd.DataFrame(data=tasklist)
    def setStatus(self, index:int):
        if(self.__status[index] == False):
            self.__status[index] = True
        tasklist = {"Task":self.__tasks, "Task Status":self.__status}
        self._tasklist = pd.DataFrame(data=tasklist)
    def printList(self):
        print(self._tasklist)

def main():

    # test object (comment out later)
    todo = TaskList()
    f = open("toDo.out", "w")
    sys.stdout = f
    todo.printList()
    todo.addTask("Complete this Implementation")
    todo.printList()
    todo.setStatus(0)
    todo.printList()
    f.close()

main()

