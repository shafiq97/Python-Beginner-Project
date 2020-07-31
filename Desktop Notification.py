from win10toast import ToastNotifier

if __name__ == '__main__':
    toaster = ToastNotifier()
    toaster.show_toast("Hello!!", "Sour Candy", None, 4, False)
