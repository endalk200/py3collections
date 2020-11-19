
# perform cl
cleanup:
	python setup.py clean
	rm -rv dist/ || true
	rm -rv .pytest_cache || true
	rm -rv src/py3collections.egg-info || true

clean_cache:
	rm -rv tests/__pycache__/ || true
	rm -rv src/pycollections/__pycache__/ || true
