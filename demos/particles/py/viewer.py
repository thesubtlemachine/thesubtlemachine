# viewer.py

from vispy import scene

class Viewer:
    def __init__(self, simulation_module):
        self.sim = simulation_module

        self.canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=False)
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'arcball' #'turntable'
        self.scatter = scene.visuals.Markers()
        self.view.add(self.scatter)
        self.lines = scene.visuals.Line()
        self.view.add(self.lines)

        # Delay update until after first draw
        self.canvas.events.draw.connect(self.on_first_draw)

    def on_first_draw(self, event):
        self.update()
        # Only run once: disconnect after first call
        self.canvas.events.draw.disconnect(self.on_first_draw)

    first = True

    def update(self):
        pos = self.sim.get_positions()
        self.scatter.set_data(pos, edge_color=None, face_color=(1, 0.5, 0, 1), size=5)
        self.lines.set_data(pos=pos, width=2)



