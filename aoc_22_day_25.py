blob = """21==112=11=100-
1--0=-=22-
2121
10112
1=0=00
1=0-01-000--=122-
2111-
10-=-=2=0=-2
1=0112==2
2-2=1
210
11-111
12=2=221--00-1
1=--2-0001--=1=
10001==0001212-
12=1
11=1-=0=
1=10000102-2=
2=--221-1-00
2-10=-1-=1---2=222
1-=21022=-00=2
120=-221=2--=121
1=---00==-2020=0201
1=0=
200-=21=0---1=22
1=10-12=2-12
11210==0-=0-120
2--22=0-0=-12=1
1=-000
1=2--20=1
111---1=1-12=-=
1=-=2=1100-12==
2110=0===11-1=
10=1
1=-0
1-===102--0=1-1210-0
2010-2=1--=01--
210-11===-12
1=-2111=--1200
100
1=21--==-=-210102=
2-2=211--01
1--22=-
1121
1222=100-12002==-
1=20=1=-11112=2021
1102=0-11212
2=--==-002
2-=0=-=-
2-220--
122=02
1=012---2=0
1--=--21
1-=01202=-1
22=02
1=---2=-2202
1-==-
122-2=1-02
111-0-0120-10210
201
210=-0-==110201-11=
21
22110-2==0-0
11210=00=1-0=-022
1120==
2=--=2-011=
1--2-2--0-010=1-
1=--021-==--=102=
11=210=
2=001201
21==-0=21
1=00=
1-1
10--10000-=212--
10211
10=1=12201-112-
1=01=
122-1
202-=1222
22-111
122010-0=22121=-=-
102
1-001=0==222=2
2-0=1-1-1--
2---20=22=11212
1=0=11-2212-==-1
2=011-
1-1-01012-
21=22===-
22=20--=2=2=--021-
1===0==
2=12222100
2=
11-1==20=0-20
22120-1-11--
2-
1==1--2-==2=211
212-2=2212===-1-=-
10=
200=201=
1=21=
1==
11210=02102----2
2=-11==2121-100=-
11=-=0==
120=2==
1-1=102--2-=-=02=0
102=-1
1==202202221102=
100=12=
11-=1-12020-2=1=
10==02200=
1====02
1=-
101==2=-=-=01-=0
1-1=-1022121=-0
2212====
11=02=02===1=222-12
112=12----12
202=-1--0020
1=20-1=02000
1-
11=20120=
112==120-
22
1-1-11--2020
11="""

rows = blob.split("\n")

def snafu_to_decimal(snum):
	# SNAFU number to decimal number
	result = 0
	decimal = {"2":2,"1":1,"0":0,"-":-1,"=":-2}
	for e, k in enumerate(reversed(snum)):
		result += decimal[k]*(5**e)
	return result


def decimal_to_snafu(dnum):
	# decimal number to SNAFU number
	assert type(dnum) == int

	max_exponent = 0 
	while dnum > 2*(5**max_exponent):
		max_exponent +=1
	# print(f"max exponent: {max_exponent}	->	2*5**max_exponent = {2*5**max_exponent}")

	remainder = dnum
	result = ""
	for e in reversed(range(max_exponent+1)):
		most_impact_i = 0
		for i in range(5):
			i-=2
			if abs(remainder - i*5**e) < abs(remainder - most_impact_i*5**e):
				most_impact_i = i

		result += str(most_impact_i).replace("-2","=").replace("-1","-")
		remainder -= most_impact_i*5**e

	return result


if __name__ == "__main__":
	# summ snafu blob
	# https://adventofcode.com/2022/day/25
	result = 0
	for row in rows:
		result += snafu_to_decimal(row)
	print("decimal\t->\t",result)
	print("SNAFU\t->\t",decimal_to_snafu(result))

	