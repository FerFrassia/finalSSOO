import random

preguntas = {
	"Procesos": ["¿Qué es y para qué sirve una System Call? Explicar los pasos involucrados por hardware y software. Ejemplificar", "Una PCB clásica para el manejo de procesos contiene todos los recursos para que el proceso pueda ejecutar, por ejemplo Registros, Archivos abiertos, etc. ¿Cómo debe modificarse para soportar threads?", "¿Qué son las funciones reentrantes y cuál es su relación con los threads?", "Describa como funciona la lectura de un archivo desde un proceso de usuario indicando las llamadas al sistema, sus parámetros y los controles que se hacen. Relacione el concepto de monitor de usuario (2022)", "Que ve un proceso en unix? Con esto terminamos hablando de DAC en unix y de setuid (2022)"],
	"Sincronización": ["Cuál es la diferencia entre spin lock y semaforos? (2022)"],
	"Memoria": ["Describa de qué manera el Sistema Operativo protege el espacio de memoria de un proceso", "¿Que es Thrashing y como se puede solucionar sin agregar hardware?"],
	"Scheduling": ["¿Qué es el problema de inversión de prioridades y qué schedulers afecta?"],
	"Seguridad": ["¿Para qué sirve setuid y cuales son sus riesgos?", "Explicar DAC y comparar DAC en unix y windows.", "Describa como implementaría un sistema de autenticación utilizando la clave pública - privada. El mecanismo propuesto ¿Es más seguro que un sistema de autenticación con contraseña? Justifique. (2022)", "Es mejor un sistema con contraseñas o con clave pública y clave privada y por qué? (2022)"],
	"Filesystems": ["¿Qué es el superbloque en ext2 y que pasa si se pierde su información?", "¿Cuál es la diferencia a nivel de operaciones, de cuando se hace ls y ls -l?", "En un FS ext2, el sistema de archivo detecta en el arranque que el FS puede estar en estado inconsistente ¿Qúe información utiliza para determinarlo y dónde se encuentra? (2022)", "Usando dibujos y pocas palabras, ilustre las diferencias entre hard-link y soft-link. Luego, indique la principal limitación del hard-link. (2022)", "Cuál es la diferencia entre hard link y symbolic link? (2022)", "Si se corta la luz en un fs (ext2 o ext3) cómo se da cuenta cuando vuelvo a prender la máquina de que hubo un problema y después como resolverlo? (2022)", "Ventajas de los contenedores? (2022)"],
	"E/S": ["¿Cuáles son las 2 grandes diferencias a nivel de administración de E/S qu ehace el sistema operativo entre los discos mangnéticos (HDD) y los discos de estado sólido (SSD)? (2022)"],
	"Sistemas Distribuidos": ["Problema sobre un algoritmo de commit distribuido", "¿Cúal de las siguientes afirmaciones es verdadera sobre el protocolo de lamport para la sincronización de relojes en sistemas distribuidos? a-. El procotolo de Lamport utiliza un reloj centralizado para sincronizar los relojes de los nodos del sistema. b-. El protocolo de Lamport utiliza un algoritmo de elección de lider para elegir un nodo maestro que sincroniza los relojes de los demás nodos. c-. El protocolo de Lamport utiliza un algoritmo basado en el intercambio de mensajes entre nodos para sincronizar los relojes de forma descentralizada.  (2022)", "¿Cómo se relacionan los conceptos de consistencia, disponibilidad y tolerancia a fallos, en un sistema distribuido? (2022)", "Cómo mantener consistencia en fs distribuido? (2022)", "Diferencia entre raid 4 y raid 5? (2022)"]
}

def tomarFinal():
	categorias = list(preguntas.keys())
	print("Comencemos ;)")
	while(len(categorias) != 0):
		categoria = random.choice(categorias)
		categorias.remove(categoria)

		var = input("")
		print("Categoría: " + str(categoria))

		preguntasDeEstaCategoria = preguntas[categoria]
		while(len(preguntasDeEstaCategoria) != 0):
			pregunta = random.choice(preguntasDeEstaCategoria)
			preguntasDeEstaCategoria.remove(pregunta)
			var = input("")
			print(pregunta)

tomarFinal()