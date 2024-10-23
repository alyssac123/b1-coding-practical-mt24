class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp # Proportional gain of the controller
        self.kd = kd # Derivate gain of the controller
        self.previous_error = 0 # Creating a variable to store the error from the previous time step

    def control_action(self, reference: float, current_depth: float) -> float:
        """ 
        Compute the control action using the PD controller formula.
        r[t] is the reference/desired depth for each x-position
        y[t] is the current actual depth of the UUV
        u[t] is the control action generated 
        """
        error = reference - current_depth # Calculating e[t]
        derivative = error - self.previous_error # e[t] - e[t-1]

        # Now implementing the PD control equation:
        control = (self.kp*error) + (self.kp*derivative)

        # Update previous error for next iteration 
        self.previous_error = error

        return control 








