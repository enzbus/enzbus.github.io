.PHONY: local_build

local_build:
	python -m venv --system-site-packages env
	env/bin/python -m pip install sphinx pydata-sphinx-theme
	env/bin/python -m sphinx build source _build
	open _build/index.html
	
	
