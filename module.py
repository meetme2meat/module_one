
import time
import platform

def main():
	print(platform.system())
	print("this is a module.py {}".format(time.time()))


if __name__ == "__main__":
	main()

