# ev82etiq
This is a simple python package that once supplied image root, it resizes it.
Two kinds of resize are possible: you can resize and maintain the aspect ration of 
image, or you can resize to a square shape


## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/MuthumbiAlex/ev82etiq
```

## Usage
Features:
* function.py ---- main function that takes in 3 inputs:
  * x : 		location of image
  * height: 	what will be the height after resizing
  * ratio: 		do you want to maintain aspect ratio or not


* if code is run as ipynb, you can use interact to choose a slider on size of image (toy example provided), and dropbox with ratio choice

#### Demo of some of the features:
```python
import toolbox
from toolbox import report

message = toolbox.functions.weirdCase("The toolbox package is ready for use")
report(message)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for chunk in toolbox.functions.listChunker(lst=list_of_numbers, dsize=3):
    print(chunk)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)