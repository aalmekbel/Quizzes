def sum_inbox(math, lang):
	inbox = 25

	if math<5 and lang<5:
		inbox -=30

	if math == 10 and lang == 10:
		inbox += 30

	if math>7 and lang>8:
		inbox +=10

	if math>=5 and lang>7:
		inbox +=5

	if math<5 or lang<5:
		inbox -=10
	return inbox


print sum_inbox(8,9)
print sum_inbox(5,8)
print sum_inbox(10,10)
print sum_inbox(4,3)
print sum_inbox(8,4)
print sum_inbox(4,4)