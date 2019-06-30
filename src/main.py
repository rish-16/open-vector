from openvector import OpenVectorSpace
import numpy as np

ovs = OpenVectorSpace()
a_ = np.array([1, 2, 3])
b_ = np.array([3, 5, 1])
c_ = ovs.cross(a_, b_) # cross product
d_ = ovs.kvecmul(2, c_) # multiplying scalar to vector

ovs.plot([a_, b_, d_])
ovs.add_legend(['a', 'b', 'd'])
ovs.show()