class Event():

    def __init__(self, input_date, input_event_name, input_number_of_guests, input_room_location, input_description, input_recurring):
        self.date = input_date
        self.name = input_event_name
        self.number_of_guests = input_number_of_guests
        self.room_location = input_room_location
        self.description = input_description
        self.recurring = input_recurring
    