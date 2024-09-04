# Wikipedia Race

Setting up the environment
On Windows:

Backend
1. create virtual env: python -m venv myenv
2. activate env: myenv\Scripts\activate
3. install django: pip install django
4. start the django project: django-admin startproject WikiRace
5. start the django app: python manage.py startapp wikiapp
6. install django restframework: pip install djangorestframework
7. migrate database: python manage.py migrate
8. run backend: python manage.py runserver

Frontend
1. install react: npm install -g create-react-app
2. create frontend: npx create-react-app frontend
3. change directory: cd frontend
4. start: npm start
5. inside .env write: SKIP_PREFLIGHT_CHECK=true


All done!
