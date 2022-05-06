from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='query',
    version='0.0.0.1',
    description='Build query for sqlite.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Arnaldo Ono',
    author_email='git@onoarnaldo.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],

    keywords='flask',
    package_dir={'': 'src', 'query': 'src/query'},
    packages=find_packages(where='src'),
    python_requires='>=3.10',

    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },

    # include_package_data=True,
    # package_data={'your_project': ['utils/data/*.csv']},
)