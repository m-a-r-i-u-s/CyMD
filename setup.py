import distutils.core
import Cython.Build
import numpy as np
import os
os.environ["CC"] = "/usr/bin/clang"
distutils.core.setup(ext_modules = Cython.Build.cythonize("coords.pyx"), include_dirs=[np.get_include()], zip_safe=False)
