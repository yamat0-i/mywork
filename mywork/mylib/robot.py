from mywork.mylib import console
from mywork.mylib import fiber_measure


class Robot():
    def __init__(self, name='Robot'):
        self.name = name

    def say_hello(self):
        print('Welcome!')

    def say_goodbye(self):
        print('See you!')

class Analyser(Robot):
    def __init__(self, name='Analyser'):
        self.name = name

    def menu(self):
        self.mode = None
        print('Select mode.')
        self.mode = input('> mode: ')  # Now 'fiber' or 'exit'

        if self.mode == 'fiber':
            self.get_data()
            fiber_measure.measure(self.date_dir_path, self.date)
        elif self.mode == 'exit':
            return
        
        self.menu()

    def get_data(self):
        self.date = None
        if not self.date:
            print('Please enter date.(yyyyMMdd)')
            self.date = input('> date: ')

        mode_dir_path = console.get_mode_dir_path(self.mode)
        self.date_dir_path = console.get_date_dir_path(mode_dir_path, self.date)
        