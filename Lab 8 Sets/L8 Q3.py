st=set()
for i in range(0,5):
    n=input("Enter name: ")
    st.add(n)
print(st)
lt=list(st)
lt[2]="Anjali"
st=set(lt)
print(st)
st.pop()
st.pop()
print(st)
