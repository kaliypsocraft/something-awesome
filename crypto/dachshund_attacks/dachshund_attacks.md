# CTF Write-Up: [Dachshund Attacks][Cryptography]

## Description
>What if d is too small? Connect with nc mercury.picoctf.net 31133.


## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{proving_wiener_3899149}`)

## Difficulty
- **Difficulty Level:** medium

## Tools Used
- pwntools

## Write-Up

### Preparatory Phase

Running the remote connection the observer obtains parameters $e$, $n$ and $c$. 
```
Welcome to my RSA challenge!
e: 38921143885956173571507895843596262266450334726133106736046701224979250176125678032870962036702024083888563464140694355776846810961720783062835148709295551479429864288229788286349989950722680582141952551557084896941240087614152413568339085764147264903562241284079789147389528523430143472649237656261763260113
n: 107175151218872570272000046399183976520425719573115139590240162534691517132786086909937045878545596320952840836361744997857693488372107750102120590329931372814051887282503970154678043287458861709273972234306141986810573548594851587149632301712363437634261367978760758031755981917050626352274869547454155264653
c: 93808590344894515268784207530408292070502630089434555990902288066232664616090719630113540166887061171094713123066985298130776970709640393684993012587437369483116993612408823822018751981088656989008843458175879892082281530452216783487332667140042596668277895781963061730947548482426219910622512651793490654051
```

These parameters are too large to brute-force a prime factorisation of $n$ therefore we need to look for another route. The clue of "What is the $d$ is too small" reminds me an attack I learnt in `COMP6453`(Applied Cryptography) called Wiener's attack whereby if an RSA private key is upper-bounded in value, it can be determined using continued fractions. I didn't recall the exact details but this lead to my research brain to turn on again.

### Attack Phase
Upon connecting to the host and port, we are greeted with values $e$, $n$, and $c$. I ran the connection multiple times to check if the exponents and variables changed, and they did.

Using the clue that $d$ is small suggests attempting [[Wiener's attack]]. To execute this, download `import owiener` and run `d = owiener.attack(e, n)`. 

Next, obtain $m$ using the equation $c^{d} \mod n$. I attempted to decode the result as ASCII, which initially yielded some garbled output. However, a simple `long_to_bytes()` function successfully converted the result into a readable format.
### Final Solution/Payload
``` py
from pwn import *
import owiener
from Cryptodome.Util.number import long_to_bytes, bytes_to_long

e = 26178309766743842489285048064116878464884511723174029446673981758317149297108860929111130362790370305519135539752724869370541746944023968948449507675012153783345430219478733778225734185410024379350236274286969218532060152402406854526792145291718838082778812787899452930129564272973102115753855931174614283259
n = 127257001275209156619317163515619384325539311291284613971174553538298916980792504498224393536720652805739418483480359153396007886003547533832854505941065194968828883325605498591952342296090238533861933359527337311643052676267005708571680064928005748683812235243663906926199186693487549985234055120129058247597
c = 15977144308665168267735991529714212422660772718310542791573085073630672781871482736087417727735669019193319060378562218771275314640379104050133170455710600378061592032073486980215039922979212974079469896792240480415513988114361209282153636151629501724691036982473329858181162444410020386441986536954673392473
d = owiener.attack(e, n)

m = pow(c, d, n)
assert(pow(m, e, n) == c)
print(long_to_bytes(m).decode())

```
### Lessons Learnt

This attack highlights the need for implementers to check the size of parameters. If a private key satisfies the following condition Given the RSA modulus $N = pq$ with $q < p < 2q$ and private exponent $d$ satisfying $d < \frac{1}{3} N^{1/4}$, we aim to demonstrate how an attacker can efficiently recover $d$ given the public key $\langle N, e \rangle$ where $ed \equiv 1 \pmod{\lambda(N)}$. Then one can use Wiener's attack. Source: [here](https://en.wikipedia.org/wiki/Wiener%27s_attack).

Using a simple library from Python can disrupt a seemingly mathematically robust cipher if these parameters are not satisfied. The actual mathematical implementation of Wiener's algorithm involves using continued fractions to approximate $d$.


## References
- https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf


