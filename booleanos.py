'''
Este programa evalua expresiones booleanas con los simbolos de conjuncion &, disyuncion |, implicacion => y negacion ^.
La implementacion se realizo por medio de un AST o arbol sintactico abstracto que se forma de acuerdo a las precedencias 
de las operaciones y permite tanto realizar las operaciones como parentizar.
Tambien se crearon dos funciones llamadas evaluarPreorder y evaluarPostorder que aunque no se utilizan en el programa principal
tambien son capaces de calcular las operaciones de la expresion, pero no hacen uso del AST que se crea con ayuda de una clase Arbol.
'''
#La funcion verificarEntrada verifica si la entrada del usuario contiene las palabras PRE o POST
def verificarEntrada(separacion):
	if (separacion[1].find("PRE")== -1) and (separacion[1].find("POST") == -1):
		return False
	else:
		return True
#La funcion operar realiza las operaciones indicadas en la expresion booleana. Los parametros se pasan a esta funcion
#mientras se descubren al visitar el arbol. Se verifica si el string es true, True, false o False y se modifica por un
#valor booleano para poder calcular su valor de acuerdo a la operacion deseada, que se pasa como string.	
def operar(izq, der, op):
	#conjunción: Representada por el símbolo &.
	#disyunción: Representada por el símbolo |.
	#implicación: Representada por el símbolo =>.
	#negación: Representada por el símbolo ˆ.
	if izq.find("true")!=-1 or izq.find("True")!=-1:
		izq = True
	elif izq.find("false")!=-1 or izq.find("False")!=-1:
		izq = False
	if der.find("true")!=-1 or der.find("True")!=-1:
		der = True
	elif der.find("false")!=-1 or der.find("False")!=-1:
		der = False
	resultado = False
	if op == "&":
		resultado = bool(izq) and bool(der)
	elif op == "|":
		resultado = bool(izq) or bool(der)
	elif op == "=>":
		resultado = (not bool(izq)) or bool(der)
	elif op == "^" or op == "ˆ":
		resultado = not bool(izq)
	return str(resultado)

'''La funcion evaluarPreorder utiliza un algoritmo que itera sobre el string para poder evaluar 
su valor. Esta funcion itera sobre el string y al conseguir un operando lo guarda en una pila, si 
consigue un operador, saca dos operandos de la pila en caso de que el operador sea binario y los opera, luego
aloja nuevamente el valor obtenido en la pila para ir acumulando los valores y al culminar el ciclo se tiene
un unico valor en la lista operandos que es el valor deseado de la expresion.
'''
def evaluarPreorder(expresion):
	operadores = ["&","|","=>","^","ˆ"]
	operandos = []
	for x in range(len(expresion)-1,-1,-1):
		if expresion[x] not in operadores:
			operandos = [expresion[x]]+operandos
		elif expresion[x] in operadores:
			if expresion[x] == "^" or expresion[x] == "ˆ":
				izquierda = operandos.pop(0)
				resultado = operar(izquierda,"",expresion[x])
				operandos = [resultado] + operandos
			else:
				derecha = operandos.pop(0)
				izquierda = operandos.pop(0)
				resultado = operar(izquierda,derecha,expresion[x])
				operandos = [resultado] + operandos	
		else:
			continue
	cambio = (lambda x: "true" if (x=="True") else "false")
	print(cambio(operandos[0]))	
	return cambio(operandos[0])

'''La funcion evaluarPostorder utiliza un algoritmo que itera sobre el string para poder evaluar 
su valor. Esta funcion itera sobre el string y al conseguir un operando lo guarda en una pila, si 
consigue un operador, saca dos operandos de la pila en caso de que el operador sea binario y los opera, luego
aloja nuevamente el valor obtenido en la pila para ir acumulando los valores y al culminar el ciclo se tiene
un unico valor en la lista operandos que es el valor deseado de la expresion. Solo se diferencia de evaluarPreorder
ya que visita al string de izquierda a derecha, mientras que evaluarPreorder lo hace de derecha a izquierda, debido
a la diferencia en las notaciones que se desean evaluar.
'''
def evaluarPostorder(expresion):
	operadores = ["&","|","=>","^","ˆ"]
	operandos = []
	for x in range(0,len(expresion)):
		if expresion[x] not in operadores:
			operandos = [expresion[x]] + operandos
		elif expresion[x] in operadores:
			if expresion[x] == "^" or expresion[x] == "ˆ":
				izquierda = operandos.pop(0)
				resultado = operar(izquierda,"",expresion[x])
				operandos = [resultado] + operandos
			else:
				derecha = operandos.pop(0)
				izquierda = operandos.pop(0)
				resultado = operar(izquierda,derecha,expresion[x])
				operandos = [resultado] + operandos	
		else:
			continue
	cambio = (lambda x: "true" if (x=="True") else "false")
	print(cambio(operandos[0]))
	return cambio(operandos[0])
	
'''La clase Arbol es la clase que se utilizara para crear el AST que evaluara y parentizara en modo infijo las expresiones dadas.
Esta clase solo contiene 3 atributos: nodo, izquierdo y derecho. En caso de que un nodo no tenga hijos, izquierdo y derecho se colocan
como None.
'''
class Arbol:
	def __init__(self, valor, izquierdo, derecho):
		self.nodo = valor
		self.izquierdo = izquierdo
		self.derecho = derecho
	def __str__(self):
		if self.izquierdo != None:
			print("El hijo izquierdo de "+self.nodo)
			self.izquierdo.__str__()
		if self.derecho != None:
			print("El hijo derecho de "+self.nodo)
			self.derecho.__str__()

#En el diccionario precedencias se alojan las precedencias de cada uno de los operadores de las expresiones
precedencias = {"^":3,"ˆ":3,"|":2,"&":2,"=>":1,"true":0,"false":0}

'''La funcion visitarArbol se encarga de visitar el AST para retornar su version infija parentizada, es por esto que se consideran
diversos casos de precedencias, que ayudan a colocar los parentesis de manera adecuada.
'''
def visitarArbol(arbol):
	if arbol.izquierdo == None and arbol.derecho == None:
		return arbol.nodo
	if arbol.izquierdo != None and arbol.derecho != None:
		if (arbol.nodo == "=>"):
			return "("+visitarArbol(arbol.izquierdo)+arbol.nodo+visitarArbol(arbol.derecho)+")"
		if (precedencias[arbol.nodo] > precedencias[arbol.izquierdo.nodo] and precedencias[arbol.nodo] > precedencias[arbol.derecho.nodo]):
			return visitarArbol(arbol.izquierdo)+arbol.nodo+visitarArbol(arbol.derecho)
		if (precedencias[arbol.nodo] == precedencias[arbol.izquierdo.nodo]) and (precedencias[arbol.nodo] == precedencias[arbol.derecho.nodo]):
			return "("+visitarArbol(arbol.izquierdo)+")"+arbol.nodo+"("+visitarArbol(arbol.derecho)+")"
		if (precedencias[arbol.izquierdo.nodo]>precedencias[arbol.nodo]) and (precedencias[arbol.derecho.nodo]>precedencias[arbol.nodo]):
			return "("+visitarArbol(arbol.izquierdo)+")"+arbol.nodo+"("+visitarArbol(arbol.derecho)+")"
		if (precedencias[arbol.izquierdo.nodo]>precedencias[arbol.nodo]):
			return "("+visitarArbol(arbol.izquierdo)+")"+arbol.nodo+visitarArbol(arbol.derecho)
		if (precedencias[arbol.derecho.nodo]>precedencias[arbol.nodo]):
			return visitarArbol(arbol.izquierdo)+arbol.nodo+"("+visitarArbol(arbol.derecho)+")"
		else:
			return visitarArbol(arbol.izquierdo)+arbol.nodo+visitarArbol(arbol.derecho)
	if arbol.izquierdo != None:
		return arbol.nodo+visitarArbol(arbol.izquierdo)

'''La funcion evaluarArbol de manera similar a la funcion visitarArbol toma un arbol y los visita, pero en lugar de incluirle los 
parentesis, busca hasta los ultimos nodos que tengan hijos para efectuar las operaciones que alli se encuentran, luego retorna este 
valor y realiza cada una de las operaciones a modo de "backtracking" para obtener los valores de las expresiones.
'''
def evaluarArbol(arbol):
	if arbol.izquierdo != None and arbol.izquierdo.izquierdo == None:
		return operar(arbol.izquierdo.nodo,arbol.derecho.nodo,arbol.nodo)
	if arbol.izquierdo != None and arbol.derecho != None:
		if arbol.izquierdo.izquierdo != None and arbol.derecho.izquierdo != None:
			evaluarArbol(arbol.izquierdo)
			evaluarArbol(arbol.derecho)
	if arbol.izquierdo != None:
		return operar(arbol.izquierdo.nodo,"",arbol.nodo)

'''La funcion evaluarArbolPostorder utiliza un algoritmo muy similar a las funciones de evaluarPostorder y evaluarPreorder
pero en este caso se aprovecha de una lista para alojar los arboles de cada uno de los nodos que va consiguiendo, si al evaluar
la expresion, es un operando se crea un nodo sin hijos, si es un operador, se toman los dos ultimos nodos sin hijos de la lista
y se agregar como hijos del operando, luego se ingresa el arbol del operando de nuevo a la lista y asi progresivamente, hasta
que se haya termina de leer la expresion. Finalmente, se llama a la funcion evaluarArbol una vez se tiene el arbol.
La expresion se lee de izquierda a derecha, ya que se trata de una expresion postfija
'''
def evaluarArbolPostorder(expresion):
	operadores = ["&","|","=>","^","ˆ"]
	operandosArboles = []
	for x in range(0,len(expresion)):
		if expresion[x] not in operadores:
			operandosArboles = [Arbol(expresion[x],None,None)] + operandosArboles
		elif expresion[x] in operadores:
			if expresion[x] == "^" or expresion[x] == "ˆ":
				hijoIzquierdo = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,None)] + operandosArboles
			else:
				hijoDerecho = operandosArboles.pop(0)
				hijoIzquierdo = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,hijoDerecho)] + operandosArboles
		else:
			continue
	return evaluarArbol(operandosArboles[0])

'''La funcion evaluarArbolPostorder utiliza un algoritmo muy similar a las funciones de evaluarPostorder y evaluarPreorder
pero en este caso se aprovecha de una lista para alojar los arboles de cada uno de los nodos que va consiguiendo, si al evaluar
la expresion, es un operando se crea un nodo sin hijos, si es un operador, se toman los dos ultimos nodos sin hijos de la lista
y se agregar como hijos del operando, luego se ingresa el arbol del operando de nuevo a la lista y asi progresivamente, hasta
que se haya termina de leer la expresion. Finalmente, se llama a la funcion evaluarArbol una vez se tiene el arbol.
La expresion se lee de derecha a izquierda, ya que se trata de una expresion prefija
'''
def evaluarArbolPreorder(expresion):
	operadores = ["&","|","=>","^","ˆ"]
	operandosArboles = []
	for x in range(len(expresion)-1,-1,-1):
		if expresion[x] not in operadores:
			operandosArboles = [Arbol(expresion[x],None,None)]+operandosArboles
		elif expresion[x] in operadores:
			if expresion[x] == "^" or expresion[x] == "ˆ":
				hijoIzquierdo = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,None)] + operandosArboles
			else:
				hijoIzquierdo = operandosArboles.pop(0)
				hijoDerecho = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,hijoDerecho)] + operandosArboles	
		else:
			continue
	return evaluarArbol(operandosArboles[0])

'''La funcion mostrarPostorder utiliza un algoritmo muy similar a las funciones de evaluarPostorder y evaluarPreorder
pero en este caso se aprovecha de una lista para alojar los arboles de cada uno de los nodos que va consiguiendo, si al evaluar
la expresion, es un operando se crea un nodo sin hijos, si es un operador, se toman los dos ultimos nodos sin hijos de la lista
y se agregar como hijos del operando, luego se ingresa el arbol del operando de nuevo a la lista y asi progresivamente, hasta
que se haya termina de leer la expresion. Finalmente, se llama a la funcion visitarArbol una vez se tiene el arbol.
La expresion se lee de izquierda a derecha, ya que se trata de una expresion postfija
'''
def mostrarPostorder(expresion):
	operadores = ["&","|","=>","^","ˆ"]
	operandosArboles = []
	for x in range(0,len(expresion)):
		if expresion[x] not in operadores:
			operandosArboles = [Arbol(expresion[x],None,None)] + operandosArboles
		elif expresion[x] in operadores:
			if expresion[x] == "^" or expresion[x] == "ˆ":
				hijoIzquierdo = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,None)] + operandosArboles
			else:
				hijoDerecho = operandosArboles.pop(0)
				hijoIzquierdo = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,hijoDerecho)] + operandosArboles
		else:
			continue
	print(visitarArbol(operandosArboles[0]))
	
'''La funcion mostrarPreorder utiliza un algoritmo muy similar a las funciones de evaluarPostorder y evaluarPreorder
pero en este caso se aprovecha de una lista para alojar los arboles de cada uno de los nodos que va consiguiendo, si al evaluar
la expresion, es un operando se crea un nodo sin hijos, si es un operador, se toman los dos ultimos nodos sin hijos de la lista
y se agregar como hijos del operando, luego se ingresa el arbol del operando de nuevo a la lista y asi progresivamente, hasta
que se haya termina de leer la expresion. Finalmente, se llama a la funcion visitarArbol una vez se tiene el arbol.
La expresion se lee de derecha a izquierda, ya que se trata de una expresion prefija
'''
def mostrarPreorder(expresion):
	operadores = ["&","|","=>","^","ˆ"]
	operandosArboles = []
	for x in range(len(expresion)-1,-1,-1):
		if expresion[x] not in operadores:
			operandosArboles = [Arbol(expresion[x],None,None)]+operandosArboles
		elif expresion[x] in operadores:
			if expresion[x] == "^" or expresion[x] == "ˆ":
				hijoIzquierdo = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,None)] + operandosArboles
			else:
				hijoIzquierdo = operandosArboles.pop(0)
				hijoDerecho = operandosArboles.pop(0)
				operandosArboles = [Arbol(expresion[x],hijoIzquierdo,hijoDerecho)] + operandosArboles	
		else:
			continue
	print(visitarArbol(operandosArboles[0]))

'''La funcion mostrar recibe una lista que contiene si la expresion es prefija o postfija y muestra la expresion de acuerdo a esto.
Llamando a las funciones mostrarPreorder o mostrarPostorder
'''
def mostrar(ordenExpresion):
	orden = ordenExpresion.pop(0)
	if orden == "PRE":
		mostrarPreorder(ordenExpresion)
	else:
		mostrarPostorder(ordenExpresion)

'''La funcion evaluar recibe una lista que contiene si la expresion es prefija o postfija y evalua la expresion de acuerdo a esto.
Llama a las funciones evaluarArbolPreorder o evaluarArbolPostorder y antes de imprimir su resultado, mapea con una funcion lambda 
sus resultados a strings con true o false.
'''
def evaluar(ordenExpresion):
	orden = ordenExpresion.pop(0)
	cambio = (lambda x: "true" if (x=="True") else "false")
	if orden == "PRE":
		print(cambio(evaluarArbolPreorder(ordenExpresion)))
	else:
		print(cambio(evaluarArbolPostorder(ordenExpresion)))
	
'''La funcion main maneja las entradas del usuario y llama a las demas funciones del programa. Aparecera el simbolo ":" que indica que
ya se puede introducir una entrada desde la consola.
'''
def main():
	funciona = True
	while funciona:
		entrada = str(input(":"))
		e1 = entrada.find("EVAL")
		e2 = entrada.find("MOSTRAR")
		e3 = entrada.find("SALIR")
		if e1 == 0:
			separacion = entrada.split(" ")
			if verificarEntrada(separacion) == False:
				print("La entrada no es valida")
			else:
				separacion.pop(0)
				evaluar(separacion)
		elif e2 == 0:
			separacion1 = entrada.split(" ")
			if verificarEntrada(separacion1) == False:
				print("La entrada no es valida")
			else:
				separacion1.pop(0)
				mostrar(separacion1)
		elif e3 == 0 and len(entrada):
			funciona = False
		if e1 != 0 and e2 != 0 and e3 != 0:
			print("La entrada no es valida")
			
main()
