# Install dependencies
pip3 install -r deps.txt

# Run the build commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate

