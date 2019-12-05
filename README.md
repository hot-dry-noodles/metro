# metro



## Requirements

- Python 3.7+ with pip

- Run the command

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip django django-admin djangorestframework pylint pylint-django
pip install django_filter
# create a user to use admin panel
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
# login the admin panel with the username and password just entered
python manage.py runserver
```

## APIs

### Station
=======
### Station, Line and Route
>>>>>>> 94c587dc87862e0bf19664e34b0024ddfab731df

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
t = Station(name='街道口')
t = Station(name='华中科技大学')
t = Station(name='汉口北')

# insert it into the table
t.save()

# similarily, add elements in line and route table:
from booking.models import Line
from booking.models import Route
entry = Line(line_name='b', station_name='街道口')
entry.save()
entry = Line(line_name='b', station_name='华中科技大学')
entry.save()
entry = Line(line_name='a', station_name='汉口北')
entry.save()

s1 = qs[1]
s0 = qs[0]
s2 = qs[2]
r = Route(begin=s0, end=s1, distance=7.126, price=3, route='李祺彦到此一游')
r.save()
r = Route(begin=s0, end=s2, distance=26.608, price=7, route='李祺彦到此一游')
r.save()
r = Route(begin=s1, end=s2, distance=33.74, price=8, route='李祺彦到此一游')
r.save()

# check if it exists
q = Station.objects.get(name='first ternimal')
print(q.name)
```

2. Then check whether we can get data using API:

```bash
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/stations/

```
```bash
curl -H 'curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/routes/\?begin\=1\&end\=2
```
```bash
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/lines/\?line_name\=b
>>>>>>> 94c587dc87862e0bf19664e34b0024ddfab731df
```
3. You would see something like this:

```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "街道口"
        },
        {
            "name": "华中科技大学"
        },
        {
            "name": "光谷广场"
        },
        {
            "name": "汉口北"
        }
    ]
}
```

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "line_name": "b",
            "station_name": "街道口",
            "first_working": "",
            "last_working": "",
            "first_off": "",
            "last_off": ""
        },
        {
            "line_name": "b",
            "station_name": "华中科技大学",
            "first_working": "",
            "last_working": "",
            "first_off": "",
            "last_off": ""
        }
    ]
}
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "begin": "http://127.0.0.1:8000/api/stations/1/",
            "end": "http://127.0.0.1:8000/api/stations/2/",
            "distance": 7.126,
            "price": 3,
            "route": "李祺彦到此一游"
        }
    ]
}%
```

## Bugs

In booking/filters.py:

Linefilter and routefiler class are not used because of unsolved bugs.

If you can solve these bugs, you can use these filter classes to make advanced filters,  although it seems that we only need very simple filters.
