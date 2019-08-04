
class Say ( ):
    def say_hello (self,a):
        print( "hello" , a )

    def say_goodbye (self,name):
        print( "goodbye" ,name )

if __name__ == '__main__':
    s =Say()
    s.say_goodbye("大白菜")