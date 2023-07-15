# Activate the virtual environment
source /opt/render/project/src/.venv/bin/activate

# Install dependencies
pip3 install -r deps.txt

# Run the build commands
mkdir -p staticfiles
chmod -R 755 staticfiles
python3 manage.py collectstatic --no-input
python3 manage.py migrate

