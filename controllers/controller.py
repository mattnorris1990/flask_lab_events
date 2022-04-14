from flask import render_template, request
from app import app
from models.event import Event
from models.events_list import add_new_event, events_list, recurring_status

@app.route('/')
def home():
    return "The Hopper: Edinburgh's premier arts venue"

@app.route('/allevents')
def all_events():
    return render_template('index.html', title= "All Events", events_list=events_list)

@app.route('/addevent', methods=["POST"])
def add_event():
    print(request.form)

    event_date = request.form["adddate"]
    event_name = request.form["eventname"]
    event_guests_number = int(request.form["numberofguests"])
    event_room_location = request.form["roomlocation"]
    event_description = request.form["description"]
    event_recurring = recurring_status(request.form["recurring"])

    new_event = Event(event_date, event_name, event_guests_number, event_room_location,event_description, event_recurring)
    
    print(new_event)

    add_new_event(new_event)

    return render_template('index.html', title= "All Events", events_list=events_list)

@app.route('/allevents/delete/<index>')
def delete_an_event(index):
    events_list.pop(int(index))

    return render_template('index.html', title= "All Events", events_list=events_list)
