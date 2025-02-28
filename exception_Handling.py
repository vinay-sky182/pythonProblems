class A:

    def method_one(self):

      print("Starting of the program");

      try:
        print("Enter a Number: ", end='');
        num = int(input());
        a = 10 / num;

      except Exception as e: 
        print(f"An exception occurred: {e}");

      else:
        print("Inside else block");  

      finally:
        print("Inside finally block");  

      print("Ending of the program");  

obj = A();
obj.method_one();      