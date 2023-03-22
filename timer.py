import arcade


class Timer:
    """A class representing a Timer. To be used for scheduling events to occur after x seconds"""

    def set_timer(self, dur:float, interval:float=1) -> dict:
        """Sets the timer to countdown until 0
        
        Args:
            dur (float): The duration of the timer
            interval (float): How often to countdown
            
        Returns:
            A dictionary that will be updated once the timer is finished."""
        self.res = {
            "DURATION": dur,
            "FINISHED": False
            }
        
        arcade.schedule(self.count, interval)
        return self.res
        
    def count(self, dt):
        """Acts as the timer and counts down.
        
        Args:
            dt (float): Delta time nigga"""
        self.res['DURATION'] -= dt
        if self.res['DURATION'] <= 0:
            self.res['FINISHED'] = True
            arcade.unschedule(self.count)
    
            