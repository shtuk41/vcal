from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def plotvec(vec, ax, color, width):
	xline = [0, vec[0]];
	yline = [0, vec[1]];
	zline = [0, vec[2]];
	ax.plot3D(xline, yline, zline, color, linewidth=width);
    
def plotVecUsePos(vec, posvec, ax, color, width):
	xline = [posvec[0], posvec[0] + vec[0]];
	yline = [posvec[1], posvec[1] + vec[1]];
	zline = [posvec[2], posvec[2] + vec[2]];
	ax.plot3D(xline, yline, zline, color, linewidth=width);







		

