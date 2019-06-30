# open-vector
A computation and visualisation library for vector operations and manipulation to simplify Machine Learning math.

---

### Installation
To install `openvector`, you can simply use `pip`:
```bash
pip install openvector
```

---

### Usage
To start visualising vectors, you first need to instantiate an `OpenVectorSpace` object that enables you to draw, manipulate and operate on vectors.
```python
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
```
This should render a figure that looks like this:
<img src="assets/render." />

---

### Features
`openvector` comes with a range of functions and utilities to use to manipulate vectors. You can test theorems on vectors and can get their reflections. Some of these features include:

1. Ratio Theorem
2. Reflection 
3. Foot of a perpendicular from a line
4. Foot of a perpendicular from a place
5. Angles between lines, vectors, and planes