# Django SuperApp
SuperApp is a framework on top of Django, designed to accelerate the development of software projects for startups. It incorporates all the powerful features of Django, plus additional tools to seamlessly integrate various applications.

![django-superapp-demo](https://django-superapp.bringes.io/assets/docs/admin-portal/admin-portal.svg "Django SuperApp")

### Getting Started
```bash
# Install django_superapp
pipx install django_superapp

# Setup the project
django_superapp bootstrap-project \
        --template-repo https://github.com/django-superapp/django-superapp-default-project \
        ./my_superapp;
cd my_superapp;

# Setup Admin Portal
cd superapp/apps;
django_superapp bootstrap-app \
    --template-repo https://github.com/django-superapp/django-superapp-admin-portal \
    ./admin_portal;
cd ../../;

# Setup Authentication
cd superapp/apps;
django_superapp bootstrap-app \
    --template-repo https://github.com/django-superapp/django-superapp-authentication \
    ./authentication;
cd ../../;

# Start the project
make setup-sample-env
make start-docker

# Apply migrations
docker-compose exec web python3 manage.py migrate;

# Create superuser
docker-compose exec web python3 manage.py createsuperuser

# Open the browser
http://localhost:8000/
```

### Documentation
For a more detailed documentation, visit [https://django-superapp.bringes.io](https://django-superapp.bringes.io).

### Development
```bash
source venv/bin/activate
make install-requirements
make install
make release
```
