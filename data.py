global k, num_of_points, spectral_function, fermi_distribution, frequencies
k = 1.

def get_k():
    return k

def set_number_of_points(value):
   global num_of_points
   num_of_points = value

def get_num_of_points():
    return num_of_points

def save_spectral_function(array):
    global spectral_function
    spectral_function = array

def get_spectral_function():
    return spectral_function

def save_fermi_distribution(array):
    global fermi_distribution
    fermi_distribution = array

def get_fermi_distribution():
    return fermi_distribution

def set_frequencies(array):
    global frequencies
    frequencies = array

def get_frequencies():
    return frequencies