import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tasks",
    version="0.0.1",
    author="HazemMeqdad",
    author_email="hazemmeqdad@gmail.com",
    description="A simple package to make async task background",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DwcTeam/tasks",
    project_urls={
        "Bug Tracker": "https://github.com/DwcTeam/tasks/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["tasks"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)