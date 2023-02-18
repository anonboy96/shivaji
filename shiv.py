from sklearn.preprocessing import scale
from sketchpy import canvas

pen = canvas.sketch_from_svg('3.svg',scale = 230)

pen.draw()