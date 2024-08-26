class Timer:
    
    def __init__(self, duration, function, *args, **kwargs):
        self.duration = duration
        self.time_elapsed = 0
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.running = False    
        
    def start(self):
        self.running = True       
        
    def stop(self):
        self.running = False    
    
    def reset(self):
        self.time_elapsed = 0
    
    def update(self, dt):
        if self.running:
            self.time_elapsed += dt * 3600
            if self.time_elapsed >= self.duration:
                self.function(*self.args, **self.kwargs)
                self.reset()        
                
            
        
        