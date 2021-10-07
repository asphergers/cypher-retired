from tkinter import *
import random
from datetime import *
import time
root = Tk()
root.geometry("435x480")
root.title("Cypher")
frame = Frame(root)
large_font = ("Verdana", 20)
medium_font = ("Verdana", 15)
mediumlarge_font = ("Verdana", 18)

acceptable_chars = [9, 10] + list(range(32, 127))

acceptable_chars_two = [410, 412] + list(range(32, 127))

result = ""
message = ""
result_string = ""

characters_in_order = [chr(x) for x in acceptable_chars]





def clear_res():
	result_string.delete("1.0", "end")



def clear():
	msg.delete(0, "end")



def standard_seed():
	todays_date = str(date.today())
	li = list(todays_date.split("-"))
	test_list = [int(i) for i in li]

	dt = datetime(test_list[0], test_list[1], test_list[2])
	timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
	standard = random.seed(timestamp)
	standard = timestamp + (random.randint(10, 10000000000) * random.random())

	return standard



def decrypt():
	result = ""
	r_seed = cypher_key.get()
	message = msg.get()

	if r_seed != "":
		try:
			r_seed = float(r_seed)
		except:
			emergency = Label(root, text = "PLEASE INPUT AN INTEGER", font = medium_font, foreground = "red")
			emergency.place(x = 70, y = 235)
			emergency.after(1000, emergency.destroy)

		else:
			random.seed(r_seed)
			shuffled_list = [chr(x) for x in acceptable_chars_two]
			random.shuffle(shuffled_list)


			for i in range(0, len(message)):
				result += characters_in_order[shuffled_list.index(message[i])]

			encrypt_result_window_decrypt(result)
	elif r_seed == "":
		r_seed = int(standard_seed())
		random.seed(r_seed)
		shuffled_list = [chr(x) for x in acceptable_chars_two]
		random.shuffle(shuffled_list)


		for i in range(0, len(message)):
			result += characters_in_order[shuffled_list.index(message[i])]

		encrypt_result_window_decrypt(result)



def encrypt():
	result = ""
	message = msg.get()
	r_seed = cypher_key.get()
	
	if r_seed != "":
		try:
			r_seed = float(r_seed)

		except:

			emergency = Label(root, text = "PLEASE INPUT AN INTEGER", font = medium_font, foreground = "red")
			emergency.place(x = 70, y = 235)
			emergency.after(1000, emergency.destroy)

		else:
			random.seed(r_seed)
			shuffled_list = [chr(x) for x in acceptable_chars_two]
			random.shuffle(shuffled_list)

			for i in range(0, len(message)):
				result += shuffled_list[characters_in_order.index(message[i])]

			encrypt_result_window_encrypt(result)
	elif r_seed == "":
		r_seed = int(standard_seed())

		random.seed(r_seed)
		shuffled_list = [chr(x) for x in acceptable_chars_two]
		random.shuffle(shuffled_list)

		for i in range(0, len(message)):
			result += shuffled_list[characters_in_order.index(message[i])]

		encrypt_result_window_encrypt(result)



def encrypt_result_window_decrypt(result):

	global result_string

	result_string = Text(root, height = 8, width = 35, wrap = WORD, foreground = "green")
	result_string.place(x = 72, y = 280)

	result_string.insert(1.0, (result)) 

	return result_string



def encrypt_result_window_encrypt(result):

	global result_string

	result_string = Text(root, height = 8, width = 35, foreground = "blue")
	result_string.place(x = 72, y = 280)

	result_string.insert(1.0, result) 

	return result_string


			




label1 = Label(root, text = "Message to be encoded/unencoded:", font = medium_font)
label1.place(x = 40, y = 15)

msg = Entry(root, font = medium_font)
msg.place(x = 80, y = 50)

encrypt_decrypt = Label(root, text = "Cypher key below: ", font = medium_font)
encrypt_decrypt.place(x = 110, y = 90)

cypher_key = Entry(root, font = medium_font, justify = CENTER, show = "*")
cypher_key.place(x = 80, y = 125)

encrypt_message = Button(root, text = "ENC-A", command = encrypt, font = mediumlarge_font, foreground = "blue", activebackground = "blue", activeforeground = "white")
encrypt_message.place(x = 70, y = 175)

clear_button = Button(root, text = "CLR", command = clear, font = mediumlarge_font, foreground = "red", activebackground = "red", activeforeground = "white")
clear_button.place(x = 175, y = 175)

decrypt_message = Button(root, text = "DEC-B", command = decrypt, font = mediumlarge_font, foreground = "green", activebackground = "green", activeforeground = "white")
decrypt_message.place(x = 250, y = 175)

text_clear = Button(root, text = "CLEAR RESULT", command = clear_res, font = mediumlarge_font, foreground = "red", activebackground = "red", activeforeground = "white")
text_clear.place(x = 105, y = 420)





root.mainloop()