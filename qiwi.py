

def generate_qiwi_link(pid,phone,amont,comment,currency):
	link = f'https://qiwi.com/payment/form/{pid}?extra%5B%27account%27%5D={phone}&amountInteger={amont}&amountFraction=0&extra%5B%27comment%27%5D={comment}&currency={currency}'
	return link
print(generate_qiwi_link(99,380989870157,2,'test',643))




