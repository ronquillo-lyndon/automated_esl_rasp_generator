from screeninfo import get_monitors

def _get_monitor_size():
    width = 0
    height = 0
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height

    return width, height