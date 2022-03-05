import Sofa
import numpy as np


class Controller(Sofa.Core.Controller):
    def __init__(self, MO):
        super().__init__()
        self.MO = MO

    def onAnimateBeginEvent(self, _):
        print("\n\nonAnimateBeginEvent")
        random_disp = np.random.normal(0, 1e-2, self.MO.position.value.shape)
        self.MO.position.value = self.MO.rest_position.value + random_disp
        print(f"{random_disp[0]=}")
        print(f"{self.MO.position.value[0]=}")

    def onAnimateEndEvent(self, _):
        print("onAnimateEndEvent")
        print(f"{self.MO.position.value[0]=}")


def createScene(root):
    root.addObject('RequiredPlugin', pluginName=['BugPosition'])
    root.addObject("MechanicalObject", name="MO", template="Vec3d", position=[1, 0, 0])
    root.addObject("TestComponent", position="@MO.position")
    root.addObject(Controller(root.MO))


if __name__ == '__main__':
    import SofaRuntime
    import Sofa.Gui
    from sys import argv
    from os import path

    current_dir = path.dirname(path.abspath(__file__))

    SofaRuntime.PluginRepository.addFirstPath(path.join(current_dir, 'build'))

    root = Sofa.Core.Node("root")
    createScene(root)
    Sofa.Simulation.init(root)

    if len(argv) == 2 and argv[1] == 'gui':
        Sofa.Gui.GUIManager.Init("myscene", "qglviewer")
        Sofa.Gui.GUIManager.createGUI(root, __file__)
        Sofa.Gui.GUIManager.SetDimension(1080, 1080)
        Sofa.Gui.GUIManager.MainLoop(root)
        Sofa.Gui.GUIManager.closeGUI()
    else:
        Sofa.Simulation.animate(root, 0.01)