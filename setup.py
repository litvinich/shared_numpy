import platform
import subprocess
import sys
from distutils.core import Extension, setup


if sys.version_info[0] == 3 and sys.version_info[1] == 6:
    subprocess.run(
        ["python", "shared_numpy/py36_clinic.py", "shared_numpy/posixshmem.c"]
    )
elif sys.version_info[0] == 3 and sys.version_info[1] == 7:
    subprocess.run(
        ["python", "shared_numpy/py37_clinic.py", "shared_numpy/posixshmem.c"]
    )
elif sys.version_info[0] == 3 and sys.version_info[1] == 8:
    subprocess.run(
        ["python", "shared_numpy/py37_clinic.py", "shared_numpy/posixshmem.c"]
    )
else:
    raise ValueError("Must run on Python 3.6, 3.7 or 3.8")


linux_module = Extension(
    "shared_numpy/_posixshmem",
    define_macros=[
        ("HAVE_SHM_OPEN", "1"),
        ("HAVE_SHM_UNLINK", "1"),
        ("HAVE_SHM_MMAN_H", 1),
    ],
    libraries=["rt"],
    sources=["shared_numpy/posixshmem.c"],
)


darwin_module = Extension(
    "shared_numpy/_posixshmem",
    define_macros=[
        ("HAVE_SHM_OPEN", "1"),
        ("HAVE_SHM_UNLINK", "1"),
        ("HAVE_SHM_MMAN_H", 1),
    ],
    sources=["shared_numpy/posixshmem.c"],
)


setup(
    name="shared-numpy",
    version="1.1.1",
    description="Shared Numpy",
    py_modules=["shared_numpy"],
    ext_modules=[linux_module]
    if platform.system() == "Linux"
    else [darwin_module]
    if platform.system() == "Darwin"
    else [],
)
