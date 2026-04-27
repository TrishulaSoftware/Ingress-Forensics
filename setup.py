from setuptools import setup
from Cython.Build import cythonize

setup(
    name="IngressForensics",
    ext_modules=cythonize("rag_sanitizer.py", compiler_directives={'language_level': "3"}),
    zip_safe=False,
)