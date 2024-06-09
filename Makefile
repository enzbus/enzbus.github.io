.PHONY: local_build

local_build:
	python -m venv --system-site-packages env
	pip install sphinx
	sphinx-build source _build
	open _build/index.html
	
	
