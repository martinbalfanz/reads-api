.PHONY: clean develop lint

help:
	@echo "clean - clean out *.pyc and other files"
	@echo "develop - install all packages required for development"
	@echo "lint - check style with flake8"


clean:
	find . -iname "*.pyc" -delete
	find . -iname "*~" -delete
	find . -iname "#*" -delete

develop:
	@echo "Installing python pdendencies"
	pip install --upgrade pip wheel
	pip install --use-wheel -r ./src/requirements.txt
	@echo ""

lint:
	@echo "----- Outdated dependencies -----"
	pip list --outdated

	@echo "----- Prospector analysis -----"
	prospector

	@echo "----- Bandit analysis -----"
	bandit -r ./src/
