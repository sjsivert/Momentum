from flaskr.models import AdminUser, set_password, check_password, Job_applicant
from flask import session
import pytest

import flaskr.auth as auth 
import io

def test_add_admin_and_set_password(session):
    admin = AdminUser(username="test")

    set_password(admin, "test123")
    assert check_password(admin, "test") == False
    assert check_password(admin, "test123") == True

    session.add(admin)
    session.commit()  # save to DB

    assert admin.id > 0
    assert AdminUser.query.filter_by(username='test').first() is not None


def test_register(client):
    response = client.get('/auth/register')
    assert response.status_code == 200


@pytest.mark.parametrize(('first_name', 'last_name', 'email', 'password', 'type', 'date', 'message'), (
    ('', '', '','', 'Job_applicant', '2018-01-14', b'Mangler obligatoriske felter'),
    ('sindre', 'sivertsen', 'admin@admin.no','admin123', 'AdminUser', '2018-01-14', b''),
    ('sindre', 'sivertsen', 'admin@admin.no','admin123', 'Job_applicant', '2018-01-14', b''),
    ('sindre', 'sivertsen', 'admin@admin.no','admin123', 'Startup', '2018-01-14', b''),
    # ('sindre', 'sivertsen', 'admin@admin.no','admin123', 'AdminUser', '2018-01-14', b'Bruker finnes'),
))
def test_register_job_applicant_validate_input(client, first_name, last_name, email, password, type, date, message):
    response = client.post('/auth/register', data={'first_name': first_name, 'last_name': last_name,
        'email': email, 'password': password,  'type': type, 'date': date, 'password': password, 'file': (io.BytesIO(b'my file contents'), 'hello world.txt'),},
         follow_redirects=True,
         content_type='multipart/form-data')

    assert message in response.data

def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200

# tester at email legges på forsiden ved login
def test_sucsessfule_lgin(session, client, app):
    # make user
    user = AdminUser(email="admin@admin.no")
    set_password(user, "admin123")
    
    session.add(user)
    session.commit()

    response = client.post('auth/login',data={'email':"admin@admin.no", 'password': 'admin123'})

    assert not b'brukernavn' in response.data
    response2 = client.get('/')
    assert b'Min profil' in response2.data

# tester at cookie blir satt ved login
def test_login_session(client):
    client.get('/')
    session["test"] = True
    response = client.post('auth/login',data={'email':"admin@admin.no", 'password': 'admin123'})
    print("SESSION: ", session)
    assert session["user_email"] == "admin@admin.no"
