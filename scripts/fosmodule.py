#Written by Caleb C. in 2022 for Carthage Space Sciences | WSGC | NASA
#Module to contain classes for mpg-foss.
import struct

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class bsymbols:
    info = '\U00002139'

def title():
    print(f"{bcolors.OKGREEN}                                ____               {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}   ____ ___  ____  ____ _      / __/___  __________{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}  / __ `__ \/ __ \/ __ `/_____/ /_/ __ \/ ___/ ___/{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN} / / / / / / /_/ / /_/ /_____/ __/ /_/ (__  |__  ) {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}/_/ /_/ /_/ .___/\__, /     /_/  \____/____/____/  {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}         /_/    /____/                             {bcolors.ENDC}")

class GatorPacket:
    class header:
        def __init__(self):
            self._len = 16
            self._data: bytearray

        @property
        def len(self):
            return self._len

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data: bytearray):
            if not isinstance(data, bytearray):
                raise TypeError("Data input must be a bytearray.")
            self._data = data

        def get_payload_len(self):
            decode = self._data[0:4]
            result, = struct.unpack('>I', decode)
            return int(result) #Size in bytes?

        def get_timestamp(self):
            decode = self._data[4:8]
            result, = struct.unpack('>I', decode)
            return int(result) #Time since epoch

        def get_packet_num(self):
            decode = self._data[8:10]
            result, = struct.unpack('>H', decode)
            return int(result) #This packet number

        def get_gator_type(self):
            decode = self._data[10]
            decode = decode.to_bytes(1, byteorder='big')
            result, = struct.unpack('>B', decode)
            return int(result) #The type of gator connected

        def get_version(self):
            decode = self._data[11]
            decode = decode.to_bytes(1, byteorder='big')
            result, = struct.unpack('>B', decode)
            return int(result) #Gator firmware version
        
        def get_characters(self):
            status = False
            characters = [12, 13, 14, 15]
            yoho = "ohoy"
            sync_str = ""
            for character in characters:
                char = chr(self._data[character])
                sync_str += char
            if yoho == sync_str:
                status = True
            return status
  

    class Status:
        def __init__(self):
            self._len = 3
            self._data: bytearray
        
        @property
        def len(self):
            return self._len

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data: bytearray):
            if not isinstance(data, bytearray):
                raise TypeError("Data input must be a bytearray.")
            self._data = data

        def get_num_found(self):
            decode = self._data[17:20]
            result, = struct.unpack('>c', decode)
            return int(result) 

    class data: 

        def __init__(self):
            self._len = 23
            self._data: bytearray

        @property
        def len(self):
            return self._len

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data: bytearray):
            if not isinstance(data, bytearray):
                raise TypeError("Data input must be a bytearray.")
            self._data = data

        def access_bit(self, data, num):
            base = int(num // 8)
            shift = int(num % 8)
            return (data[base] >> shift) & 0x1

        def get_cog_data(self): 
            decode = self._data[20:44]
            as_string = bytes(decode)
            print(as_string)
            bytes_as_bits = [self.access_bit(decode, i) for i in range (len(decode)*8)]
            print(bytes_as_bits)
            print("Length: ", len(bytes_as_bits))
            cog_length = len(decode)/23
            
            sensor_1 = bytes_as_bits[0:19]
            sensor_2 = bytes_as_bits[19:38]
            sensor_3 = bytes_as_bits[38:57]
            sensor_4 = bytes_as_bits[57:76]
            sensor_5 = bytes_as_bits[76:95]
            sensor_6 = bytes_as_bits[95:114]
            sensor_7 = bytes_as_bits[114:133]
            sensor_8 = bytes_as_bits[133:152]
            sensor_9 = bytes_as_bits[152:171]
            all_sensors = [sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6, sensor_7, sensor_8, sensor_9]
            print("\nSensor 1:", sensor_1, "Length:", len(sensor_1), "\nSensor 2:", sensor_2, "Length:", len(sensor_2), "\nSensor 3:", sensor_3, "Length:", len(sensor_3), "\nSensor 4:", sensor_4, "Length:", len(sensor_5), "\nSensor 5:", sensor_5, "Length:", len(sensor_5), "\nSensor 6:", sensor_6, "Length:", len(sensor_6),"\nSensor 7:", sensor_7, "Length:", len(sensor_7), "\nSensor 8:", sensor_8, "Length:", len(sensor_8), "\nSensor 9:", sensor_9, "Length:", len(sensor_9),)
            return all_sensors
    

        




class zen:
    zen = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!"]
