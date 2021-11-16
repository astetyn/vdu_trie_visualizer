from turtle import circle, penup, pendown, forward,\
right, left, write, done, backward, pencolor, speed, goto, setup

RADIUS = 17
EDGE = 60
WIDTH = 1000
HEIGHT = 700


def draw_node(abs_angle, text):

    val, rest = split_node(text)
    
    circle_offset(1)
    
    circle(RADIUS)
    
    # value text
    left(90)
    penup()
    forward(RADIUS // 2)
    pendown()
    write(val, align='center', font=('Arial', 13, 'normal'))
    penup()
    backward(RADIUS // 2)
    right(90)
    pendown()
    
    right(-abs_angle)
    
    edges = get_edges(rest)
    angle = 180 / (len(edges) + 1)
    
    for i, e in enumerate(edges):
        
        e = e[1:len(e) - 1]
        e_parts = e.split(',', 1)
        
        right(angle)
        forward(EDGE // 2)
        pencolor('red')
        write(e_parts[0], align='center', font=('Arial', 15, 'normal'))
        pencolor('black')
        forward(EDGE // 2)
        
        penup()
        forward(RADIUS)
        pendown()
        
        left(angle)
        
        draw_node(angle * i, e_parts[1])
        
        right(angle)
        
        penup()
        backward(RADIUS)
        pendown()
        
        backward(EDGE)

    left(angle * len(edges))
    right(abs_angle)
    
    circle_offset(-1)

def split_node(text):
    parts = text.split(' ', 1)
    
    second = parts[1]
    
    val = ''
    rest = second[7:len(text)]
    
    if second[0] == '(':
        val = ''
        for c in second:
            if c == ')':
                break
            val += c
        rest = second[(len(val) + 2):len(second)]
        val = val[6:len(val)]
    
    return val, rest

def circle_offset(sign):
    penup()
    right(90)
    forward(RADIUS * sign)
    left(90)
    pendown()
    
def get_edges(text):
    
    text = text[1:len(text) - 1]

    edge_text = ''
    nest_count = 0
    
    result = []
    
    for c in text:
        
        edge_text += c
        
        if c == '(':
            nest_count += 1
        elif c == ')':
            nest_count -= 1
            if nest_count == 0:
                result.append(edge_text)
                edge_text = ''
        elif nest_count == 0:
            edge_text = ''
    
    return result

to_parse = input()
example = "TNode (Just 42) [('a',TNode (Just 16) []),('b',TNode Nothing [('b',TNode (Just 1) []),('c',TNode (Just 5) []),('e',TNode (Just 2) [])])]"

setup(width=WIDTH, height=HEIGHT)
penup()
goto(0, HEIGHT // 2 - RADIUS)
pendown()

speed(0)
draw_node(0, to_parse)
done()