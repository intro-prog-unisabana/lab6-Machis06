def trigger_alarm(temperatures, threshold=80):
    alarms = []

    for sensor in temperatures:
        if temperatures[sensor] > threshold:
            alarms.append(sensor)

    return alarms