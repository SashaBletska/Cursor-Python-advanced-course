"""4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface."""


from abc import abstractmethod, ABC


class Laptop:
    @abstractmethod
    def screen(self):
        raise NotImplementedError('Subclasses are necessary to implement these abstract methods')

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError('Subclasses are necessary to implement these abstract methods')

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError('Subclasses are necessary to implement these abstract methods')

    @abstractmethod
    def webcam(self):
        raise NotImplementedError('Subclasses are necessary to implement these abstract methods')

    @abstractmethod
    def ports(self):
        raise NotImplementedError('Subclasses are necessary to implement these abstract methods')

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError('Subclasses are necessary to implement these abstract methods')


class HPLaptop(Laptop, ABC):
    def __init__(self, size_of_screen, backlight_of_keyboard, function_of_touchpad, pixels_of_webcam, quantity_of_ports,
                 power_of_dynamics):
        self.size_of_screen = size_of_screen
        self.backlight_of_keyboard = backlight_of_keyboard
        self.function_of_touchpad = function_of_touchpad
        self.pixels_of_webcam = pixels_of_webcam
        self.quantity_of_ports = quantity_of_ports
        self.power_of_dynamics = power_of_dynamics

    def screen_size(self):
        print(f'Size of screen: {self.size_of_screen}')

    def keyboard_color(self):
        print(f'Color of keyboards backlight: {self.backlight_of_keyboard}')

    def touchpad_function(self):
        print(f'Function of touchpad: {self.function_of_touchpad}')

    def webcam_pixels(self):
        print(f'Video resolution of web camera: up to {self.pixels_of_webcam} pixels')

    def ports_quantity(self):
        print(f'Quantity of ports: {self.quantity_of_ports}')

    def dynamics_power(self):
        print(f'Power of dynamics: {self.power_of_dynamics} W')


hp_1 = HPLaptop('15', 'red', 'zoom by 2 fingers', '1920 x 1080', 'USB-3, HDMI-1', '10')
hp_1.screen_size()
hp_1.keyboard_color()
hp_1.touchpad_function()
hp_1.webcam_pixels()
hp_1.ports_quantity()
hp_1.dynamics_power()
