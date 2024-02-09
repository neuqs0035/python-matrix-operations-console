import pyinputplus as pyin

def main():

	print("-----------------------------")
	print("|     Matrix Operations     |")
	print("-----------------------------")

	while True:

		print("\n	     Main Menu		")

		choice = pyin.inputMenu(["Matrix Addition","Exit"],prompt="\nChoose Option\n\n",numbered=True)
		
		match choice:

			case 1:
				print("\n		Matrix Addition")
			case 2:
				print("\nProgram Exited")
				break

if __name__ == "__main__":

	main()