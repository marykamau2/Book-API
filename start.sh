export SECRET_KEY="leresiSekjdskhdohsjd"
export MAIL_USERNAME='kevinleparwa@gmail.com'
export MAIL_PASSWORD='0717025499'
export SECRET_KEY="kenya254"

flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
python3 manage.py server
