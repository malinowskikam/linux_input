import traceback
import struct
import const

device = "/dev/input/event25"


def main():
    try:
        print("Opening device file")
        with open(device, "rb") as d:
            while True:
                event_bytes = d.read(const.INPUT_EVENT_SIZE)
                timestamp, millis, ev_type, ev_code, ev_value = struct.unpack(const.INPUT_EVENT_FORMAT,event_bytes)
                if ev_type == const.EV_ABS and ev_code == const.ABS_RZ:
                    print(f"{ev_type} {ev_code} {ev_value}")
    except KeyboardInterrupt:
        print("Exitting")
        return
    except Exception as e:
        traceback.print_exc()

if __name__ == "__main__":
    main()