from models.event import *

event_1 = Event("2020-03-21", "Cheese Rolling Competition", 2, "Room 3a", "The annual cheese-rolling extravaganza, in which cheese is rolled and hearts are won", False)

event_2 = Event("2032-12-20", "Lonely Hearts: Paint by Number", 22, "Room 2b (or not 2b)", "Find someone to colour your pallette at this weekly singles painting extravaganza!", True)

event_3 = Event("2028-10-10", "Babybop Kid Rave", 300, "Stuart and John Memorial Auditorium", "Chaos reigns at this, the first of its kind, the baby rave - no parents allowed! Extravaganza.", True)

events_list = [event_1, event_2, event_3]

def add_new_event(event):
    events_list.append(event)

def recurring_status(recurring):
    if recurring.lower() == "true":
        return True


