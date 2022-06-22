# Django Admin Panel

Time to make a pretty admin panel.

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M12-Django-Admin).
2. Make sure to have `python 3.9.13` installed (use `pyenv install 3.9.13` to ensure it is installed).
3. Install the project dependencies using `poetry install`.
4. Run the migrations using `poetry run manage migrate`.
5. Create a superuser using `poetry run manage createsuperuser`.

## Quick Scaffold

For steps 2 - 4, you'll need to make these changes in `urls.py`.

1. Register all of our ninja models in `admin.py`.
   - Import `models` from `ninjas`
   - Add all the `models` to `list` a variable called `to_register`
   - Register the `to_register` variable in the admin site
2. Change the `title` of the admin site login page from `Django Administration` to `Naruto Admin`.
3. Change the `subtitle` of the admin site after logging in from `Site Administration` to `Welcome to Naruto's Portal`.
4. Change the HTML title page from `Django site admin` to `Naruto Portal`.
5. Fix `Academys` on the admin site to be `Academies` (**HINT:** you'll need to change this on the model level.)
