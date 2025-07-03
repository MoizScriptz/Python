# Python Operators
## Operators are used to perform operations on variables and values.

## Python divides the operators in the following groups:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators

## ➗ Python Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name           | Example   |
|:--------:|----------------|-----------|
| `+`      | Addition        | `x + y`   |
| `-`      | Subtraction     | `x - y`   |
| `*`      | Multiplication  | `x * y`   |
| `/`      | Division        | `x / y`   |
| `%`      | Modulus         | `x % y`   |
| `**`     | Exponentiation  | `x ** y`  |
| `//`     | Floor Division  | `x // y`  |


## 🧮 Python Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example         | Same As          |
|:--------:|------------------|------------------|
| `=`      | `x = 5`          | `x = 5`          |
| `+=`     | `x += 3`         | `x = x + 3`      |
| `-=`     | `x -= 3`         | `x = x - 3`      |
| `*=`     | `x *= 3`         | `x = x * 3`      |
| `/=`     | `x /= 3`         | `x = x / 3`      |
| `%=`     | `x %= 3`         | `x = x % 3`      |
| `//=`    | `x //= 3`        | `x = x // 3`     |
| `**=`    | `x **= 3`        | `x = x ** 3`     |
| `&=`     | `x &= 3`         | `x = x & 3`      |
| `|=`     | `x |= 3`         | `x = x | 3`      |
| `^=`     | `x ^= 3`         | `x = x ^ 3`      |
| `>>=`    | `x >>= 3`        | `x = x >> 3`     |
| `<<=`    | `x <<= 3`        | `x = x << 3`     |
| `:=`     | `print(x := 3)`  | `x = 3; print(x)`|


## 🔍 Python Comparison Operators

Comparison operators are used to compare two values:

| Operator | Name                         | Example   |
|:--------:|------------------------------|-----------|
| `==`     | Equal                        | `x == y`  |
| `!=`     | Not Equal                    | `x != y`  |
| `>`      | Greater Than                 | `x > y`   |
| `<`      | Less Than                    | `x < y`   |
| `>=`     | Greater Than or Equal To     | `x >= y`  |
| `<=`     | Less Than or Equal

## 🔗 Python Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description                                      | Example                         |
|:--------:|--------------------------------------------------|---------------------------------|
| `and`    | Returns `True` if both statements are true       | `x < 5 and x < 10`              |
| `or`     | Returns `True` if at least one statement is true | `x < 5 or x < 4`                |
| `not`    | Reverses the result                              | `not(x < 5 and x < 10)`         |


## 🧬 Python Identity Operators

Identity operators compare whether two variables reference the **same object in memory**, not just if they are equal.

| Operator  | Description                                       | Example     |
|:---------:|---------------------------------------------------|-------------|
| `is`      | Returns `True` if both variables are the same object     | `x is y`     |
| `is not`  | Returns `True` if both variables are **not** the same object | `x is not y` |


## 🧪 Python Membership Operators

Membership operators are used to test if a **value or variable exists within a sequence** (like list, string, tuple, etc.):

| Operator   | Description                                                      | Example        |
|:----------:|------------------------------------------------------------------|----------------|
| `in`       | Returns `True` if the value is present in the sequence           | `x in y`       |
| `not in`   | Returns `True` if the value is **not** present in the sequence   | `x not in y`   |


## 🧮 Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers at the bit level:

| Operator | Name                 | Description                                                                 | Example    |
|:--------:|----------------------|-----------------------------------------------------------------------------|------------|
| `&`      | AND                  | Sets each bit to `1` if **both** bits are `1`                               | `x & y`    |
| `\|`     | OR                   | Sets each bit to `1` if **one of two** bits is `1`                          | `x | y`    |
| `^`      | XOR                  | Sets each bit to `1` if **only one** of two bits is `1`                     | `x ^ y`    |
| `~`      | NOT                  | Inverts all the bits                                                        | `~x`       |
| `<<`     | Left Shift           | Shift left by pushing in zeros from the right                               | `x << 2`   |
| `>>`     | Right Shift          | Shift right by pushing copies of leftmost bit from the left                 | `x >> 2`   |


