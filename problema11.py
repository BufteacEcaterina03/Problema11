n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
# if n<10:
for i in range(0,n):
    x=int(input('Dati elementul=')) 
    a.extend([x])
print(a)
print('a) afiseaza pe ecran componentele tabloului la un interval de 5 pozitii;')
print(a[:5])
print('b) afisează pe ecran numerele in ordinea inversa a introducerii in calculator;')
for i in range(len(a),0, -1):
    print(a[i-1])
print('c) sorteaza componentele tabloului in ordine descrescatoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d) afiseaza pe ecran doar componentele pare;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print(c)
print('e) afiseaza pe ecran media aritmetica a componentelor pare;')
print(sum(c)/len(c))
print('f) afiseaza pe ecran doar componentele impare;')
d=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        d.extend([y])
print(d)
print('g) afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y (valorile x si y se citesc de la tastatura);')
x=int(input('valoarea x= '))
y=int(input('valoarea y= '))
g=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]%y!=0)):
        u=a[i]
        g.extend([u])
print(g)
print('h) afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y (valorile x şi y se citesc de la tastatura);')
x1=int(input('valoarea x= '))
y1=int(input('valoarea y= '))
h=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]<y)):
        u1=a[i]
        h.extend([u1])
print(h)
print('i) afiseaza pe ecran pozitiile (indiciile) componentelor impare negative;')
for i in a:
    if i < 0 and i%2==1:
        print(a.index(i))
print('j) afiseaza pe ecran pozitiile (indiciile) componentelor ce contin doar doua cifre semnificative;')
for i in a:
    if (i < 100 and i>9) or (i > -100 and i<-9):
        print(a.index(i))
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=a
x=min(k)
k.insert(0,x)
print(k)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=a
l1=l.index(min(l))
l2=l[0]
l[l1]=l2
print('m) creeaza un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatura;')
even = []
for i in a:
    if i % 2 == 0:
        even.append(i)
print(even)
print('n) creeaza un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura;')
en = []
for i in a:
    if i % 3 == 0:
        en.append(i)
print(en)
print('o) creeaza un tablou nou, format doar din acele componente ale tabloului introdus de la tastatura care au cel mult patru divizori.')
h = []
for i in a:
    counter = 0
    for b in range(1,i):
        if i%b==0:
            counter+=1
    if counter < 5:
        h.append(i)
print(h)