import csv  #Inputs data
import matplotlib   #makes graphs

#make graphs work with dashboard
matplotlib.use("TkAgg")
#import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk    #makes dashboard/buttons/interactivity
from tkinter import ttk

class GradeMeApp(tk.Tk): #Controller class, right out of tutorial
  def __init__(self,*args,**kwargs):
      tk.Tk.__init__(self,*args,**kwargs) #initializes the application
      #tk.Tk.iconbitmap(self,default="clienticon.ico")
      tk.Tk.wm_title(self, "Grade Me client") #names the window
      container =  tk.Frame(self)
      container.pack(side="top", fill="both", expand=True)
      container.grid_rowconfigure(0, weight=1)
      container.grid_columnconfigure(0, weight=1)
      self.frames={}
      for page in (HomePage, Page1, Page2, Page3, Page4, Page5, Page6, Page7):
          frame = page(container, self)
          self.frames[page] = frame
          frame.grid(row=0, column=0, sticky="nsew")
      self.show_frame(HomePage)

  def show_frame(self, cont):
      frame = self.frames[cont]
      frame.tkraise()

class HomePage(tk.Frame):
  def __init__(self, parent, controller):
      global student_name
      global weightnames
      ###
      #Creating kinda like the window
      tk.Frame.__init__(self,parent)
      label = tk.Label(self, text=student_name+"'s Home Page")
      label.pack(pady=10,padx=10)
      ###
      button = ttk.Button(self, text="See Overall Grade", command=lambda: controller.show_frame(Page1))
      button.pack()
      button2 = ttk.Button(self, text="See "+weightnames[0], command=lambda: controller.show_frame(Page2))
      button2.pack()
      button3 = ttk.Button(self, text="See "+weightnames[1], command=lambda: controller.show_frame(Page3))
      button3.pack()
      button4 = ttk.Button(self, text="See "+weightnames[2], command=lambda: controller.show_frame(Page4))
      button4.pack()
      button5 = ttk.Button(self, text="See "+weightnames[3], command=lambda: controller.show_frame(Page5))
      button5.pack()
      button6 = ttk.Button(self, text="See "+weightnames[4], command=lambda: controller.show_frame(Page6))
      button6.pack()
      button7 = ttk.Button(self, text="See "+weightnames[5], command=lambda: controller.show_frame(Page7))
      button7.pack()

class Page1(tk.Frame):
  def __init__(self, parent, controller):
      ##
      tk.Frame.__init__(self, parent)
      label = tk.Label(self, text="Overall Grade")
      label.pack(pady=10,padx=10)
      ##
      button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
      button1.pack()
      button2 = ttk.Button(self, text="Next Section", command=lambda: controller.show_frame(Page2))
      button2.pack()
      #CREATING THE ACTUAL PIE CHART
      f = pie_chart()
      canvas = FigureCanvasTkAgg(f, self)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #toolbar = NavigationToolbar2TkAgg(canvas, self)
      #toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Page2(tk.Frame):
  def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      global weightnames
      label = tk.Label(self, text=weightnames[0])
      label.pack(pady=10,padx=10)
      button1 = ttk.Button(self, text="Previous Section", command=lambda: controller.show_frame(Page1))
      button1.pack()
      button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
      button2.pack()
      button3 = ttk.Button(self, text="Next Section", command=lambda: controller.show_frame(Page3))
      button3.pack()
      f = whisker_plot()
      canvas = FigureCanvasTkAgg(f, self)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
      #toolbar = NavigationToolbar2TkAgg(canvas, self)
      #toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)
      h = pie_chart()
      can = FigureCanvasTkAgg(h, self)
      can.draw()
      can.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
      # toolbar = NavigationToolbar2TkAgg(canvas, self)
      # toolbar.update()
      can._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)

class Page3(tk.Frame):
  def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      global weightnames
      label = tk.Label(self, text=weightnames[1])
      label.pack(pady=10,padx=10)
      button1 = ttk.Button(self, text="Previous Section", command=lambda: controller.show_frame(Page2))
      button1.pack()
      button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
      button2.pack()
      button3 = ttk.Button(self, text="Next Section", command=lambda: controller.show_frame(Page4))
      button3.pack()
      f = histogram(grade2)
      canvas = FigureCanvasTkAgg(f, self)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #toolbar = NavigationToolbar2TkAgg(canvas, self)
      #toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Page4(tk.Frame):
  def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      global weightnames
      label = tk.Label(self, text=weightnames[2])
      label.pack(pady=10,padx=10)
      button1 = ttk.Button(self, text="Previous Section", command=lambda: controller.show_frame(Page3))
      button1.pack()
      button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
      button2.pack()
      button3 = ttk.Button(self, text="Next Section", command=lambda: controller.show_frame(Page5))
      button3.pack
      
      f = histogram(grade3)
      canvas = FigureCanvasTkAgg(f, self)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #toolbar = NavigationToolbar2TkAgg(canvas, self)
      #toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Page5(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       global weightnames
       label = tk.Label(self, text=weightnames[3])
       label.pack(pady=10, padx=10)
       button1 = ttk.Button(self, text="Previous Section", command=lambda: controller.show_frame(Page4))
       button1.pack()
       button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
       button2.pack()
       button3 = ttk.Button(self, text="Next Section", command=lambda: controller.show_frame(Page6))
       button3.pack()
      
      f = histogram(grade4)
       canvas = FigureCanvasTkAgg(f, self)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
       #toolbar = NavigationToolbar2TkAgg(canvas, self)
       #toolbar.update()
       canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Page6(tk.Frame):
  def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      global weightnames
      label = tk.Label(self, text=weightnames[4])
      label.pack(pady=10,padx=10)
      button1 = ttk.Button(self, text="Previous Section", command=lambda: controller.show_frame(Page5))
      button1.pack()
      button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
      button2.pack()
      button3 = ttk.Button(self, text="Next Section", command=lambda: controller.show_frame(Page7))
      button3.pack()
      
      f = histogram(grade5)
      canvas = FigureCanvasTkAgg(f, self)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #toolbar = NavigationToolbar2TkAgg(canvas, self)
      #toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
      
class Page7(tk.Frame):
  def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      global weightnames
      label = tk.Label(self, text=weightnames[5])
      label.pack(pady=10,padx=10)
      button1 = ttk.Button(self, text="Previous Section", command=lambda: controller.show_frame(Page6))
      button1.pack()
      button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
      button2.pack()
      
      f = histogram(grade6)
      canvas = FigureCanvasTkAgg(f, self)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      #toolbar = NavigationToolbar2TkAgg(canvas, self)
      #toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


#calculates final grade given a list of grades for one student
def calculate_final_grade(grades,weights):
  final_grade = 0
  sum = 0
  index = 0
  for element in grades:
      final_grade = final_grade+(int(element)*int(weights[index]))
      sum = sum + int(weights[index])
      index = index + 1
  final_grade = final_grade/sum
  return final_grade

#Calculates final grades for ALL students
def get_all_final_grades(matrix):
  final_grades = []
  for j in range(len(matrix[6])):
      column = []
      for i in range(7, len(weights) + 7):
          column.append(matrix[i][j])
      final_grades.append(calculate_final_grade(column,matrix[5]))
  return final_grades #returns a list with all final grades

def count_letter_grades(grades):
  count = [0,0,0,0,0]
  #count = [A,B,C,D,F]
  for x in grades:
      if x >= 90:
          count[0]=count[0] + 1
      if x < 90 and x>=80:
          count[1] = count[1] + 1
      if x < 80 and x>=70:
          count[2] = count[2] + 1
      if x < 70 and x>=60:
          count[3] = count[3] + 1
      if x < 60:
          count[4] = count[4] + 1
  return count

def pie_chart():    #Function that creates a pie chart
  global letter_count
  test = ['A', 'B', 'C', 'D', 'F']
  labels = list(test)
  colors = ['gold', 'yellowgreen', 'pink', 'lightskyblue', 'red']
  f = Figure(figsize=(5,5), dpi=100)
  graph = f.add_subplot(111)
  graph.pie(letter_count, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
  graph.axis('equal')
  #graph.show()
  return f

def whisker_plot():
  #fig = plt.figure(1, figsize=(9, 6))
  global grades
  f = Figure(figsize=(5,5), dpi=100)
  graph = f.add_subplot(111)
  graph.boxplot(grades)
  return f

def histogram(n):
  number_bins = 10
  f = Figure(figsize=(5,5), dpi=100)
  graph = f.add_subplot(111)
  graph.hist(n,number_bins,facecolor='yellow',alpha=0.5)
  return f

############################################
#######Code starts here#####################
############################################

matrix = [] #This is a list of lists
#INPUT
filename1 = input("Enter a file to read data from: ")
with open(filename1) as txtfile:   #opens file
   csv_file = csv.reader(txtfile)
   #Moving data into a matrix
   for row in csv_file:
       matrix.append(row)  #adding rows to matrix


#moving data from matrix to variables
course_code = matrix[0][0] #first row, first column
semester = matrix[1][0]
ID = matrix[2][0]
student_name = matrix[3][0]

#
weightnames = []    #a list for the percentage that each grade is
for names in matrix[4]:    #any number of weights is allowed
  if names=='':
      break
  weightnames.append(names)

#print(weightnames)
#

#store percentages into weights
weights = []    #a list for the percentage that each grade is
for percentage in matrix[5]:    #any number of weights is allowed
  if percentage=='':
      break
  weights.append(percentage)

#find the index for the logged in student
j = 0
for student in matrix[6]:
  if(student_name == student):
      break
  else:
      j = j + 1

#obtain grades for logged in student
student_grades = [] #ONLY GRADES for the logged in student
for i in range(7,len(weights)+7):
  student_grades.append(int(matrix[i][j]))
  
grade1 = []
for i in range(len(matrix[6])):
  grade1.append(matrix[7][i])

grade2 = []

for i in range(len(matrix[6])):
  grade2.append(matrix[8][i])

grade3 = []

for i in range(len(matrix[6])):
  grade3.append(matrix[9][i])

grade4 = []

for i in range(len(matrix[6])):
  grade4.append(matrix[10][i])
grade5 = []

for i in range(len(matrix[6])):
  grade5.append(matrix[11][i])

grade6 = []

for i in range(len(matrix[6])):
  grade6.append(matrix[12][i])

#finds final grade for logged in student
selected_grade = calculate_final_grade(student_grades,weights) #final grade for the selected student

#Find final grades for all students
grades = get_all_final_grades(matrix)

#counts the letter grades
#returns list of amount of each letter
letter_count = count_letter_grades(grades)

#pie_chart(letter_count,student_final)
#whisker_plot(final_grades,student_final)
#histogram(final_grades,student_final)
#whisker_plot()

#Creates Danshboard, and activates
app = GradeMeApp()  ##controller class
app.mainloop()  ##activating dashboard
