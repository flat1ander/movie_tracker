# Install pipenv if not already installed
pip3 install --user pipenv

# Activate the virtual environment
/opt/render/project/src/.venv/bin/pipenv shell

# Install dependencies
pipenv install --ignore-pipfile

# Run the build commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate
