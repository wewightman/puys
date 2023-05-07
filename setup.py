from setuptools import setup

# load requirements list
with open("requirements.txt", 'r') as f:
    reqs = f.readlines()

with open("req_depends.txt", 'r') as f:
    reqdeps = f.readlines()

# run setup tools
setup(
    name='pyus',
    description="C-Backed beamforming engines",
    author="Wren Wightman",
    author_email="wew12@duke.edu",
    packages=[
        'pyus',
        'pyus.bmfrm'
    ],
    install_requires=reqs,
    dependency_links=reqdeps,
    version="0.0.0"
)