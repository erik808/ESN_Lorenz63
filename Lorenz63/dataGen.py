import numpy as np

class DataGen():

    def __init__(self, dataPoints):
        """
        Class constructor.
        dataPoints: number of data points
        """
        self.dataPoints = dataPoints

    def createLorenz63(self, dt, init):
        """
        Create Lorenz '63 data.
        dt:   timestep size
        init: initial value (x,y,z)
        """
        
        Nu = 3

        # Lorenz '63 parameters
        rho   = 28
        sigma = 10
        beta  = 8/3
        
        oldStates = np.zeros((self.dataPoints, Nu))
        newStates = np.zeros((self.dataPoints, Nu))
        
        oldStates[0, :] = init
        x = init[0]
        y = init[1]
        z = init[2]        
        for n in range(self.dataPoints):
            oldStates[n,:] = [x,y,z]

            x = x + dt*sigma*(y - x)
            y = y + dt*(x*(rho - z) - y)
            z = z + dt*(x*y - beta*z)        

            newStates[n,:] = [x,y,z]           

        return oldStates, newStates
    
