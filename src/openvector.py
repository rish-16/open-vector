import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

class OVSVector(object):
    def __init__(self, a_, m_=np.arrray([0,0,0])):
        self.a_ = a_
        self.m_ = m_

    def get_vector(self):
        return self.a_ + self.m_

class OVSPlane(object):
    def __init__(self):
        self.r_ = None
        self.n_ = None
        self.D_ = 0

class OpenVectorSpace(object):
    def __init__(self):
        self.container = []
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.vectors = []

    def kvecmul(self, k, pos_vec_a):
        return k * pos_vec_a

    def dot(self, pos_vec_a, pos_vec_b):
        return np.dot(pos_vec_a, pos_vec_b)

    def cross(self, pos_vec_a, pos_vec_b):
        return np.cross(pos_vec_a, pos_vec_b)

    def magnitude(self, pos_vec_a):
        mag = 0
        for i in range(len(pos_vec_a)):
            mag += pos_vec_a[i] ** 2
        mag = np.sqrt(mag)
        return mag
    
    def plot(self, vectors, color=None):
        """
        `vectors` should be a list of OVSVector Objects
        """
        if color == None:
            color = [np.random.choice(['#ff6b6b', '#5f27cd', '#54a0ff', '#feca57', '#1dd1a1']) for i in range(len(vectors))]
        for i in range(len(vectors)):
            if vectors[i].size == 3:
                self.vectors.append(vectors[i])
                self.ax.plot([0, vectors[i][0]], [0, vectors[i][1]], [0, vectors[i][2]], color=color[i])
                a = Arrow3D([0, vectors[i][0]], [0, vectors[i][1]], [0, vectors[i][2]], mutation_scale=20, lw=0, arrowstyle="-|>", color=color[i])
                self.ax.add_artist(a)
            else:
                print ('Expected vector of shape (3, 1) or (3, ). Got vector of shape {} instead.'.format(str(vectors[i].shape)))
                exit(0)

    def scatter(self, pos_vec_a, color="#ff6b6b"):
        self.ax.scatter(pos_vec_a[0], pos_vec_a[1], pos_vec_a[2], color=color, marker='o')

    def vvangle(self, pos_vec_a, pos_vec_b):
        numer = self.dot(pos_vec_a, pos_vec_b)
        denom = self.magnitude(pos_vec_a) * self.magnitude(pos_vec_b)
        angle = np.arccos(numer / denom)
        return angle

    def set_lims(self, direc=None, lims=[0, 7]):
        if direc:
            if direc == 'x':
                self.ax.axes.set_xlim3d(left=lims[0], right=lims[1])
            elif direc == 'y':
                self.ax.axes.set_ylim3d(bottom=lims[0], top=lims[1])
            elif direc == 'z':
                self.ax.axes.set_zlim3d(bottom=lims[0], top=lims[1])
            else:
                print ('Direction must correspond only to x, y, or z dimensions.')
                exit(0)
        else:
            self.ax.axes.set_xlim3d(left=lims[0], right=lims[1])
            self.ax.axes.set_ylim3d(bottom=lims[0], top=lims[1])
            self.ax.axes.set_zlim3d(bottom=lims[0], top=lims[1])

    def set_labels(self, xlabel='x', ylabel='y', zlabel='z'):
        if xlabel != None and ylabel != None and zlabel != None:
            self.ax.set_xlabel(xlabel)
            self.ax.set_ylabel(ylabel)
            self.ax.set_zlabel(zlabel)

    def add_legend(self, legend=None):
        if legend:
            self.ax.legend(legend)
        else:
            print ('Legend not detected. Specify a list of labels in a list.')

    def show(self):
        plt.show()

    def ratio_divider(self, pos_vec_a, pos_vec_b, gamma=1, mu=1):
        vec = self.kvecmul(gamma, pos_vec_a) + self.kvecmul(mu, pos_vec_b)
        k = mu + gamma
        divider_vector = self.kvecmul(k, vec)
        return divider_vector

    def draw_plane(self):
        plane = OVSPlane()
        self.fig.gca(projection='3d')
        plt3d.plot_surface(xx, yy, z, alpha=0.2)