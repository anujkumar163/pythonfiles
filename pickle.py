import pickle
f1 = open("sample", "wb")
i = []
i.append("amit")
print("Hello...")
i.append("sumit")
pickle.dump(i,f1)
print("updated!")
f1.close()

'''import pickle
f2=open("sample", "rb")
data = pickle.load(f2)
print(data)
f2.close()'''

'''import pickle#joblib
with open("sample", "rb") as fobj:
    data = pickle.load(fobj)
    print(data)
    fobj.close()'''
