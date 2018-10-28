import collections

Customer 	= collections.namedtuple('Customer', 	['cust_id', 'cust_prefs' , 'cust_prefs_count'])

customers = []

for row_id in range(5):
	cust_prefs={row_id: 'G', row_id+1: 'M', row_id+2: 'G'}

	customers.append(
		Customer(cust_id="cust_" + str(row_id+1), cust_prefs=cust_prefs, cust_prefs_count=row_id)
		)

# customers.sort(key=lambda cust: cust.cust_prefs_count)
print("--------")
print("namedtuple almacenado:")
print(customers)
print("--------")
print('acceso a namedtuple')
for cust in customers:
    print(" ",cust.cust_id, ';', cust.cust_prefs, ';', cust.cust_prefs_count)
print("--------")