# HuaweiTrainer
## Basics
Simple application for training to the HCIA exam

It provides a comfy interface to get well acquainted with course exam questions.

To run the program it is you should start the console in the project directory and run main.py file with python by using command:
> py main.py

## Modes
Currently the app supports three modes:
1. LIST:<br><br>
  Lists all questions in the csv file along with the possible and the correct answers.
  Call this mode with <i>-list</i> flag
  > py main.py -list
  
2. TRAIN:<br><br>
  It asks the user randomly-ordered questions one by one and gives immediate feedback to the user's chosen answer. This mode is being run by default.
  Call this mode with <i>-train</i> flag, or without any
  > py main.py -train
  
3. TEST:<br><br>
  It asks the user randomly-chosen questions one by one, without giving immediate feedback. It asks by default 20 questions.
  At the end of the test the user is provided with obtained score.
  Call this mode with <i>-test</i> flag
  > py main.py -test
