from openvector import OpenVectorSpace
import numpy as np

ovs = OpenVectorSpace()
a_ = np.array([1, 2, 3])
b_ = np.array([3, 2, 1])
p_ = ovs.ratio_divider(a_, b_)
ovs.plot([a_, b_, p_])
ovs.add_legend(['a', 'b'])
ovs.set_labels()
ovs.set_lims()
ovs.show()