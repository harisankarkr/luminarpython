name=["a","b","c","d","e","f","g","h"]
passed=["a","b","c"]

nameset=name()
passedset=passed()

failed=nameset.difference(passedset)
print(failed)