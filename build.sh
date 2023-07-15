# Activate the virtual environment
source /opt/render/project/src/.venv/bin/activate

# Install dependencies
pip3 install -r deps.txt

# Run the build commands
echo "Running the build commands..."
mkdir -p staticfiles
chmod -R 755 staticfiles
echo "Collecting static files..."
python3 manage.py collectstatic --no-input
echo "Applying migrations..."
python3 manage.py migrate

