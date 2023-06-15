import tkinter

# local varibales

# Functions


def submit():
    global errors
    errors = []
    # check for empty
    if name_textbox.get() == "":
        errors.append("Fill the نام\n")
    if lastName_textbox.get() == "":
        errors.append("Fill the نام خانوادگی\n")
    if age_textbox.get() == "":
        errors.append("Fill the سن\n")
    if username_textbox.get() == "":
        errors.append("ّFill the یوزرنیم\n")
    if password_textbox.get() == "":
        errors.append("Fill the رمزعبور\n")

    if len(errors) == 0:
        sign_up(name_textbox.get(), lastName_textbox.get(),
                age_textbox.get(), username_textbox.get(), password_textbox.get())
    else:
        show_error(errors)


def show_error(errors: list):
    error_window = tkinter.Tk()
    error_window.title("ERROR!")
    error_window.geometry("200x200")
    text = ""
    for error in errors:
        text += error
    text_box = tkinter.Label(error_window, text=text)
    text_box.grid(row=0, column=0)
    error_window.mainloop()


def sign_up(name: str, lastname: str, age: str, username: str, password: str) -> None:
    try:
        index = calculate_index()
    except FileNotFoundError:
        index = 1

    # Clean all text boxes
    clean_textbox(name_textbox)
    clean_textbox(lastName_textbox)
    clean_textbox(age_textbox)
    clean_textbox(username_textbox)
    clean_textbox(password_textbox)
    user = f"User{index}:\n\tName: {name}\n\tLast Name: {lastname}\n\tAge: {age}\n\tUsername: {username}\n\tPassword: {password}\n"
    append_in_file(user)


def append_in_file(text: str) -> None:
    with open("users.txt", mode="a", encoding="utf8") as users_file:
        users_file.write(text)


def clean_textbox(textbox: tkinter.Entry) -> None:
    textbox.delete(0, tkinter.END)


def calculate_index() -> int:
    with open("users.txt", mode="r+", encoding="utf8") as file:
        text = file.readlines()
        return int((len(text)/6)+1)


def check_username(username: str) -> bool:
    with open("users.txt", mode="r", encoding="utf8") as users:
        text = users.readlines()
        if text[4].contains(username):
            return False


# Window
main_window = tkinter.Tk()
main_window.title("Sing Up")
main_window.geometry("400x400")

# name Row
name_label = tkinter.Label(main_window, text="نام")
name_label.grid(row=0, column=0)
name_textbox = tkinter.Entry(main_window, width=40)
name_textbox.grid(row=0, column=1)
# lastName Row
lastName_label = tkinter.Label(main_window, text="نام خانوادگی")
lastName_label.grid(row=1, column=0)
lastName_textbox = tkinter.Entry(main_window, width=40)
lastName_textbox.grid(row=1, column=1)
# age Row
age_label = tkinter.Label(main_window, text="سن")
age_label.grid(row=2, column=0)
age_textbox = tkinter.Entry(main_window, width=40)
age_textbox.grid(row=2, column=1)
# ّusername Row
username_label = tkinter.Label(main_window, text="نام کاربری")
username_label.grid(row=3, column=0)
username_textbox = tkinter.Entry(main_window, width=40)
username_textbox.grid(row=3, column=1)
# password Row
password_label = tkinter.Label(main_window, text="رمز عبور")
password_label.grid(row=4, column=0)
password_textbox = tkinter.Entry(main_window, width=40, show="*")
password_textbox.grid(row=4, column=1)
# submit button
submit_btn = tkinter.Button(
    main_window, text="ثبت نام", pady="10", padx="20", command=submit)
submit_btn.grid(row=5, column=1)


if __name__ == "__main__":
    main_window.mainloop()
