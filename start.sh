export SECRET_KEY="kenya254"

flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
python3.9 manage.py server
