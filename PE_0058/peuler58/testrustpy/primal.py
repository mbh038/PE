from ctypes import cdll
lib = cdll.LoadLibrary('is_prime.dll')

is_prime = lib.is_prime