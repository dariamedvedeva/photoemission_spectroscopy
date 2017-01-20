import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import math
import data

##############
#save picture
##############
def save(name = '', fmt = 'png'):
    pwd = os.getcwd()
    plt.savefig('%s.%s' % (name, fmt), fmt = 'png')
    os.chdir(pwd)

def draw(x, y):
    #plt.figure()
    plt.title('Photoemission spectroscopy', color = 'k', size = 25)
    plt.xlabel('ENERGY, eV', size = 15)
    plt.ylabel('INTENSITY (arbitrary units)', size = 15)
    plt.grid(True)
    plt.plot(x, y, linewidth = 2, color = 'red', label = 'EDMFT')
    plt.xlim(0, 3)
    plt.legend()
    plt.show()

def fermi_distribution_function(frequencies, mu, T):
    print "Fermi distribution function was constructed"
    num_of_points = data.get_num_of_points()
    fermi_distribution = np.zeros(num_of_points, np.float)
    for j in range(num_of_points):
        fermi_distribution[j] = 1. / (math.exp((frequencies[j] - mu) / data.get_k() * T) + 1.)
    #draw(frequencies, fermi_distribution)
    data.save_fermi_distribution(fermi_distribution)

def read_spectral_function():
    f = open("data/green_imp_r.dat")
    lines = f.readlines()
    # read all lines and get the number of them
    length = lines.__len__()
    spectral_function = np.zeros(length, np.float)
    frequencies = np.zeros(length, np.float)
    print "The number of points in spectral function from file", length
    data.set_number_of_points(length)
    j = 0
    for i in lines:
        line = i.split()
        frequencies[j] = np.float(line[0])
        spectral_function[j] = np.float(line[2])
        j += 1
    #draw(frequencies, spectral_function)
    data.save_spectral_function(spectral_function)
    data.set_frequencies(frequencies)

def photoemission_spectra():
    spectra = data.get_fermi_distribution() * data.get_spectral_function()
    #draw(data.get_frequencies(), spectra)
    DOS = -1./math.pi * spectra
    draw(data.get_frequencies(), DOS)