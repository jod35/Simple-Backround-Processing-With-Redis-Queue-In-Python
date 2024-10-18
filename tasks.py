import time
from datetime import datetime


def execute_after(seconds: int) -> bool:
    print("This will execute after {} seconds.".format(seconds))
    start_time = datetime.now()

    print("Started at {}".format(start_time))
    
    time.sleep(seconds)
    end_time = datetime.now()
    print("Finished at {}".format(end_time))
    
    print("Finished successfully")
    return True



