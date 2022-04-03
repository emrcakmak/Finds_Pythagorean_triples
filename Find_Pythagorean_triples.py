
from multiprocessing import Process,Value



def hipotonTri(limits, p):
    c = 0
    m = 2
    print("proccess", {p})
    current = limits*(p-1)

    storeg = 0
    while True:

        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n


            if c > limits*p:
                print(f"p {p} finished")
                storeg = 1
                break
            if current < c:
                yield a,b,c

        if storeg == 1:
            break

        m = m + 1

def SingleProcess(limits, p):
        for text in hipotonTri(limits, p):
            print(text)


if __name__ == '__main__':
    size = 1000
    p = 8
    storeg=Value('i',0)
    number_new = size/p
    process = []
    for i in range(1,p+1):
        process.append(Process(target=SingleProcess, args=(number_new,i)))

    for pross in process:
        pross.start()

    for pross in process:
        pross.join()