## What I learned
### Definition of a Shallow Copy
> * Shallow copy of a list duplicates the outer list, but the elements inside the list are still referenced to the same items in the original list
> * So if you have a list of lists (to be an array) and you copy it, only the rows are duplicated, but each item in each row has a shared reference
> * So if you update an item in one array, they both update
> * Have to use deepcopy instead