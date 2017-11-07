test:
	py.test --pep8

clean:
	rm -rf .cache
	rm -fr build dist .egg twisted_adb.egg-info
	rm -rf docs/_build/

install:
	pip install -e .
