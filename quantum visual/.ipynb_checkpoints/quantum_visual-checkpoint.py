# VIRTUAL ENVIRONMENT - 'quantum_visual':conda

import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import tkinter as tk
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings

warnings.filterwarnings('ignore')

# DEFINE WINDOW
root = tk.Tk()
root.title('Quantum Visual')

## window specifications
# setting the icon
root.iconbitmap(default='H:\quamtum computing\code practice\projects\quantum visual\glasses_logo.ico') # iconbitmap() will set our desired logo on the window and if lets say, you main window opens up another window via any button, then on that window also you will need the same logo, so thats why 'default' parameter is used
root.geometry('399x422')
root.resizable(0,0) # restricts main window from resizing, SPELLING OF RESIZABLE IS DIFFERENT FROM INTUITIVE SPELLING !!!

# color and fonts
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial',18)
disp_font = ('Arial',32)

# working of about function
def about():   # gives information about the project
    info = tk.Tk()
    info.title('About')
    info.geometry('850x330')
    info.resizable(0,0)
    
    label = tk.Label(info, text='About Quantum Visual app')
    label.config(font=('Arial',14))
    label.pack()
    
    text_to_disp = '''
    Quantum Visuals is an GUI app that is made to visualize following gate operations on a single qubit. 
    Qubit is initially in the state |0>.
    
    1. X-gate : bit-flip gate                                              : circuit.x()
    2. Y-gate : bit- and phase-flip gate                                   : circuit.y()
    3. Z-gate : phase-flip gate                                            : circuit.z()
    4. H-gate : sqaure-root of X-gate                                      : circuit.h()
    5. S-gate : rotation by pi/4 about plane perpendicular to Z-axis       : circuit.s()
    6. T-gate : rotation by pi/4 about plane perpendicular to Z-axis       : circuit.t()
    7. Rx-gate : rotation about plane perpendicular to X-axis              : circuit.rx(theta)
    8. Ry-gate : rotation about plane perpendicular to Y-axis              : circuit.ry(theta)
    9. Rz-gate : rotation about plane perpendicular to Z-axis              : circuit.rz(theta)
    10. S(dag)-gate : rotation by pi/4 about plane perpendicular to Z-axis : circuit.sdag()
    11. T(dag)-gate : rotation by pi/4 about plane perpendicular to Z-axis : circuit.tdag()
    
    NOTE: 1. theta will vary from [-2pi,2pi] with a gap of 0.25pi for Rx, Ry and Rz gates.
          2. Atmost 10 operations are allowed at once on a qubit.

    '''
    text = tk.Text(info, height=20, width=20)
    text.insert(END, text_to_disp)
    text.pack(fill='both', expand=True)
    
    info.mainloop()

# initialize the circuit
def initialize():
    global circuit     # making variable 'circuit' a global variable
    circuit = QuantumCircuit(1)     # we need 1 qubit only

initialize()
theta = 0

# function for clear button
def clear():        # it should have a parameter 'circuit', but as we have made circuit as global variable, so we can use circuit without passing it as a parameter.
    '''
    1. Clears the display screen.
    2. Reinitializes the circuit to state |0>.
    3. If all the gate buttons are disabled, then, enables them.
    '''
    disp.delete(0,END)
    
    initialize()
    
    if x_gate['state']==DISABLED:   # checking if any gate is DISABLED or not, if yes, then all the gates would be DISABLED. 
        gates = [x_gate, y_gate, z_gate, rx_gate, ry_gate, rz_gate, s_gate, s_dg, t_gate, t_dg, hdmd]
        for gate in gates:
            gate.config(state = NORMAL)        

# displays the gate operation on the screen
def display_gate(gate_input):
    disp.insert(END, gate_input)
    
    input = disp.get()
    num_gates = len(input)
    list_input = list(input)
    search_double_char = ['R','d']
    count_double_char = [list_input.count(i) for i in search_double_char]
    num_gates -= sum(count_double_char)
    
    if num_gates == 10:  # in qiskit, we can perform nly 10 gates on a qubit at a time
        gates = [x_gate, y_gate, z_gate, rx_gate, ry_gate, rz_gate, s_gate, s_dg, t_gate, t_dg, hdmd]
        for gate in gates:
            gate.config(state=DISABLED)

# function to change theta value and apply Rx, Ry, Rz gate
def change_theta(coeff, window, key):
    global theta
    theta = coeff * np.pi      # coeff is the coefficient of 'pi'
    if key == 'x':
        circuit.rx(theta,0)
        theta = 0 # reinitialize the value of theta to 0, so that if we again choose any parameterized gate, we get no error.and
    elif key == 'y':
        circuit.ry(theta,0)
        theta = 0
    else:
        circuit.ry(theta,0)
        theta = 0
    window.destroy()

# Function for taking user input for Parameterized gates (Rx, Ry, Rz)
def user_input(key):
    get_input = tk.Tk()
    
    get_input.title('Get value for theta')
    get_input.geometry('360x160')
    get_input.resizable(0,0)

    val1 = tk.Button(get_input, height=2, width=10, text='pi/4', bg=buttons, font=('Arial',10), command=lambda:change_theta(0.25, get_input, key))
    val1.grid(row=0, column=0)

    val2 = tk.Button(get_input, height=2, width=10, text='pi/2', bg=buttons, font=('Arial',10), command=lambda:change_theta(0.5, get_input, key))
    val2.grid(row=0, column=1)

    val3 = tk.Button(get_input, height=2, width=10, text='pi', bg=buttons, font=('Arial',10), command=lambda:change_theta(1, get_input, key))
    val3.grid(row=0, column=2)
    
    val4 = tk.Button(get_input, height=2, width=10, text='2pi', bg=buttons, font=('Arial',10), command=lambda:change_theta(2, get_input, key))
    val4.grid(row=0, column=3, sticky='W')
    
    nval1 = tk.Button(get_input, height=2, width=10, text='-pi/4', bg=buttons, font=('Arial',10), command=lambda:change_theta(-0.25, get_input, key))
    nval1.grid(row=1, column=0)

    nval2 = tk.Button(get_input, height=2, width=10, text='-pi/2', bg=buttons, font=('Arial',10), command=lambda:change_theta(-0.5, get_input, key))
    nval2.grid(row=1, column=1)
    
    nval3 = tk.Button(get_input, height=2, width=10, text='-pi', bg=buttons, font=('Arial',10), command=lambda:change_theta(-1, get_input, key))
    nval3.grid(row=1, column=2)    
    
    nval4 = tk.Button(get_input, height=2, width=10, text='-2pi', bg=buttons, font=('Arial',10), command=lambda:change_theta(-2, get_input, key))
    nval4.grid(row=1, column=3, sticky='W')
    
    note = '''
    NOTE: Provide the value for theta !
    The value of theta is from [-2pi, 2pi]
    '''
    text_box = tk.Text(get_input, height=20, width=20, bg='grey')
    text_box.grid(sticky='WE', columnspan=4)
    text_box.insert(END, note)
    
    get_input.mainloop()

# visualize the circuit
def visual_circuit(window):
    '''
    1. To visualize our quantum circuit.
    2. If we use just the visualize_transition directly, then it will give error when the display screen is empty, it will give error saying 'Nothing to visualize'.
    3. So, to handle above problem, we use this explicitly defined function.
    '''
    try:
        visualize_transition(circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        print('Nothing to Visualize, apply some gate operation to visualize.')
        window.destroy()

## Frames in main window
# setting up frames for the main window
disp_frame = tk.LabelFrame(root)
button_frame = tk.LabelFrame(root, bg='black')
disp_frame.pack()
button_frame.pack(fill='both', expand=True)

# display frame layout
disp = tk.Entry(disp_frame, width=120, bg=background, font=disp_font, borderwidth=10, justify=LEFT)
disp.pack(padx=3, pady=4)

# button layout
x_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='X', command=lambda:[display_gate('X'), circuit.x(0)])
y_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='Y', command=lambda:[display_gate('Y'), circuit.y(0)])
z_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='Z', command=lambda:[display_gate('Z'), circuit.z(0)])
x_gate.grid(row=0, column=0, ipadx=47, pady=1)
y_gate.grid(row=0, column=1, ipadx=48, pady=1)
z_gate.grid(row=0, column=2, ipadx=48, pady=1)

rx_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='Rx', command=lambda:[display_gate('Rx'), user_input('x')])
ry_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='Ry', command=lambda:[display_gate('Ry'), user_input('y')])
rz_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='Rz', command=lambda:[display_gate('Rz'), user_input('z')])
rx_gate.grid(row=1, column=0, columnspan=1, pady=1, sticky='WE')
ry_gate.grid(row=1, column=1, columnspan=1, pady=1, sticky='WE')
rz_gate.grid(row=1, column=2, columnspan=1, pady=1, sticky='WE')

s_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='S', command=lambda:[display_gate('S'), circuit.s(0)])
s_dg = tk.Button(button_frame, font=button_font, bg=buttons, text='S(dag)', command=lambda:[display_gate('Sd'), circuit.sdg(0)])
hdmd = tk.Button(button_frame, font=button_font, bg=buttons, text='H', command=lambda:[display_gate('H'), circuit.h(0)])
s_gate.grid(row=2, column=0, columnspan=1, pady=1, sticky='WE')
s_dg.grid(row=2, column=1, columnspan=1, pady=1, sticky='WE')
hdmd.grid(row=2, column=2, rowspan=2, sticky='WENS')

t_gate = tk.Button(button_frame, font=button_font, bg=buttons, text='T', command=lambda:[display_gate('T'), circuit.t(0)])
t_dg = tk.Button(button_frame, font=button_font, bg=buttons, text='T(dag)', command=lambda:[display_gate('Td'), circuit.tdg(0)])
t_gate.grid(row=3, column=0, sticky='WE')
t_dg.grid(row=3, column=1, sticky='WE')

quit = tk.Button(button_frame, font=button_font, bg=special_buttons, text='Quit', command=root.destroy)
visual = tk.Button(button_frame, font=button_font, bg=special_buttons, text='Visualize', command=lambda:visual_circuit(root))
quit.grid(row=4, column=0, columnspan=2, ipadx=5, sticky='WE')
visual.grid(row=4, column=2, ipadx=5, sticky='WE')

clear = tk.Button(button_frame, font=button_font, bg=special_buttons, text='Clear', command=clear)
clear.grid(row=5, column=0, columnspan=3, sticky='WE')

about = tk.Button(button_frame, font=button_font, bg=special_buttons, text='About', command=about)
about.grid(row=6, column=0, columnspan=3, sticky='WE')



root.mainloop()