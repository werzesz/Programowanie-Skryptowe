argumentySuma = [[4,5]]
argumentyRoznica =[[4,5,6]]

def argumenty(y):
    def inner(func):
      def wrapper(*args, **kwargs):
        x = y[-1]

        list1 = list(args[1:]

        for i in range(len(x)):
            list1.append(x[i])

        for i in range (len(list1)-1,-1,-1):
            try:
              func(*list1, **kwargs)
              break

            except:
              del list1[i]

      return wrapper
    return inner

class Operacje:

  def __setitem__(self, k=None, v=None):
    if k =='roznica':
      argumentyRoznica.append(v)
    elif k == 'suma':
      argumentySuma.append(v)

  @argumenty(argumentySuma)
  def suma(a,b,c):
    print ("%d+%d+%d=%d" % (a,b,c,a+b+c))

  @argumenty(argumentyRoznica)
  def roznica(x,y):
    print ("%d-%d=%d" % (x,y,x-y))
