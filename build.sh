pip3 install -r deps.txt

python3 manage.py collectstatic --no-input

python3 manage.py migrate