install:
	if [ ! -d ".venv" ]; then make venv; fi
	@echo "Installing dependencies..."
	.venv/bin/pip install -r requirements.txt --upgrade
	
venv:
	@echo "Creating virtual env..."
	python3 -m venv .venv
