# calculates band gap, phonon frequency and dielectric constant
import numpy as np
import math
import matplotlib.pyplot as plt
# Plotting of ElectronBandGap
class ElectronBandGap:
    def __init__(self,material): #takes the type of nanosemiconductor
        self.material=material
        self.range_of_D = np.linspace(2,26).reshape(50,1) #creates a numpy array of D.
        self.zeta = {'Spherical':np.array([[1]]),'Regular Tetrahedral':np.array([[1.49]]),'Regualar Hexahedral':np.array([[1.24]]),'Regular Octahedral':np.array([[1.18]])}
        self.beta = np.array([[0.75]])
        if material == 'TiO2':
            self.Eg_bulk = np.array([[3.05]])
            self.d = np.array([[0.458]])
        elif material == 'Si':
            self.Eg_bulk = np.array([[1.1]])
            self.d = np.array([[0.192]])
        elif material == 'CdS':
            self.Eg_bulk = np.array([[2.5]])
            self.d = np.array([[0.25]])
        elif material == 'CdSe':
            self.Eg_bulk = np.array([[1.74]])
            self.d = np.array([[0.219]])
        else:
            self.Eg_bulk = np.array([[3.5]])
            self.d = np.array([[0.201]])
    def calculateBandGap(self):        #returns plot of bandgap vs D
        #Step-1: Calculaton of Eg for each zeta and range_of D in total
        plt.figure(figsize=(10,10))
        for i in self.zeta:
            Eg = self.Eg_bulk * (1 + (4*self.beta*self.zeta[i]*self.d)/(self.range_of_D))
            plt.plot(self.range_of_D,Eg,label=i)
            plt.legend()
        plt.xlabel('D(nm)')
        plt.ylabel('Eg(eV)')
        plt.title(f'Band Gap of {self.material} in different shapes')
        plt.savefig(f'Eg vs D for {self.material}')
    pass
class PhononFrequency:
    def __init__(self,material):
      self.material=material
      self.range_of_D = np.linspace(2,26).reshape(50,1) #forms D values which are 
      self.zeta = {'Spherical':np.array([[1]]),'Regular Tetrahedral':np.array([[1.49]]),'Regualar Hexahedral':np.array([[1.24]]),'Regular Octahedral':np.array([[1.18]])}
      self.beta = np.array([[0.75]])
      if material == 'TiO2':
          self.omega_bulk = np.array([[np.NaN]])
          self.d = np.array([[0.458]])
      elif material == 'Si':
          self.omega_bulk = np.array([[520]])
          self.d = np.array([[0.192]])
      elif material == 'CdS':
          self.omega_bulk = np.array([[np.NaN]])
          self.d = np.array([[0.25]])
      elif material == 'CdSe':
          self.omega_bulk = np.array([[210]])
          self.d = np.array([[0.219]])
      else:
          self.omega_bulk = np.array([[np.NaN]])
          self.d = np.array([[0.201]])
    def cacluatePhononFrequency(self):
      plt.figure(figsize=(10,10))
      print('Ok')
      for i in self.zeta:
          omega = self.omega_bulk *((1 - (4*self.beta*self.zeta[i]*self.d)/(self.range_of_D))**0.5)
          plt.plot(self.range_of_D,omega/self.omega_bulk,label=i)
          plt.legend()
      plt.xlabel('D(nm)')
      plt.ylabel('\u03C9(D)/\u03c9(bulk)')
      plt.title(f'Phonon Frequency of {self.material} in different shapes')
      plt.savefig(f'\u03C9 vs D for {self.material}')
    pass

class DielectricConstant:
  def __init__(self,material):
      self.material=material
      self.range_of_D = np.linspace(2,26).reshape(50,1) #forms D values which are 
      self.zeta = {'Spherical':np.array([[1]]),'Regular Tetrahedral':np.array([[1.49]]),'Regualar Hexahedral':np.array([[1.24]]),'Regular Octahedral':np.array([[1.18]])}
      self.beta = np.array([[0.75]])
      if material == 'TiO2':
          self.epsilon_bulk = np.array([[NaN]])
          self.d = np.array([[0.458]])
      elif material == 'Si':
          self.epsilon_bulk = np.array([[11.4]])
          self.d = np.array([[0.192]])
      elif material == 'CdS':
          self.epsilon_bulk = np.array([[8.7]])
          self.d = np.array([[0.25]])
      elif material == 'CdSe':
          self.epsilon_bulk = np.array([[6.2]])
          self.d = np.array([[0.219]])
      else:
          self.epsilon_bulk = np.array([[8.63]])
          self.d = np.array([[0.201]])

  def cacluateDielectricConstant(self):
      plt.figure(figsize=(10,10))
      #print('OK')
      for i in self.zeta:
          epsilon = 1+ (self.epsilon_bulk-1) *((1 +(4*self.beta*self.zeta[i]*self.d)/(self.range_of_D))**(-2))
          plt.plot(self.range_of_D,epsilon,label=i)
          plt.legend()
      plt.xlabel('D(nm)')
      plt.ylabel('\u03B5(D)')
      plt.title(f'Dielectric Constant of {self.material} in different shapes')
      plt.savefig(f'\u03B5 vs D for {self.material}')
  pass

if __name__ == '__main__':
    nanomaterials_for_Eg = ['TiO2','Si','GaN','CdS','CdSe']
    for i in nanomaterials_for_Eg:
        Eg = ElectronBandGap(i)
        Eg.calculateBandGap()
    nanomaterials_for_frequency = ['Si','CdSe']
    for i in nanomaterials_for_frequency:
        omega = PhononFrequency(i)
        omega.cacluatePhononFrequency()
    nanomaterials_for_dielectric_constant = ['CdS','CdSe','Si','GaN']
    for i in nanomaterials_for_dielectric_constant:
        epsilon = DielectricConstant(i)
        epsilon.cacluateDielectricConstant()

