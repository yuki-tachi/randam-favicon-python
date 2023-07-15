import PySimpleGUI as sg
import cairosvg
from draw_svg import Drawable, Rect, Circle, Triangle, get_draw_svg, create_svg
import generate_pattern
import os

left_layout = [
    [sg.Text('Division:'), sg.Input(5, key='-DIV-', change_submits=True)],
    [sg.Text('Shape:'), sg.Combo(['Rect', 'Circle', 'Triangle'], default_value='Rect', key='-SHAPE-', readonly=True, change_submits=True)],
    [sg.Text('Fill:'), sg.Input("#B30F3A", key='-FILL-', change_submits=True)],
    [sg.Text('Pattern:'), sg.Ok("Change Pattern",key='-PATTERN-')],
]
right_layout = [
    [sg.Column([
        [sg.Image(key='-FAVICON-', filename='favicon.png') if os.path.isfile('favicon.png') else sg.Image(key='-FAVICON-', filename='')]
    ], justification='center')]
]

leftFrame = sg.Frame('setting', left_layout, size=(200, 250), vertical_alignment="top")
rightFrame = sg.Frame('result', right_layout, size=(200,200), vertical_alignment="center")

layout = [
    [
        leftFrame, rightFrame
    ],
    [
        sg.Exit()
    ]
]

window = sg.Window('CampsiteAvailabilityChecker', layout, resizable=True)
favi = window.find_element('-FAVICON-')


shape_dic = {
    'Rect': Rect,
    'Circle': Circle,
    'Triangle':Triangle
}
shpae: Drawable = shape_dic['Rect']()
shpae.set_size(5)
pattern = generate_pattern.execute(5)

# svgを更新して、pngとして書き出して表示(PySimpleGUIでは直接svgを表示できないため)
def update_favicon():
    create_svg(get_draw_svg(shpae, pattern))
    cairosvg.svg2png(url="favicon.svg", write_to="favicon.png")
    favi.update(filename='favicon.png')

while True:
    event, values = window.read()
    # print(event, values)

    if event in (sg.WIN_CLOSED, 'Exit'):
        print("Exit")
        break

    if event == '-DIV-':
        div_count = values['-DIV-']
        if(div_count == ""):
            continue
        div_count = int(div_count)
        print(div_count)

        pattern = generate_pattern.execute(div_count)
        shpae.set_size(div_count)

        update_favicon()
        continue

    if event == '-SHAPE-':
        shpae: Drawable = shape_dic[values['-SHAPE-']]()
        shpae.set_size(int(values['-DIV-']))

        update_favicon()
        continue

    if event == '-FILL-':
        shpae.fill = values['-FILL-']

        update_favicon()
        continue
    if event == '-PATTERN-':
        pattern = generate_pattern.execute(int(values['-DIV-']))
        
        update_favicon()
        continue

window.close()