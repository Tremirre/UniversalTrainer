# HuaweiTrainer
## Basics
Simple application for training to the HCIA exam.
Currently compatible with python 3.8.x and higher. 
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
  
4. TEST with custom size: <br><br>
  User can specify the length of the test by providing the desired (positive) number of questions after the flag. <br>
  In case user inputs the size larger then the pool of questions, the size will be automatically adjusted to fit. <br>
  Example command for test with 10 questions:
  >py main.py -test 10

## Exit
Currently the only way of quiting the app amid running is to press Ctrl+C on your keyboard.
