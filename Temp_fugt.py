# Dette er et eksemple på brugen at Thingspeak
#import thingspeak
import time
import thingspeak
import random


channel_id = 1144539  # PUT CHANNEL ID HERE
write_key = '9OHDJI8WKYA9VBE1'# PUT YOUR WRITE KEY HERE
read_key = '8G4EYHZ4M6U5TNDK' # PUT YOUR READ KEY HERE


def measure(channel):
    try:

        humidity=random.randrange(30,100)
        temperature=random.randrange(-30,100)
        print("Fugt:",humidity)
        print("Temp:",temperature)
        response = channel.update({'field1': temperature, 'field2': humidity})
        #response = channel.update({'field2': humidity})
        read = channel.get({})
        print(read)

    except:
        print("connection failed")


if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)

