seats = {(r,c):0 for r,e in enumerate(open("text.txt","rt").read().splitlines())
                 for c,s in enumerate(e) if s=='L'} # (r,c)->0|1 for Empty/Occupied
NR = max(rc[0] for rc in seats.keys())+1
NC = max(rc[1] for rc in seats.keys())+1; NN = max(NR,NC)

def adj1(rc,seats):
  return sum(seats.get((rc[0]+dr,rc[1]+dc),0) for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)

def adj2(rc,seats,o=0):
  for dr,dc in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
    for k in range(1,NN):
      ar=rc[0]+k*dr; ac=rc[1]+k*dc
      if ar<0 or ar>=NR or ac<0 or ac>=NC: break
      if (ar,ac) in seats: o+=seats[(ar,ac)]; break
  return o

def step(seats,adj,limit):
  return {rc:int(adj(rc,seats)<limit) if s else int(adj(rc,seats)==0) for rc,s in seats.items()}

def solve(seats,adj,limit):
  while (new:=step(seats,adj,limit)) != seats: seats=new
  return sum(seats.values())

print(solve(seats,adj1,4))
print(solve(seats,adj2,5))