# Assignment 1
For the first assignment it is required to write a python node that controls the robot to put all the golden boxes together. The code is found in this Git Repository (named as assignment.py) and flowchart is seen below.

## Installing and running
The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).
Use `run.py` to run the script in the simulator:
```bash
$ python2 run.py exercise1.py
```

## Flowchart for the code:
1.Main program <br>
![Main code](https://github.com/IrisLaanearu/Project/assets/145934148/46febfeb-dc51-43b3-9dd9-7ff3cd4010fc)

### Functions
2.Drive and turn <br>
![Drive and Turn](https://github.com/IrisLaanearu/Project/assets/145934148/825e101a-c4d2-47df-bd40-4a5d199912d9)

3.Find token <br>
![Find token](https://github.com/IrisLaanearu/Project/assets/145934148/fbb8632e-7bb7-48fe-a177-5d41a1065250)

4.Find center token <br>
![Find center token](https://github.com/IrisLaanearu/Project/assets/145934148/a2ed04a9-09f9-476a-b0f8-89d6435bb0e8)

5.Move token <br>
![Move token](https://github.com/IrisLaanearu/Project/assets/145934148/5ced616d-d684-4e95-9af7-51f84b9a7ead)

## Possible improvements
The code is built to find the first token and drive it to the center. This is done by manually inserting the trajectory from the first token to the center. It is not the best approach because the code does not work if the robot or the first token is positioned differently than in the current simulation. <br>
One solution is to not collect all the tokens in the center. After pairing the first tokens, it is possible to locate the next token by the previous one and collect them where the first token was found.

