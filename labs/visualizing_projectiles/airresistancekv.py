from vpython import *

ACCEL = vector(0, -9.81, 0)
DT = 0.1
V_TERM = 10
MASS = 0.5

def get_k(m, v_term):
    '''
    Calculate K
    
    ma = mg - kv
    lim t -> infty
    
    0 = mg - kv_term
    
    mg/v_term = k
    '''
    
    return m * ACCEL.y / v_term
    
'''
Program an object that drops in air with air resistance, using an F=-kv force.  Include a v-t graph.
'''

K = get_k(MASS, V_TERM)

ball = sphere(radius=10, pos=vector(0,100,0), color=color.blue)
vt_graph = graph(title="v vs t", xtitle="t", ytitle="v")
vt_curve = gcurve(color=color.blue)

t = 0
v_current = vector(0, 0, 0)
p_future = M * v_current 

while ball.pos.y >= 0:
    vt_curve.plot(t, v_current.y)
    p_future += (MASS * ACCEL - K * v_current) * DT
    
    v_current = p_future / MASS
    ball.pos.y += (v_current.y) * DT
    t += DT
    print(ball.pos.y)

    rate(100)
