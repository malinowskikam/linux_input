# Linux input

Repo for learning to access raw input from Linux kernel input subsystem with python and C

# Event devices

To access input sybsystem files user needs to be a part of ``input`` group

### Device File

```
/dev/input/eventX
```

### Device Metadata

```
sys/class/input/eventX/device/
```

# Event struct

The ``input_event`` struct is as follows:

```C
// input.h
// https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/input.h
struct input_event {
	struct timeval time;
	__u16 type;
	__u16 code;
	__s32 value;
};
```

On a 64 bit system this struct should be 24 bytes long (to confirm run sizes.c).
In python3 this struct can be represented with ``qqHHi`` format ([docs](https://docs.python.org/3/library/struct.html#format-characters))