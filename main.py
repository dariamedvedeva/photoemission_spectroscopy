import functions as func
import numpy as np
import data

mu = 1.
T = 1./100.

func.read_spectral_function()
func.fermi_distribution_function(data.get_frequencies(), mu, T)
func.photoemission_spectra()
