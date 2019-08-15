import setuptools

with open("./README.md", "r") as fh:
    readme = fh.read()

INSTALL_REQUIRE = [
	'flask>=1.0.1',
	'pysqlite3>=0.2.0',
	'waitress>=1.2.0'
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Other Environment',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development',
    'Topic :: Adaptive Technologies',
    'Topic :: System :: Distributed Computing',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
]

setuptools.setup(
     
    name="sharkradar",
    version="1.1.2",
    url="https://bmonikraj.github.io/sharkradar",
    project_urls={
        "Documentation": "https://github.com/bmonikraj/sharkradar/wiki",
        "Code": "https://github.com/bmonikraj/sharkradar",
        "Issue tracker": "https://github.com/bmonikraj/sharkradar/issues",
    },
    license="BSD-3-Clause",
    author="Monik Raj Behera",
    author_email="bmonikraj@gmail.com",
    maintainer="Preetam Keshari Nahak",
    maintainer_email="preetamnahak@gmail.com",
    description="Lightweight micro service registry and discovery tool, compatible with any HTTP based microservice",
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=CLASSIFIERS,
    packages=setuptools.find_packages("src"),
    package_dir={"":"src"},
    include_package_data=True,
    python_requires=">=2.7, >=3",
    install_requires=INSTALL_REQUIRE,
    entry_points={"console_scripts": ["sharkradar = sharkradar.Main.Main:main"]},
 )