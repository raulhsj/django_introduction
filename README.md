A prior virtual env is mandatory to get the app to run

```
pip install virtualenv
```

Virtual env creation (setting python3)

```
virtualenv -p python3 <name>
```

or just

```
virtualenv <name>
```

Before using the env, activation is needed

```
source <name>/bin/activate
```

Finally, django installation

```
pip install django
```

Watch out for the command, because it is `django-admin`, and then

```
django-admin startproject <my_project>
```
