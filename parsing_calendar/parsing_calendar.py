from ics import Calendar, Event
from datetime import datetime
import pytz


cal = Calendar()

# Define the revised timetable
timetable = {
    '2024-08-20': [
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '10:00', 'end': '11:00', 'location': 'Room no: 106,104,220,221,014'},
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '11:10', 'end': '12:10', 'location': 'Room no: 106,104,220,221,014'},
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '14:15', 'end': '15:15', 'location': 'Room no: 106,104,220,221,014'},
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '15:15', 'end': '16:15', 'location': 'Room no: 106,104,220,221,014'}
    ],
    '2024-08-21': [
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '10:00', 'end': '11:00', 'location': 'Room no: 106,104,220,221,014'},
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '11:10', 'end': '12:10', 'location': 'Room no: 106,104,220,221,014'},
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '14:15', 'end': '15:15', 'location': 'Room no: 106,104,220,221,014'},
        {'summary': 'B.tech 2022-2026 Applicative Project (Project Evaluation -1)', 'start': '15:15', 'end': '16:15', 'location': 'Room no: 106,104,220,221,014'}
    ],
    '2024-08-22': [
        {'summary': 'Text Analytics', 'start': '10:00', 'end': '11:00', 'instructor': 'Prof. Rajan Kumar Pandit', 'location': 'Room no: 221'},
        {'summary': 'AIML 2022 B (Leopards) Software Engineering', 'start': '11:10', 'end': '12:10', 'instructor': 'Dr. Purushotham M', 'location': 'Room no: 221'},
        {'summary': 'AIML 2022 B (Leopards)', 'start': '12:10', 'end': '13:10', 'location': 'Room no: 221'},
        {'summary': 'Responsible Leadership', 'start': '14:15', 'end': '15:15', 'instructor': 'Dr. Dibyagana Biswas', 'location': 'Room no: 221'},
        {'summary': 'Data Engineering and Modeling', 'start': '15:15', 'end': '16:15', 'instructor': 'Dr. Ayushi Arya', 'location': 'Room no: 220'}
    ],
    '2024-08-23': [
        {'summary': 'Data Mining Lab', 'start': '10:00', 'end': '11:00', 'instructor': 'Prof. Ramanjaneyulu Yannam, Mr Ravi Kumar', 'location': 'Room no: 221'},
        {'summary': 'Data Mining Lab', 'start': '11:10', 'end': '12:10', 'instructor': 'Prof. Ramanjaneyulu Yannam, Mr Ravi Kumar', 'location': 'Room no: 221'},
        {'summary': 'AIML 2022 B (Leopards) Software Engineering', 'start': '12:10', 'end': '13:10', 'instructor': 'Dr. Purushotham M', 'location': 'Room no: 221'},
        {'summary': 'Data Mining', 'start': '14:15', 'end': '15:15', 'instructor': 'Prof. Ramanjaneyulu Yannam', 'location': 'Room no: 221'},
        {'summary': 'Data Engineering and Modeling Lab', 'start': '15:15', 'end': '16:15', 'instructor': 'Dr. Ayushi Arya, Ms Navitha', 'location': 'Room no: 221'},
        {'summary': 'Data Engineering and Modeling Lab', 'start': '16:20', 'end': '17:20', 'instructor': 'Dr. Ayushi Arya, Ms Navitha', 'location': 'Room no: 221'}
    ]
}

tz = pytz.timezone('Asia/Kolkata')

def create_event(date, event_details):
    start_time = datetime.strptime(f"{date} {event_details['start']}", "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(f"{date} {event_details['end']}", "%Y-%m-%d %H:%M")
    
    event = Event()
    event.name = event_details['summary']
    event.begin = tz.localize(start_time)
    event.end = tz.localize(end_time)
    event.location = event_details.get('location', '')
    event.description = event_details.get('instructor', '')
    return event

for date, events in timetable.items():
    for event_details in events:
        event = create_event(date, event_details)
        cal.events.add(event)

with open('timetable.ics', 'w') as file:
    file.write(cal.serialize())
