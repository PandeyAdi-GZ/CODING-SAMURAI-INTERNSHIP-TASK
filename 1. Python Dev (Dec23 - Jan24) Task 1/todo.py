import os


def add():
	task = input("Enter your task: ")

	f = open("todo.txt", "r")
	fnum = int(f.readline().strip("\n"))
	# print(fnum)
	fl = f.readlines()
	# print(fl)
	fnum += 1
	f.close()

	f = open("temp.txt", "w")
	f.write(f"{fnum}\n")
	fl.append(f"[{fnum}, '{task}', {0}]\n")
	# print(fl)
	f.writelines(fl)
	f.close()

	os.remove("todo.txt")
	os.rename("temp.txt", "todo.txt")

	print("New task added successfully.")


def view():
	f = open("todo.txt", "r")
	fl = f.read().split("\n")[1:-1]
	fl = list(map(lambda x: eval(x), fl))
	fl1 = list(filter(lambda x: x[2] == 0, fl))
	fl2 = list(filter(lambda x: x[2] == 1, fl))
	if fl1:
		print("Unfinished Tasks: ")
		for x in fl1:
			print(f"{x[0]}. {x[1]}")
	if fl2:
		print("Finished Tasks: ")
		for x in fl2:
			print(f"{x[0]}. {x[1]}")
	f.close()


def markDone():
	task = input("Which task do you want to want to mark as done: ")
	while not task.isdigit():
		task = input("Enter a valid task number: ")
	task = int(task)
	# print(task)

	f = open("todo.txt", "r")
	fnum = f.readline()
	fl = f.readlines()
	f.close()
	fl = list(map(lambda x: eval(x), fl))

	found = 0
	done = 0
	for i in range(len(fl)):
		if task == fl[i][0]:
			found = 1
			if fl[i][2] == 1:
				done = 1
				print("Task is already completed.")
			else:
				fl[i][2] = 1
			break

	if found == 1:
		f = open("temp.txt", "w")
		f.write(f"{fnum}")
		for i in range(len(fl)):
			fl[i] = str(fl[i]) + "\n"
			f.write(fl[i])
		f.close()
		os.remove("todo.txt")
		os.rename("temp.txt", "todo.txt")
		if done == 0:
			print("Task marked as done.")
	else:
		print("Task not found.")


def delete():
	task = input("Which task do you want to delete: ")
	while not task.isdigit():
		task = input("Enter a valid task number: ")
	task = int(task)

	f = open("todo.txt", "r")
	fnum = f.readline()
	fl = f.readlines()
	f.close()
	fl = list(map(lambda x: eval(x), fl))

	found = 0
	ind = 0
	for i in range(len(fl)):
		if task == fl[i][0]:
			found = 1
			ind = i
			break

	if found == 1:
		for i in range(ind+1, len(fl)):
			fl[i][0] -= 1
		fnum = str(int(fnum) - 1) + "\n"
		f = open("temp.txt", "w")
		f.write(f"{fnum}")
		for i in range(len(fl)):
			if i != ind:
				fl[i] = str(fl[i]) + "\n"
				f.write(fl[i])
		f.close()
		os.remove("todo.txt")
		os.rename("temp.txt", "todo.txt")
		print("Task deleted.")
	else:
		print("Task not found.")


try:
	f = open("todo.txt", "r")
	x = f.read()
	f.close()
	if x == "":
		f = open("todo.txt", "w")
		f.write("0\n")
		f.close()

except FileNotFoundError:
	# print("The file was not found. Creating a new file.")
	f = open("todo.txt", "w")
	f.write("0\n")
	f.close()


def main():
	print("----------------------------------------------")
	print("----------------------------------------------")
	print("1. Add Task")
	print("2. View All Tasks")
	print("3. Mark as Done")
	print("4. Delete Task")
	print("Else => Quit")

	tasks = input("Enter your choice: ")
	while not tasks.isdigit():
		tasks = input("Enter a valid choice: ")
	tasks = int(tasks)

	print("----------------------------------------------")
	print("----------------------------------------------")

	# tasks = 2

	if tasks == 1:
		add()
	elif tasks == 2:
		view()
	elif tasks == 3:
		markDone()
	elif tasks == 4:
		delete()
	else:
		quit()


if __name__ == "__main__":
	while True:
		main()
