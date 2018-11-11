# KidsCoding

this is a simple implement for teaching kids learning Python step by step from scratch.
also included a [kc](https://github.com/ximitiejiang/KidsCoding/tree/master/kc) coding lib to draw lines/ for fun, which can be used to replace the **turtle**, which is always as slow as turtle.

### [lesson_1](https://github.com/ximitiejiang/KidsCoding/blob/master/lesson_1.py)

### [lesson_2](https://github.com/ximitiejiang/KidsCoding/blob/master/lesson_2.py)

### [lesson_3](https://github.com/ximitiejiang/KidsCoding/blob/master/lesson_3.py)

### [lesson_4](https://github.com/ximitiejiang/KidsCoding/blob/master/lesson_4.py)

### [lesson_5](https://github.com/ximitiejiang/KidsCoding/blob/master/lesson_5_draw.py)

### [lesson_6](https://github.com/ximitiejiang/KidsCoding/blob/master/lesson_6.py)

![kids works](https://github.com/ximitiejiang/KidsCoding/blob/master/kc/imgs/robot.png)
![kids works](https://github.com/ximitiejiang/KidsCoding/blob/master/kc/imgs/star.png)
### How to use kc package

import class from kc package, create object paper, draw, and ant.
when you create draw and ant, you should tell them where they can run,
so paper object should transfer to them, then you can use the object to draw.
```
from .kc.tool import PAPER, DRAW, ANT
paper = PAPER(size=[m,n])
draw = DRAW(paper)
ant = ANT(paper)
```
a [demo](https://github.com/ximitiejiang/KidsCoding/blob/master/kc/demo.py) here can be a good start to learn to use it.

Happy Coding! 