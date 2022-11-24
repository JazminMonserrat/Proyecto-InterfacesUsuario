import signal
import resource
import os




def tiempo_excedido(num_signal, frame_signal):
  raise SystemExit('Se ha excdendido el tiempo límite')

def establecer_tiempo_limite(segundos):
  _, hard = resource.getrlimit(resource.RLIMIT_CPU)
  resource.setrlimit(resource.RLIMIT_CPU, (segundos, hard))
  signal.signal(signal.SIGXCPU, tiempo_excedido)

def main():
  establecer_tiempo_limite(7)
  while True:
    pass


if _name__ == "_main_":
  main()