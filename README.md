# BugPosition

To reproduce, let's define SOFA root path and add it to 
python's search paths. 

```bash
export SOFA_ROOT=/opt/sofa
export PYTHONPATH=$PYTHONPATH:$SOFA_ROOT/plugins/SofaPython3/lib/python3/site-packages
```
Then, compile and launch the scene
```bash
git clone git@github.com:jnbrunet/BugPosition.git
cmake -DCMAKE_PREFIX_PATH=$SOFA_ROOT/lib/cmake -S BugPosition -B BugPosition/build -DCMAKE_BUILD_TYPE=Release
cmake --build BugPosition/build
python3 BugPosition/scene.py
 ```

The result should be something like:
```commandline
(...)
onAnimateBeginEvent
random_disp[0]=array([-0.01092411, -0.00742505, -0.01442109])
self.MO.position.value[0]=array([1., 0., 0.])
onAnimateEndEvent
self.MO.position.value[0]=array([1., 0., 0.])
```

We can see that the random displacement was not taken into account.

Starting the same scene with the GUI yield the good results:
```commandline
python3 BugPosition/scene.py gui
(...)
onAnimateBeginEvent
random_disp[0]=array([-0.00746889, -0.01065234,  0.00446683])
self.MO.position.value[0]=array([ 0.99253111, -0.01065234,  0.00446683])
onAnimateEndEvent
self.MO.position.value[0]=array([ 0.99253111, -0.01065234,  0.00446683])
```