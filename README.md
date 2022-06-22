# Django Admin Panel

Time to make a pretty admin panel.

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M12-Django-Admin).
2. Make sure to have `python 3.9.13` installed (use `pyenv install 3.9.13` to ensure it is installed).
3. Install the project dependencies using `poetry install`.
4. Run the migrations using `poetry run manage migrate`.
5. Create a superuser using `poetry run manage createsuperuser`.

## Quick Scaffold

Use [this](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/) to your advantage. For steps 2 - 4, you'll need to make these changes in `urls.py`.

1. Register all of our ninja models in `admin.py`.
   - Import `models` from `ninjas`
   - Add all the `models` to `list` a variable called `to_register`
   - Register the `to_register` variable in the admin site
2. Change the `title` of the admin site login page from `Django Administration` to `Naruto Admin`.
3. Change the `subtitle` of the admin site after logging in from `Site Administration` to `Welcome to Naruto's Portal`.
4. Change the HTML title page from `Django site admin` to `Naruto Portal`.
5. Fix `Academys` on the admin site to be `Academies` (**HINT:** you'll need to change this on the model level.)

## Custom List View

Use [this](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/) to your advantage.

### Village List View

1. Display both the `id` and `name` in the list page.
2. Add a custom list display that shows the current number of ninjas.
   - Use [this](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count) to count stuff like a pro
   - The filter should be the cohort that has an end date greater than `timezone.now()`
   - From the active cohorts get the students that have `graduated_at=null` and count this queryset
3. Make both the `id` and `name` link to the edit page for a village.

### Academy List View

1. Display both the `id` and `founded` in the list page.
2. Add a custom list display that shows the village name.
3. Make both the `id` and `village_name` link to the edit page.

### Cohort List View

1. Display the `id`, `start_at`, `end_at` in the list page.
2. Add a custom list display that shows the count of `senseis` in this cohort.
3. Add a custom list display that shows the count of `ninjas` in this cohort.
4. Make the `id`, `start_at`, and `end_at` link to the edit page.

### Sensei List View

1. Display the `id` and `name` in the list page.
2. Add a custom list display that shows the count of `cohorts` this `sensei` has been in.
3. Make the `id` and `name` link to the edit page.

### Ninja List View

1. Display the `id` and `name` in the list page.
2. Add a custom list display that shows if the `ninja` graduated or not (displays `True` or `False`).
3. Make the `id` and `name` link to the edit page.

#### Ninja List View Bonus

Make the custom list display for `graduated` show a checkmark/cross icon instead of `True/False`.

## Filters

[This](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter) link is your best friend.

1. Add a filter in the `sensei` list view for the `cohort`.
2. Add a filter in the `ninja` list view for whether or not they graduated.

## Inlining Models

[This](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#inlinemodeladmin-objects) link is your new best friend.

Inline `Cohort` in the `Academy` edit view. So if an admin goes to the `Academy` edit view, they should be able to create cohorts on the spot.

## Actions

[Seems like you have many best friends.](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/actions/)

Add an action that marks all selected `ninjas` to have graduated at `timezone.now()`.
