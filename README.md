# TrailMatch
This README is intended for dev use only and is **not** the final README for the project.

## Running Django server
Before you can see the website hosted on your local machine, you first need to run the Django server. All you need to do is be at the **root directory** of the project and run `python manage.py runserver`. This will start the website on your local machine and you can view it at `localhost:8000` in your browser. You can change what address and port Django runs the server on using `python manage.py runserver [ipaddress]:[port]`

## Making Changes to Django
When making changes to the backend, simply running `runserver` won't let you see any changes. First you must run `python manage.py makemigrations` everytime you make a change to any of Django's models. To then push those changes to the website, run `python manage.py migrate`. After this, you can rerun the server to see the changes. You can also look at the current migrations at anytime using `python manage.py showmigrations`.

## Making Changes to JavaScript code
Any JavaScript code that is **not considered inline** (pasted directly using the `script` tag) needs to be built using `npm` and registered in `trailsite/urls.py` if it's a new JavaScript file. Please make sure that [npm and Node.js is already installed](https://nodejs.org/en/download/)!
### Existing JavaScript File
If you are editing an existing JavaScript file, you simply need to make sure the Django server is running in a separate terminal window, open a new terminal window, and run `npm run dev`. This will **continuously compile** JavaScript code until stopped. This means it will immediately compile any changed JavaScript files on the fly. However, the Django server will have to be restarted for each change.
### New JavaScript File
This works the same as an existing file, just with an extra step. If you are using an existing template, skip step 1.
1) You first need to tell Django where the new template is located in the `trailsite/urls.py` file. If I were adding the template `hello.html`, I would add the line inside `urlpatterns`: `path('hello/', TemplateView.as_view(template_name='hello.html')),`. Make sure to add the comma at the end of this line! That's not a mistake.
2) Inside the template where you want the script, add the line: `<script src="{% static '[script-name].js' %}"></script>`, replacing `[script-name]` with the name of the .js file you want to create.
3) Once your template is setup, create a .js file in the assets folder with your chosen script name. For the element ID, make sure to pass the same name of the ID you want to manipulate that is in your template (the `<div id="blah" </div>` portion).
