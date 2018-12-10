#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time
import RPi.GPIO as GPIO


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        count = 0
        countt = 0
        counttt = 0
        while(True):

            distance = self.car.distance_detector.get_distance()
            if distance <= 30 and distance != -1:
                count += 1
            if count >= 10:
                countt += 1
                print("aa")
                self.car.accelerator.stop()
                self.car.steering.turn(60)
                self.car.accelerator.go_forward(50)
                time.sleep(0.4)
                while(True):
                    if self.car.line_detector.read_digital() == [1,0,0,0,0] or self.car.line_detector.read_digital() == [1,1,0,0,0]:    
                        self.car.accelerator.stop()
                        time.sleep(0.1)
                        self.car.accelerator.go_backward(50)
                        time.sleep(0.4)
                        self.car.steering.turn(120)
                        self.car.accelerator.go_forward(50)
                        time.sleep(1)
                        break
                    else:
                        pass
                
                while(True):
                    if self.car.line_detector.read_digital() == [0,0,1,0,0] or self.car.line_detector.read_digital() == [1,1,1,0,0] or self.car.line_detector.read_digital() == [0,1,1,0,0]:
                        self.car.steering.turn(90)
                        self.car.accelerator.stop()
                        self.car.accelerator.go_backward(30)
                        time.sleep(0.05)
                        count = 0

                        break
                    else:
                        pass
                count = 0
            self.car.accelerator.go_forward(40)
            if(self.car.line_detector.read_digital() == [0,0,1,0,0]):
                continue
            elif(self.car.line_detector.read_digital() == [0,1,1,0,0]):
                self.car.steering.turn(80)
            
            elif(self.car.line_detector.read_digital() == [0,1,0,0,0]):
                self.car.steering.turn(75)
                
            elif(self.car.line_detector.read_digital() == [1,1,0,0,0]):
                self.car.steering.turn(50)
                
            elif(self.car.line_detector.read_digital() == [1,0,0,0,0]):
                self.car.steering.turn(45)
                
            elif(self.car.line_detector.read_digital() == [0,0,1,1,0]):
                self.car.steering.turn(95)
                
            elif(self.car.line_detector.read_digital() == [0,0,0,1,0]):
                self.car.steering.turn(100)
                
            elif(self.car.line_detector.read_digital() == [0,0,0,1,1]):
                self.car.steering.turn(120)
                
            elif(self.car.line_detector.read_digital() == [0,0,0,0,1]):
                self.car.steering.turn(125)
                
            elif(self.car.line_detector.read_digital() == [0,0,0,0,0]):
                self.car.accelerator.stop()
                self.car.steering.turn(120)
                self.car.accelerator.go_backward(30)
                while(True):
                    #print(self.car.line_detector.read_digital())
                    if(self.car.line_detector.read_digital() == [0,0,0,1,1] or self.car.line_detector.read_digital() == [0,0,0,0,1] or self.car.line_detector.read_digital() == [0,0,1,1,0]):
                        break
                    else:
                        continue
                self.car.accelerator.stop()
                self.car.steering.turn(70)
                self.car.accelerator.go_forward(25)
                while(True):
                    #print(self.car.line_detector.read_digital())
                    if(self.car.line_detector.read_digital() == [1,1,0,0,0] or self.car.line_detector.read_digital() == [1,0,0,0,0] or self.car.line_detector.read_digital() == [0,1,1,0,0] or self.car.line_detector.read_digital() == [0,0,1,0,0] or self.car.line_detector.read_digital() == [0,0,1,1,0]):
                        break
                    else:
                        continue
                self.car.accelerator.go_forward(85)
                time.sleep(0.1)
            elif(self.car.line_detector.read_digital() == [1,1,1,1,1]):
                if countt >= 1:
                    self.car.accelerator.stop()
                    time.sleep(1)
                    self.car.accelerator.go_backward(20)
                    time.sleep(0.3)
                    print(countt)
                    break
            
        self.car.accelerator.stop()
        time.sleep(1)
        


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()