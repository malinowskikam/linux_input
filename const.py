import struct

# input-event-codes.h
# https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/input-event-codes.h
EV_KEY = 1
EV_ABS = 3

BTN_SOUTH = 304 # Cross
BTN_EAST = 305 # Circle
BTN_WEST = 308 # Square
BTN_NORTH = 307 # Triangle

BTN_TL = 310 # L1
BTN_TR = 311 # R1
BTN_TL2 = 312 # L2 button
BTN_TR2 = 313 # R2 button

ABS_X = 0 # LX
ABS_Y = 1 # LY
ABS_Z = 2 # L2 axis

ABS_RX = 3 # RX
ABS_RY = 4 # RY
ABS_RZ = 5 # R2 axis

# input.h
# https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/input.h
# https://docs.python.org/3/library/struct.html#format-characters
INPUT_EVENT_FORMAT = "qqHHi"
INPUT_EVENT_SIZE = struct.calcsize(INPUT_EVENT_FORMAT)