try:
    a = int(input("Enter the number: "))
    c = 1/a
except Exception as e:
    print(e)
    exit()
finally:
    print("Done")
print("Thank you!")
