# -*- coding: utf-8 -*-
"""
Exemple d'animation d'une courbe 2D.
Etienne Hamelin ; 19/01/2018.
"""

# Import des librairies nécessaires
from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Préparation de l'animation de la corde
# (inspiration : https://matplotlib.org/examples/animation/simple_anim.html)

# Limites 
xmin, xmax = 0, 1
ymin, ymax = -1, 1
tmin, tmax = 0, 1

# Création d'une table de valeurs de x et det
N_x = 100
N_t = 100

x_tab = np.linspace(xmin, xmax, num=N_x, endpoint=True)
t_tab = np.linspace(tmin, tmax, num=N_t, endpoint=True)

dx = x_tab[1] - x_tab[0]
dt = t_tab[1] - t_tab[0]

print ("Pas de discrétisation en x: %f" % dx)
print ("Pas de discrétisation en temps: %f" % dt)

# Création du graphique
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on = False,
                     xlim=(xmin, xmax), ylim=(ymin, ymax))
plot, = ax.plot(x_tab, x_tab)
plot_titre = plt.title('t = 0')
plt.xlabel('x')
plt.ylabel('y')


# Un exemple de fonction à tracer
def f(x, t):
    """Exemple de fonction dépendant de x et du temps"""
    k = 1 # avec un paramètre manuel
    return sin(pi*k*x)*sin(2*pi*t)

# Initialise les courbes
def init():
    """Fonction d'initialisation"""
    plot.set_ydata(np.ma.array(x_tab, mask=True))
    return plot,

# Génère une trame d'animation
def frame(t):
    """Fonction de mise à jour: appelée pour chaque pas de temps t, et calcule les données à montrer à cet instant"""
    # Calcule les nouvelles valeurs de y(x, t)
    y_tab = [f(x,t) for x in x_tab]

    # Met à jour la courbe à afficher
    plot.set_ydata(y_tab) # 
    plot_titre.set_text("t = %4.2f" % t)
    return plot,


# Crée une animation
anim = animation.FuncAnimation(fig,
                               frame,
                               t_tab,
                               init_func=init,
                               interval=dt)
                               blit=True)

if True: # remplacer par 'if False' pour passer l'enregistrement 
    print ("Enregistrement de l'animation")
    anim.save('animation.mp4', fps = int(1/dt))

# Affiche l'animation
plt.show()
