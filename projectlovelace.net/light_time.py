def light_time(distance):
    speed_of_light= 299792458  # Speed of light [m/s]

    time= 0
    time=distance/speed_of_light   

    # Calculate the time taken using t = d/c and return it.

    return "time taken {:.6f} m/s".format(time)
print(light_time(376291900))



