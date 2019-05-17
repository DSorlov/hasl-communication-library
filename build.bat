rmdir /S dist 
python setup.py sdist
twine upload dist/*