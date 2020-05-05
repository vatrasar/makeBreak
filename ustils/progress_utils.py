import time

def get_progress(start_time,time_for_interval ):
    time_form_last_break=get_time_from_last_break(start_time)
    progress=time_form_last_break/time_for_interval
    progress*=100 #hange for procentage values
    if(progress>100):
        return 100
    else:
        return progress

def get_time_from_last_break(start_time):
    return time.time() - start_time
