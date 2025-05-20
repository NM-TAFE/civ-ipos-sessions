# Project name
PACKAGE_NAME=flask_tic_tac_toe_setup
VERSION=0.1.0
DIST_DIR=dist

.PHONY: help clean build install reinstall run

help:
	@echo "Usage:"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make build        - Build .tar.gz and .whl files"
	@echo "  make install      - Install the built package"
	@echo "  make reinstall    - Force reinstall the package"
	@echo "  make run          - Run the Flask app"

clean:
	rm -rf build/ $(DIST_DIR)/ *.egg-info

build: clean
	poetry build

install:
	pip install $(DIST_DIR)/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl

reinstall:
	pip install --force-reinstall $(DIST_DIR)/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl

run:
	FLASK_APP=$(PACKAGE_NAME) flask run