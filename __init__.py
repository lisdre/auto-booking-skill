from mycroft import MycroftSkill, intent_file_handler
# from picamera import PiCamera
# from time import sleep
import requests


class AutoBooking(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('booking.auto.intent')
    def handle_booking_auto(self, message):
        ## Lijian part start
        # self.speak_dialog("init camera")
        # camera = PiCamera()
        # self.speak_dialog("starting preview")
        # camera.start_preview()
        # self.speak_dialog("wait for 5 seconds")
        # sleep(5)
        # path = '/home/pi/ISAPM/temp/image.jpg'
        # self.speak_dialog("taking photo capture")
        # camera.capture(path)
        # camera.stop_preview()
        # self.speak_dialog("taking photo succeeded!")
        ## Lijian part end
        
        ## Li Sheng part start
        firstName = self.get_response("What is you first name")
        lastName = self.get_response("What is you last name")
        self.speak_dialog("Hi " + firstName + " " + lastName)
        contactNumber = self.get_response("What is you contact number")
        self.speak_dialog("Your contact number is " + contactNumber)
        email = self.get_response("What is you email address")
        self.speak_dialog("Your email address is " + email)
        dob = self.get_response("When is your birthday")
        self.speak_dialog("Your birthday is " + dob)
        facility = self.get_response("Which type of facility you prefer")
        self.speak_dialog("The type of facility you choose is " + facility)
        bookingDate = self.get_response("Which date you want to booking")
        self.speak_dialog("Your booking date is " + bookingDate)
        self.log.info("firstName:" + firstName + ",lastName:" + lastName + ", contactNumber:" + contactNumber + ", email:" + email + ", dob:" + dob + ", facility:" + facility + ", bookingDate:" + bookingDate)

        url = 'https://google.com'
        myobj = {
          "First_Name": firstName,
          "Last_Name": lastName,
          "Contact_No": contactNumber,
          "Email": "dsfdssf@gmail.com",
          "Address": email,
          "DOB": dob,
          "Medical_Description" : "",
          "Treatment_Facility" : facility,
          "Date_Booking": bookingDate,
          "Sore_Throat": True,
          "Fever": False
        }

        res = requests.post(url, data = myobj)
        self.log.info(res)
        ## Li Sheng part end
        
        ## Yan Bo part start
        ## Yan Bo part end

def create_skill():
    return AutoBooking()

