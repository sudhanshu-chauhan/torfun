from stem.control import Controller

try:
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        bytes_read = controller.get_info("traffic/read")
        bytes_written = controller.get_info("traffic/written")
        print("bites written: {} bites read: {}".format(bytes_written, bytes_read))
except Exception as err:
    print("an error has occurred:")
    print(err)