def bubble(a,n):
    for i in range(1,n):
        for j in range(1,n):
            if a[j]<a[j-1]:
                (a[j],a[j-1])=a[j-1],a[j]
    return a




def left(i):
    return 2*i+1
def right(i):
    return 2*i + 2

def heapify(a,i):

    L=left(i)
    R=right (i)
    max = i
    if len (a)>L and a[max]<a[L]:
        max=L
    if len (a)>R and a[max]<a[R]:
        max=R

    if max!=i:
        a[i],a[max] = a[max],a[i]
        return heapify(a,max)
    # זמן ריצה מקסימום log2n
def build(a):
    for i in range(len(a)//2,-1,-1):
        heapify(a,i)

def main():
    a=[27,17,3,16,13,10,1,5,7,12,4,8,9,0]
    n=3
    build(a)
    print(a)

if __name__ == '__main__':
    main()
"""  סיבוכיות זמן וסיבוכיות מקום:::



מושפע מגודל הקלט , ביחס לאינסוף הוא מוגדר.
עץ בינארי מלא- לכל קודקוד או 0 בנים או 2 בנים
עץ בינארי שלם- בעץ נראה במקסימום האפשרי עבור עומק 

"""