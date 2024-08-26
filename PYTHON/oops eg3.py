class vehicle():

    def start(self):
        print( "vehicle started")
    
class car(vehicle):

    def start(self):
        print("car started")
    
innova=car()
innova.start()
