install:venv
	@echo "Installing requirements..."
	.venv/bin/pip install -r requirements.txt --upgrade
	
venv:
	if [ ! -d ".venv" ]; then python3 -m venv .venv; fi

app:venv
	@echo "Creating app..."
	.venv/bin/python3 -m streamlit run app/main.py