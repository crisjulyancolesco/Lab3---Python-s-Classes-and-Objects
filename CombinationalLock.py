# Combo Lock class
class ComboLock:

    # Attributes (Status and Current Status)
    Current = 0
    Status = 0 

    # Constructor (3 number combination)
    def __init__(self, Secret1, Secret2, Secret3):
        self.Secret1 = Secret1
        self.Secret2 = Secret2
        self.Secret3 = Secret3

    # Reset method, resets the status back to 0
    def Reset(self):
        self.Status = 0
        self.Current = 0
        print("**RESET**")

    # TurnLeft method, substract the number of ticks to current status (ticks to the left)
    def TurnLeft(self, Ticks):
        self.Current = self.Current - Ticks
        if self.Current < 0:
            self.Current = 39 - self.Current
        print("Left ticks = " + str(Ticks) + " and current status = " + str(self.Current))
        
        # If 2nd number is correct, Status + 1
        if self.Status == 1 and self.Current == self.Secret2:
            self.Status = 2
        else:
            self.Status = 0

    # TurnRight method, adds the number of ticks to the current status (ticks to the right)
    def TurnRight(self, Ticks):
        self.Current = self.Current + Ticks
        if self.Current > 39:
            self.Current = self.Current - 39
        print("Right ticks = " + str(Ticks) + " and current status = " + str(self.Current))
        
        # If 1st number is correct, Status + 1
        if self.Status == 0 and self.Current == self.Secret1:
            self.Status = 1

        # If 3rd number is correct, Status + 1
        elif self.Status == 2 and self.Current == self.Secret3:
            self.Status = 3
        else:
            self.Status = 0

    # Open method, if Status = 3 then Status == 4 , the lock will open
    def Open(self):
        if self.Status == 3:
            self.Status = 4
            print("**OPEN**")
        else:
            self.Status = 0
            print("**LOCKED**")