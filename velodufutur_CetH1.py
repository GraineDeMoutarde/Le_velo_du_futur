import matplotlib.pyplot as plt
from numpy import *

#Définition des constantes
Lt=40.1
Lf=46.6
L=17
Ls=(Lt+Lf)*0.66
Lh = 10
Lc = 5

theta_s=-pi/24
theta_d=pi/12
theta_sh = pi/18
theta_pc = -pi/14

#à changer
def theta_h(theta_oc):
    return(0.6)
    #return arcsin((Lt**2-Lf**2-(Loh**2+Loc**2-2*Loh*Loc*cos(theta_oh-theta_oc)))/(2*Lf*sqrt(Loh**2+Loc**2-2*Loh*Loc*cos(theta_oh-theta_oc))))-arcsin((Loh*cos(theta_d-theta_oh)-Loc*cos(theta_d-theta_oc))/sqrt(Loh**2+Loc**2-2*Loh*Loc*cos(theta_oh-theta_oc)))

#à changer
def theta_g(theta_oc):
    return(0.6)
    #return arcsin((Lf**2-Lt**2-(Loh**2+Loc**2-2*Loh*Loc*cos(theta_oh-theta_oc)))/(2*Lt*sqrt(Loh**2+Loc**2-2*Loh*Loc*cos(theta_oh-theta_oc))))-arcsin((Loh*cos(theta_h(theta_oc)+theta_d-theta_oh)-L*cos(theta_h(theta_oc)+theta_d-theta_oc))/(sqrt(Loh**2+Loc**2-2*Loh*Loc*cos(theta_oh-theta_oc))))

line1, = plt.plot([],[])
line2, = plt.plot([],[])
line3, = plt.plot([],[])
line4, = plt.plot([],[])
line5, = plt.plot([],[])
line6, = plt.plot([],[])

def upd_seg(line, A,B):
    line.set_data([-A[1],-B[1]],[A[0],B[0]])

#tracé des segments fixes
O = [0,0]
S = [Ls * cos(theta_s), Ls * sin(theta_s)]
H = [S[0] + Lh*cos(theta_sh), S[1] + Lh*sin(theta_sh)]
upd_seg(line1, O,S)
upd_seg(line2, S,H)


n = 200 #nombre de pas de temps

for k in range(n):
    theta_p = k*2*pi/n
    theta_g1 = theta_g(theta_p)
    theta_h1 = theta_h(theta_p)

    #création des points mobiles
    G = [H[0]+Lt*cos(theta_h1+theta_d), H[0]+Lt*sin(theta_h1+theta_d)]
    P = [L*cos(theta_p), L*sin(theta_p)]
    C = [P[0] + Lc*cos(theta_pc), P[1] + Lc*sin(theta_pc)]

    #tracé des 4 segments mobiles
    upd_seg(line3, H, G)
    upd_seg(line4, G, C)
    upd_seg(line5, C, P)
    upd_seg(line6, P, O)

    #paramètres de tracé
    plt.xlim(-40,40)
    plt.ylim(-20,75)
    plt.gca().set_aspect('equal')
    plt.legend(['Loh','LH', 'LG','Loc'])
    plt.grid(True)
    plt.pause(0.01)

plt.show()


'''
checknormCG = []
checknormCG2=[]
TH=[]
TG=[]
check norm
TH.append(theta_h(theta_oc1))
TG.append(theta_g(theta_oc1))
checknormCG2.append(sqrt((G2[0]-C[0])**2+(G2[1]-C[1])**2))
'''
