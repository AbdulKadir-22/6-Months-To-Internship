## Single Variable used to store multiple items

List  = [] ordered and changeable. Duplicates OK

Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates

Tuple = () ordered and unchangeable. Duplicates OK. FASTER

```python
Fruits = ["Apple", "Banana", "Coconut"]
Fruits.append("Pineapple")
Fruits.remove("Apple")
Fruits.insert(0,"Pineapple")
Fruits.sort()
Fruits.reverse()
Fruits.clear()
```

dictionary =  a collection of {key:value} pairs
                       ordered and changeable. No duplicates

```python
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()
```

- Random
    
    import random
    
    low = 1
    high = 20
    options = ['Rock', 'Paper', ‘Scissors’]
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    number = random.random()
    
    number= random.randint(1, 6)
    
    number= random.randint(low, high)
    
    number= random.choice(options)
    
    number.shuffle(cards)
    
- Mini Projects