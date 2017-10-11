Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t #turtle을 t라고 할 것이다.
>>> n=50 #n을 50으로 지정
>>> t.bgcolor("black") #배경색을 검은색으로 지정
>>> t.color("red") #펜 색을 빨간색으로 지정
>>> t.pensize(3) #펜 사이즈를 3으로 지정
>>> t.speed(0) # 거북이 속도를 가장 빠르게 지정
>>> for x in range(n): #n번 반복
	t.circle(50) #반지름이 50인 원을 그린다.
	t.left(200/n) #거북이가 200/n만큼 왼쪽으로 회전

	
>>> 
