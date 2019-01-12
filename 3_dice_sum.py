from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools
from itertools import product, combinations
import numpy as np
from matplotlib.widgets import Slider

#constants
NUM_DICE = 3
K_INIT = 8  #initial guess for most probable sum
ROLL_MIN = 1
ROLL_MAX = 6
MIN_SUM = NUM_DICE * ROLL_MIN
MAX_SUM = NUM_DICE * ROLL_MAX

#possible outcomes
dice_rolls = range(ROLL_MIN, ROLL_MAX + 1) #range() excludes the last value
possible_sums = range(MIN_SUM, MAX_SUM + 1) #(1,1,1) to (6,6,6)
cart_prod = [dice_rolls, dice_rolls, dice_rolls]    #Cartesian Product of 3 dice rolls
sample_space = list(itertools.product(*cart_prod))  #All possible triples (events)
sums = [sum(tup) for tup in sample_space]   #Corresponding sums from each event

#plane x + y + z = k
plane_pts, other_pts, other_sums = [], [], []
def genPlanePts(k):#solve for Z values at X,Y
    plane_pts.clear()
    other_pts.clear()
    other_sums.clear()
    X,Y = np.meshgrid(dice_rolls, dice_rolls)   #calculate X and Y as a grid of range 1-6
    Z = -1*X + -1*Y + k    #solve for Z values at X,Y
    for pt,s in zip(sample_space,sums):  #fetch all points that satisfy x+y+z=k
        if s == k:
            plane_pts.append(pt)    #all of their sums are k, no need to record
        else:
            other_pts.append(pt)
            other_sums.append(s)
    return (X,Y,Z)

def updateText(k):
    s = len(plane_pts)
    updated = str(s)
    updated += ' intersection'
    if s > 1:
        updated += 's' #grammar plural
    updated += '\nP(' + str(int(k)) + ') = ' + str(round(s/ROLL_MAX**NUM_DICE,6))   #probability to 6 decimal places
    return updated

#start setting up plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d', proj_type = 'ortho', aspect='equal')
ax.view_init(15, 20)
fig.canvas.set_window_title("3 Dice Sum")

fig.suptitle('Sample Space of 3 Dice\nintersected by x + y + z = k', size=18, ha='center')
txt = fig.text(0.1, 0.75, updateText(K_INIT), fontsize=14)

#add colorbar
colmap = plt.get_cmap('magma', MAX_SUM - MIN_SUM + 1)   #18 - 3 + 1 = 16 possible sums
norm = mpl.colors.Normalize(vmin=MIN_SUM-1,vmax=MAX_SUM)
sm = plt.cm.ScalarMappable(cmap=colmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ticks=possible_sums, cax=fig.add_axes([.85, 0.2, 0.04, 0.6]))
cbar.ax.set_title('Sum')

#plot plane and lattice points
def replot(k):
    ax.clear()
    #cube
    r = [ROLL_MIN, ROLL_MAX]
    for s,e in combinations(np.array(list(product(r,r,r))),2):
        if np.sum(np.abs(s-e)) == r[1] - r[0]:
            ax.plot3D(*zip(s, e), color='gray')
    #plane
    X,Y,Z = genPlanePts(k)
    surf = ax.plot_surface(X, Y, Z, alpha=0.2, color='m')
    #sample space of lattice points
    sctr = ax.scatter(*zip(*other_pts), c=other_sums,  facecolor=other_sums, cmap=colmap, s=50, marker='o', alpha=0.6) #sum points not in plane
    highlight = ax.scatter(*zip(*plane_pts), c='gold',  facecolor='gold', edgecolor='k', linewidth=1, s=250, marker='*')#highlights points in the plane in yellow
    #output text
    txt.set_text(updateText(k))
    #plot guides
    ax.set_xlim(ROLL_MIN, ROLL_MAX)
    ax.set_ylim(ROLL_MIN, ROLL_MAX)
    ax.set_zlim(ROLL_MIN, ROLL_MAX)
    ax.set_xlabel('Die 1')
    ax.set_ylabel('Die 2')
    ax.set_zlabel('Die 3')

replot(K_INIT)

#interactive elements
axk = plt.axes([0.2, 0.1, 0.6, 0.04], facecolor='w')
sk = Slider(axk, 'k', MIN_SUM, MAX_SUM, valinit=K_INIT, valstep=1, valfmt="%i", color='gold')
def update(val):
    k = sk.val
    replot(k)
    fig.canvas.draw_idle()
sk.on_changed(update)

mng = plt.get_current_fig_manager() 
mng.window.resizable(False, False)
plt.show()