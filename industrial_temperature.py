def trigger_alarm(temperatures, threshold=80):
    return [sensor for sensor, temp in temperatures.items() if temp > threshold]