pip3 install -3 deps.txt

python3 manage.py collectstatic --no-input

python3 manage.py migrate