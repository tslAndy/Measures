import matplotlib.pyplot as plt
import numpy as np

mittaukset = np.loadtxt("mittaukset.txt")
plt.plot(mittaukset[:, 0], mittaukset[:, 2])
plt.show()

# tiedosto = open("mittaukset.txt", "r")
#
#
# aikalista = []
# painelista = []
# lampotilalista = []
# kosteuslista = []
#
# for rivi in tiedosto:
#     rivi = rivi.rstrip()
#
#     osat = rivi.split()
#     aikalista.append(int(osat[0]))
#     painelista.append(float(osat[1]))
#     lampotilalista.append(float(osat[2]))
#     kosteuslista.append(float(osat[3]))
#
# plt.plot(aikalista, painelista)
# plt.plot(aikalista, lampotilalista, "r")
# plt.plot(aikalista, kosteuslista, "m")
# plt.title("Mittaukset")
# plt.xlabel("Aika [s]")
# plt.ylabel("Paine [mbar]")
# plt.show()
