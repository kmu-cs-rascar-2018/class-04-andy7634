#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        count = 0
        countt = 0
        counttt = 0
        distance = self.car.distance_detector.get_distance()
        self.car.accelerator.go_forward(30)
        while(count <= 3):
            distance = self.car.distance_detector.get_distance()
            print("Distance is", distance)
            time.sleep(0.001)
            if(distance < 15):
                count += 1
        self.car.accelerator.stop()
        time.sleep(1)
        self.car.accelerator.go_backward(30)
        time.sleep(4)
        self.car.accelerator.stop()
        time.sleep(1)
        distance = self.car.distance_detector.get_distance()
        self.car.accelerator.go_forward(50)
        while (countt <= 3):
            distance = self.car.distance_detector.get_distance()
            print("Distance is", distance)
            time.sleep(0.001)
            if (distance < 20):
                countt += 1
        self.car.accelerator.stop()
        time.sleep(1)
        self.car.accelerator.go_backward(50)
        time.sleep(4)
        self.car.accelerator.stop()
        time.sleep(1)
        distance = self.car.distance_detector.get_distance()
        self.car.accelerator.go_forward(70)
        while (counttt <= 3):
            distance = self.car.distance_detector.get_distance()
            print("Distance is", distance)
            time.sleep(0.001)
            if (distance < 25):
                counttt += 1
        self.car.accelerator.stop()
        time.sleep(1)
        self.car.accelerator.go_backward(70)
        time.sleep(4)
        self.car.accelerator.stop()
        time.sleep(1)
        distance = self.car.distance_detector.get_distance()







if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()


    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()