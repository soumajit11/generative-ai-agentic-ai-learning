device_staus = "active"
temperature = 38

if device_staus == "active":
    if temperature > 35:
        print("High Temperature Alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")