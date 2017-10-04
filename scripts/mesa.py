import numpy as np

G = 6.67428e-8 # dyne cm^2 / g^2
clight = 2.9979246e+10 # cm / s
arad = 7.5657e-15 # erg cm^-3 K^-4
msol = 1.9891e+33 # g
rsol = 6.9598e10 # cm
kb = 1.3806503e-16 # g cm^2 / K s^2
Na = 6.022142e+23 # 1 / mol
Rgas = 83144621.0 # erg / mol K
solarlum = 3.846e33 # erg / s
umass = 1.660538921e-24 # g

class mesa_profile(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            f.readline() # skip column numbers
            labels = f.readline().split()
            values = f.readline().split()
            # first two are integers
            for l, v in zip(labels[:2], values[:2]):
                self.__dict__[l] = int(v)
            for l, v in zip(labels[2:], values[2:]):
                self.__dict__[l] = float(v)

            f.readline()
            f.readline()

            self.columns = f.readline().split()
            values = np.loadtxt(f)
            for i, l in enumerate(self.columns):
                # order of values is inverted to start at the core
                self.__dict__[l] = values[::-1,i]
