# Translation of
# <http://www.cs.brandeis.edu/~storer/LunarLander/LunarLander/LunarLanderListing.jpg>
# by Jim Storer from FOCAL to Python.

from math import sqrt

def setup():
	print("\t\t\t\t LUNAR")
	print("\t       CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
	print("\n\n")
	print("THIS IS A COMPUTER SIMULATION OF AN APOLLO LUNAR")
	print("LANDING CAPSULE.\n\n")
	print("THE ON-BOARD COMPUTER HAS FAILED (IT WAS MADE BY")
	print("XEROX) SO YOU HAVE TO LAND THE CAPSULE MANUALLY.")

L = 0
A = 0
V = 0
M = 0
N = 0
G = 0
Z = 0
K = 0
T = 0
S = 0
W = 0
I = 0
J = 0


def landing():
	global W,V,L
	W = 3600.0 * V;
	#print("ON MOON AT ",L," SECONDS - IMPACT VELOCITY ",W," MPH FUEL REMAINING: " + str(M-N))
	#print("%.3f,%.3f," % (W, (M-N))),
	return

	if (W <= 1.2):
		print("PERFECT LANDING!")
	elif (W <= 10.0):
		print("GOOD LANDING (COULD BE BETTER)")
	elif (W <= 60.0):
		print("CRAFT DAMAGE... YOU'RE STRANDED HERE UNTIL A RESCUE")
		print("PARTY ARRIVES.  HOPE YOU HAVE ENOUGH OXYGEN!")
	else:
		print("SORRY THERE WERE NO SURVIVORS. YOU BLEW IT!")
		print("IN FACT, YOU BLASTED A NEW LUNAR CRATER ",(W*0.277)," FEET DEEP!")

	print("\n\n\nTRY AGAIN?");

def score(fuel, speed):
	score = fuel/speed
	if speed <= 60:
		score += 50
	if speed <= 10:
		score += 50
	if speed <= 1.2:
		score += 100
	if speed > 1000:
		score /= 5
	if speed > 2000:
		score /= 10
	if speed > 3000:
		score /= 100
	return (speed, fuel, score)

def sub420():
	#q, q2, q3, q4, q5;
	global I, J, K,M, N,Z,S,G,V,A

	q  = S * K/M;
	q2 = q * q;
	q3 = q * q2;
	q4 = q * q3;
	q5 = q * q4;

	J=V+G*S+Z*(-q - (q2/2.0) - (q3/3.0) - (q4/4.0) - (q5/5.0));
	I=A-G*S*S/2.0-V*S+Z*S*(q/2.0 + q2/6.0 + q3/12.0 + q4/20.0 + q5/30.0);

def sub330():
	global A, I, J, K, L, M, S, T, V
	L += S;
	T -= S;
	M -= S*K;
	A = I;
	V = J;


def sub340():
	global S,D,V,A,G,Z,K,M
	while (S >= 5.0e-3 ): # line 340
		D = V + sqrt(V*V+2.0*A*(G-Z*K/M));
		S = 2.0 * A / D;
		sub420();
		sub330();


def loop(thrust):
	global A, G, I, J, K, L, M, N, S, T, V, W, Z

	(__,K) = thrust.__next__()

	#print("\nSET BURN RATE OF RETRO ROCKETS TO ANY VALUE BETWEEN")
	#print("0 (FREE FALL) AND 200 (MAXIMUM BURN) POUNDS PER SECOND.")
	#print("SET NEW BURN RATE EVERY 10 SECONDS.\n")
	#print("CAPSULE WEIGHT 32,500 LBS; FUEL WEIGHT 16,500 LBS.")
	#print("\n\n\nGOOD LUCK")
	L=0;
	#print("\nSEC\tMI + FT \tMPH\tLB FUEL\t\tBURN RATE\n")
	A=120.0; V=1.0; M=33000.0; N=16500.0; G=1.0e-3; Z=1.8;

	while True:                        # line 150
		#print ('%3i     %3i+%4i \t%3i \t%7i\t\t%5i'%(\
		#					int(L), floor(A),\
		#					floor(5280.0*(A-floor(A))),\
		#				int(3600.0*V), int(M-N), K))
		#K = input()
		try:
			(__,K) = thrust.__next__()
		except Exception:
			return 0
		T = 10.0

		while True:                    # line 160
			if ((M-N) < 1.0e-3):
				#print"FUEL OUT AT ",L," SECONDS"
				S = (-V + sqrt(V*V + 2*A*G))/G
				V += G*S
				L += S
				landing()
				return score(M-N, W)     # Game over, Man!

			if (T < 1.0e-3):  # line 170
				break

			S = T
			if (M < (N+S*K)):
				S = (M-N)/K

			sub420()
			if (I <= 0.0):
				sub340()
				landing()
				return score(M-N, W)

			if ((V <= 0.0) or (J >= 0.0)):
				sub330()
				continue     # back to line 160

			# line 370
			while True:
				W = (1.0 - M*G/(Z*K))/2.0
				S = M*V/(Z*K*(W+sqrt(W*W+V/Z))) + 0.05
				sub420()

				if (I <= 0.0):
					sub340()
					landing()
					return score(M-N, W)

				sub330()
				if (J > 0.0):
					break
				if (V < 0.0):
					break

	return score(M-N, W)

def main():
	setup()

	thrust = [0,0,0,0,0,0,0,0,200,200,200,200,200,200,200,90,60,16,16,12.1959465,12,12,12,12,12,12,12]

	#while True:
	#for t in thrust:
	print (loop(enumerate(thrust)))

if __name__ == "__main__":
	main()
