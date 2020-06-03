from models import User
import time

while True:
    User.query.all()
    first_user = User.query.filter_by(username='admin').first()
    print(first_user)
    time.sleep(10)