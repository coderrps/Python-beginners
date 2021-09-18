#inheritance
from chef import Chef
from chinesechef import Chinesechef

myChef = Chef()
# myChef.make_chicken()
# myChef.make_special_dish()
# myChef.make_salad()

myChinesechef = Chinesechef()
myChinesechef.make_special_dish()
myChinesechef.make_fried_rice()
#after inheritance
myChef.make_chicken()
myChef.make_special_dish()
myChef.make_salad()