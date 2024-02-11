import pyinputplus as pyin

def input_matrix(row,col):

	matrix = []
	rows = []

	print("")

	for i in range(0,row):
		for j in range(0,col):
			
			rows.append(pyin.inputInt(prompt=f"Enter Element For Position m[{i}][{j}] : "))
			
		matrix.append(rows)
		rows = []

	return matrix

def main():

	print("-----------------------------")
	print("|     Matrix Operations     |")
	print("-----------------------------")

	while True:

		print("\n	     Main Menu		")

		print("\n1. Matrix Addition")
		print("0. Exit")
		
		choice = pyin.inputInt(prompt="\n_ : ",greaterThan=-1)

		match choice:

			case 1:
				print("\n\n----- Matrix Addition -----")

				print("\nFor Matrix 1 :-")
				m1_row_count = pyin.inputInt(prompt="\nEnter No Of Rows : ",greaterThan=0)
				m1_col_count = pyin.inputInt(prompt="\nEnter No Of Columns : ",greaterThan=0)

				print("\nFor Matrix 2 :-")
				m2_row_count = pyin.inputInt(prompt="\nEnter No Of Rows : ",greaterThan=0)
				m2_col_count = pyin.inputInt(prompt="\nEnter No Of Columns : ",greaterThan=0)

				if (m1_col_count+m1_row_count) != (m2_col_count+m2_row_count):
					print("\nBoth Matrix's Orders Are Not Same , Addition Is Not Possible")

				else:

					print("\nFor Matrix 1 :-")
					matrix1 = input_matrix(m1_row_count,m1_col_count)
					print("\nFor Matrix 2 :-")
					matrix2 = input_matrix(m1_row_count,m1_col_count)

			case 0:
				print("\nProgram Exited")
				break

if __name__ == "__main__":

	main()