import math

def asg_vec(p,vec):
  alv = {}
  td=0
  for i in sorted(p):
    mind = math.inf
    clv = ""
    pc = p[i]
    
    for v in vec:
      if vec[v] =="":
        veh_c= vec[v + "_coordinates"]
        dis = cal_dis(pc,veh_c)
        if dis <mind or (dis == mind and v<clv):
          mind = dis
          clv = v
    alv[i] =clv
    vec[clv] = i
    td +=mind
  return td

def cal_dis(p1,p2):
  return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

x,y = map(int,input().split())
p ={}
v= {}

def inp():
  l,m,n = input().split()
  return l,m,n

for _ in range(x):
  nam,a,b = inp()
  p[nam] = (int(a), int(b))

for _ in range(y):
  vec,a,b = inp()
  v[vec] = ""
  v[vec+ "_coordinates"] = (int(a),int(b))

mid = asg_vec(p,v)
print(mid,end ="")

