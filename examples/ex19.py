"""
Initializers in case of inheritance
"""


class Camera:
    def __init__(self, **kwargs):
        self.resolution = kwargs.get('resolution', '50MP')

    def print_info(self):
        print(f'Resolution= {self.resolution}')


class Phone:
    def __init__(self, **kwargs):
        self.type = kwargs.get('type', 'mobile')

    def print_info(self):
        print(f'Type   = {self.type}')


class SmartPhone(Phone, Camera):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Camera.__init__(self, **kwargs)
        self.memory = kwargs.get('memory', '128 GB')

    def print_info(self):
        super().print_info()
        Camera.print_info(self)
        print(f'Memory = {self.memory}')


def main():
    sp = SmartPhone(resolution='25MP', memory='64GB')
    sp.print_info()


if __name__ == '__main__':
    main()

