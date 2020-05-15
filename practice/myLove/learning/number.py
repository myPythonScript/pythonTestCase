def odd_num():
	i = 1
	while i<=100:
		if (i+1) % 2 == 0:
			print("i=%d"%i)
		i+=1

def even_num():
	i = 1
	while i <= 100:
		if i%2 == 0:
			print("i=%d" % i)
		i += 1
print("100以内的奇数如下：")
odd_num()
print("100以内的奇数如下：")
even_num()
