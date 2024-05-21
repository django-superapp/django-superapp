# Django SuperApp
SuperApp is a framework on top of Django, designed to accelerate the development of software projects for startups. It incorporates all the powerful features of Django, plus additional tools to seamlessly integrate various applications.

![django-superapp-demo](https://django-superapp.bringes.io/assets/docs/admin-portal/admin-portal.svg "Django SuperApp")

### Getting Started
```bash
pipx install django_superapp
django_superapp create-project --project-template default ./my_superapp
cd my_superapp
django_superapp create-app --app-template sample_app
make setup-sample-env
make start-docker
```

### Documentation
For a more detailed documentation, visit [https://django-superapp.bringes.io](https://django-superapp.bringes.io).

### Development
```bash
make install-requirements
make install
make release
```
