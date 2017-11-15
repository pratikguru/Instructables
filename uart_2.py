import serial
import threading
import time
import Tkinter
from Tkinter import*
import ttk

from numpy import random, array, dot, exp

current_location = 0
entries = []
state_change = 0
gui = Tk()
gui.title("MyNet")

"""
training_set_inputs  = array([[0,1,1], [0,0,1], [1,0,1],[0,1,1]])
training_set_outputs = array([[1,0,1,1]]).T

print (net.think(array([0,1,1])))
"""

class Neural_net():
	def __init__(self):

		random.seed(1)
		self.synaptic_weights = 2 * random.random((3,1)) - 1

	def sigmoid(self, x):
		return 1 / (1 + exp( -x))

	def sigmoid_derivative(self, x):
		return x * (1 - x)


	def train(self, training_data_input, training_data_output
		, number_of_iteraitons):

		for iterations in xrange(number_of_iteraitons):
			output, lol = self.think(training_data_input)
			error = training_data_output - output

			adjustments = dot(training_data_input.T, error * self.sigmoid_derivative(output))
			self.synaptic_weights += adjustments

	def think(self, inputs):
		return (self.sigmoid(dot(inputs, self.synaptic_weights))), 1


def get_data_set():
	global state_change

	

	data_1 = []
	data_2 = []
	data_3 = []
	data_4 = []
	data_5 = []
	data_6 = []

	row_1 = row_1_.get()
	row_2 = row_2_.get()
	row_3 = row_3_.get()
	row_4 = row_4_.get()

	input_row_1 = input_row_.get()

	row_5 = outcome_entry.get()

	for x in row_1:
		data_1.append(int(x))
	for y in row_2:
		data_2.append(int(y))
	for z in row_3:
		data_3.append(int(z))	
	for u in row_4:
		data_6.append(int(u))
	for o in input_row_1:
		data_4.append(int(o))
	for i in row_5:
		data_5.append(int(i))
	
	outcome = array([data_5]).T
	input_ = array([data_1, data_2, data_3, data_6])
	
	#outcome = array([data_4]).T
	print input_

	net.train(input_, outcome, (iteration_bar.get()))
	state_change = net.think(data_4)[1]
	
		
	
	final_output  = Label(text = (net.think(data_4)),font = "Helvetica 10 bold", bd = 4)
	final_output.place(x = 340, y = 73)


def add_row():
	global current_location
	global entries

	for x in range(0,1):
		inputs_x = (Entry(width = 20).grid(row = 20 + (current_location), column = 2 ))
		entries.append(inputs_x)
		current_location = current_location + 20


def delete_cell():
	global entries
	list = gui.grid_slaves()
	
	for x in list:	
		x.destroy()
		return
	
	

		
if __name__ == "__main__":

	net = Neural_net()
	

	#frames
	frame_1 = Frame(height = 350, width = 480, bd =3, relief = 'groove').place( x = 10, y = 10)

	#labels
	training_set = Label(text = "Training Data Set").place(x = 50, y = 12)
	
	input_set    = Label(text = "Input Data Set").place(x = 50, y = 150)

	row_1_l = Label(text = "Row1: ").place(x = 20, y = 30)
	row_2_l = Label(text = "Row2: ").place(x = 20, y = 60)
	row_3_l = Label(text = "Row3: ").place(x = 20, y = 90)
	row_4_l = Label(text = "Row4: ").place(x = 20, y = 120)


	Input = Label(text = "Input").place(x = 20, y = 180)
	iteration_label = Label(text = "Iterations: ").place(x = 20, y = 200)
	output_label = Label(text  = "Outcome:").place(x = 250, y = 12)
	
	final_output_label = Label(text = "Final Outcome:").place(x = 250, y = 75)
	



	#entry
	row_1_ = Entry(width = 20)
	row_1_.place(x = 60, y = 30)

	row_2_ = Entry(width = 20)
	row_2_.place(x = 60, y = 60)

	row_3_ = Entry(width = 20)
	row_3_.place(x = 60, y = 90)

	row_4_ = Entry(width = 20)
	row_4_.place(x = 60, y = 120)

	input_row_ = Entry(width = 10)
	input_row_.place(x = 60, y = 176)

	outcome_entry = Entry(width = 20)
	outcome_entry.place(x = 250, y = 30)

	# training_set_inputs  = array([[0,1,1], [0,0,1], [1,0,1],[0,1,1]])
	# training_set_outputs = array([[1,0,1,1]]).T

	row_1_.insert(0,((110)))
	row_2_.insert(0,((100)))
	row_3_.insert(0,((101)))
	row_4_.insert(0,((111)))
	
	outcome_entry.insert(1, ((1001)))

	#scales
	iteration_bar = Scale(orient = "horizontal", from_= 1000, to = 1000000, length = 300)
	iteration_bar.place(x = 20, y = 220)

	#buttons
	button = Button(text = "Train", command = get_data_set, width = 30).place(x = 20, y = 300)
	
	#add = Button(text = "add", command = add_row).place(x = 100, y = 180)
	#delete = Button(text = "delete", command = delete_cell).place(x = 100, y = 230)
	gui.geometry('500x370')
	gui.mainloop()