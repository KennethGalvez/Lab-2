from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend

width = 100
height = 100

rend = Renderer(width, height)

rend.dirLight = V3(1,0,0)

rend.active_texture = Texture("models/model.bmp")
rend.active_shader = toon
rend.glLoadModel("models/female.obj",
                 translate = V3(-3, 0, 0),
                 scale = V3(0.01,0.01,0.01),
                 rotate = V3(0,0,0))

rend.glFinish("output.bmp")
