#Importar matplotlib
import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()#Obtener las variables de plt, figura y coordenadas
  ax.bar(labels, values) #Se pasa valores para la barra
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels) #se deben indicar si o si los labels
  ax.axis('equal')#Organice en centro y forma de circulo
  plt.savefig('pie2.png')
  plt.close()


if __name__ == '__main__':
  labels = ['a','b','c']
  values = [10,40,100]
  #generate_bar_char(labels, values)
  generate_pie_chart(labels,values)