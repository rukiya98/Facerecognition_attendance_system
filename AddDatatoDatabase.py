


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-4eecf-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "14622":
        {
            "name": "Kalana Bandaranaayke",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "14635":
        {
            "name": "Rukshan Edirisinghe",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "Bad",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "14846":
        {
            "name": "Sandali Perera",
            "major": "Management",
            "starting_year": 2022,
            "total_attendance": 23,
            "standing": "Good",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"14800":
        {
            "name": "Eranga Aberathne",
            "major": "Physics",
            "starting_year": 2023,
            "total_attendance": 1,
            "standing": "Bad",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"14871":
        {
            "name": "Nethmi Wijayasekara",
            "major": "Chemistry",
            "starting_year": 2020,
            "total_attendance": 9,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)