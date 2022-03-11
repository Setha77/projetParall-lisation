
class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None

list_obj = []

def ajouter(self):
    print('Entrez nom')
    name=input()
    print('Entrez le nombre de valeur ecrites')
a=input()
n=int(a)
writes = []
for i in range(n):
    print('Entrez valeur ecrite')
    x=input()
    writes.append(x)


print('Entrez le nombre de valeur lues')
n=int(input())
reads = []
for i in range(n):
    print('Entrez valeur lue')
    x=input()
    reads.append(x)

print('Entrez le nom de run')
run=input()
  
self = Task(name, writes, reads, run)
list_obj.append(self)
print(list_obj)

ajouter(self)
    
#def ajouterV2(t):
#    list_obj.append(t)


'''
    
class Tasksystem:
def getDependecies(nomTache):

def run():    

X = None
Y = None
Z = None
def runT1():
    global X
    X = 1

def runT2():
    global Y
    Y = 2
def runTsomme():
    global X, Y, Z
    Z = X + Y

t1 = Task("t1", ["X"], runT1)

'''