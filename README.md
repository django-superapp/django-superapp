# Django SuperApp
**Superapp** boosts developer efficiency by allowing them to start projects quickly with **pre-built standalone apps**. Each app has its own `settings.py` and `urls.py` files, which are automatically recognized by the system. This modular setup makes Django projects more organized and scalable, saving developers time and effort.

![django-superapp-demo](https://django-superapp.bringes.io/assets/docs/admin-portal/admin-portal.png "Django SuperApp")

### Getting Started
```bash
# Install django_superapp
pipx install django_superapp --force

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

# Setup env variables
export $(cat .env.local | xargs)

# Apply migrations
docker-compose exec web python3 manage.py migrate;

# Create superuser
docker-compose exec web python3 manage.py createsuperuser

# Open the web interface
http://localhost:8080/
```

### Documentation
For a more detailed documentation, visit [https://django-superapp.bringes.io](https://django-superapp.bringes.io).

### Development
```bash
source venv/bin/activate
make install-requirements
make install

# If you want to release it
make release
```
