from matplotlib import pyplot as plt

class VariabelPressure():
    
    def __init__(self):
        self.maximum = 0
        self.minimum = 0
    
    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)
    
    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)
    
class Speed(VariabelPressure):
    
    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 28
        self.p7 = 35
        self.p8 = 40
        self.p9 = 70
        self.pn = 80
        
    def verylow(self, x):
        #0-p1 = 1
        #p1-p2 = down
        if x < self.p1:
            return 1
        elif self.p1<= x <= self.p2:
            self.maximum = self.p1
            self.minimum = self.p2
            return self.down(x)
        else:
            return 0
    
    def low(self, x):
        #p1-p2 = up
        #p2-p4 = down
        if self.p1 <= x <= self.p2:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.up(x)
        elif self.p2 <= x <= self.p4:
            self.minimum = self.p2
            self.maximum = self.p4
            return self.down(x)
        else:
            return 0
    
    def medium(self, x):
        #p3-p5 = up
        #p5-p6 = 1
        #p6-p7 = down
        if self.p3 <= x <= self.p5:
            self.minimum = self.p3
            self.maximum = self.p5
            return self.up(x)
        elif self.p5 <= x <= self.p6:
            return 1
        elif self.p6 <= x <= self.p7:
            self.minimum = self.p6
            self.maximum = self.p7
            return self.down(x)
        else:
            return 0
    
    def high(self, x):
        #p6-p8 = up
        #p8-p9 = down
        if self.p6 <= x <= self.p8:
            self.minimum = self.p6
            self.maximum = self.p8
            return self.up(x)
        elif self.p8 <= x <= self.p9:
            self.minimum = self.p8
            self.maximum = self.p9
            return self.down(x)
        else:
            return 0
    
    def veryhigh(self, x):
        #p8-p9 = up
        #p9-.... = 1
        if x > self.p9:
            return 1
        elif self.p8 <= x <= self.p9:
            self.minimum = self.p8
            self.maximum = self.p9
            return self.up(x)
        else:
            return 0
        
    def graph(self, value=None):
        plt.figure(figsize=(15,5))
        #Vlow
        #0-p1 = 1 [1=>1]
        #p1-p2 = down [1=>0]
        #p2 - .... [0=>0]
        x_verylow = [0, self.p1, self.p2, self.pn]
        y_verylow = [1, 1, 0, 0]
        plt.plot(x_verylow, y_verylow, label='verylow')
        
        #low
        #0-p1 = 0 [0-0]
        #p1-p2 = up [0-1]
        #p2-p4 = down [1-0]
        #p4-pn = 0 [0-0]
        x_low = [0, self.p1, self.p2, self.p4, self.pn]
        y_low = [0, 0, 1, 0, 0]
        plt.plot(x_low, y_low, label='low')
        
        #medium
        #0-p3 = 0 [0-0]
        #p3-p5 = up [0-1]
        #p5-p6 = 1 [1-1]
        #p6-p7 = down [1-0]
        #p7-pn = 0 [0-0]
        x_medium = [0, self.p3, self.p5, self.p6, self.p7, self.pn]
        y_medium = [0, 0, 1, 1, 0, 0]
        plt.plot(x_medium, y_medium, label='medium')
        
        #high
        #0-p6 = 0 [0-0]
        #p6-p8 = up [0-1]
        #p8-p9 = down [1-0]
        #p9-pn = 0 [0-0]
        x_high = [0, self.p6, self.p8, self.p9, self.pn]
        y_high = [0, 0, 1, 0, 0]
        plt.plot(x_high, y_high, label='high')
        
        #veryhigh
        #0-p8 = 0 [0-0]
        #p8-p9 = up [0-1]
        #p9-.... = 1 [1-1]
        x_veryhigh = [0, self.p8, self.p9, self.pn]
        y_veryhigh = [0, 0, 1, 1]
        plt.plot(x_veryhigh, y_veryhigh, label='veryhigh')
        
        if value:
            x_param = [0, value, value]
            y_verylow = self.verylow(value)
            y_low = self.low(value)
            y_medium = self.medium(value)
            y_high = self.high(value)
            y_veryhigh = self.veryhigh(value)
            y_param_verylow = [y_verylow, y_verylow, 0] 
            y_param_low = [y_low, y_low, 0] 
            y_param_medium = [y_medium, y_medium, 0] 
            y_param_high = [y_high, y_high, 0] 
            y_param_veryhigh = [y_veryhigh, y_veryhigh, 0]
            plt.plot(x_param, y_param_verylow, label='verylow_value')
            plt.plot(x_param, y_param_low, label='low_value')
            plt.plot(x_param, y_param_medium, label='medium_value')
            plt.plot(x_param, y_param_high, label='high_value')
            plt.plot(x_param, y_param_veryhigh, label='veryhigh_value') 
            
        plt.legend(loc = 'upper left')
        plt.show()
        
speed = Speed()
x = 50
print('verylow', speed.verylow(x))
print('low', speed.low(x))
print('medium', speed.medium(x))
print('high', speed.high(x))
print('veryhigh', speed.veryhigh(x))
speed.graph(x)
