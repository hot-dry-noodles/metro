# metro



## Requirements

- Python 3.7+ with pip

- Run the command

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip django django-admin djangorestframework pylint pylint-django
# create a user to use admin panel
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
# login the admin panel with the username and password just entered
python manage.py runserver
```

## APIs

### Station

Access APIs using tools like `curl`:

```bash
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/stations/
```

If you see something like this:

```json
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```

It means there is no data in the table `Station`.

You can add elements via directly editing database file or from django shell:

1. Run `python manage.py shell`, then type:

```python
from booking.models import Station
# select all existing objects form table `Station`
qs = Station.objects.all()
if qs.count() > 0:
    qs.delete()
# create an object
t = Station(name='first ternimal')
# insert it into the table
t.save()
# check if it exists
q = Station.objects.get(name='first ternimal')
print(q.name)
```

2. Then check whether we can get data using API:

```bash
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/stations/
```

3. You would see something like this:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "first ternimal"
        }
    ]
}
```
