from mywork.mylib import robot


def controller():
    analyser = robot.Analyser()
    analyser.say_hello()
    analyser.menu()
    analyser.say_goodbye()
