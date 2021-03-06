# Kaeshir Dictionary

A free, open source database of Kashmiri words which is my own work and I'm opening it for everyone. You can use, modify and distribute it for any purpose. 

`pip install kashmiri`

You can check my app `Kaeshir Dictionary`
* [Play Store](https://play.google.com/store/apps/details?id=com.izanmajeed.dictionary)
* [App Store](https://apps.apple.com/in/app/kaeshir-dictionary/id1563319945)


## Use the `find()` fucntion to get the Kashmiri meaning of corresponding English word as a **python dictionary.**

```python
>>> from kashmiri import find
>>> from pprint import pprint
>>>
>>> find("admire")
{'title': 'Admire', 'pos': '/ əd-ˈmī(-ə)r/, verb', 'englishMeaning': 'Khosh karun ', 'kashmiriMeaning': 'خۄش کران', 'englishExample': 'I admire Manika.', 'kashmiriExample': 'Winni chai kaem chalan'}
>>>
>>> x = find('about')
>>> pprint(x)
{'englishExample': 'What do you think about me?',
 'englishMeaning': 'Mutalik',
 'kashmiriExample': 'Tsai kya ba:sa:n mai mutalik?',
 'kashmiriMeaning': 'مُتعلِق',
 'pos': '/ ə-ˈbau̇t/, adverb',
 'title': 'About'}
>>> 
```


* If the given word is not found, a string saying `Not Found` will be displayed.

```python
>>> find('grep')
Not Found
>>> 
```


* Search is `Case Insensitive`

```python
>>> find('account')
{'title': 'Account', 'pos': '/ ə-ˈkau̇nt/, noun', 'englishMeaning': 'Hisa:b', 'kashmiriMeaning': 'حِساب', 'englishExample': 'She was asked to give an account of her actions.', 'kashmiriExample': 'Winni chai kaem chalan'}
>>> 
>>> find('aCcOuNt')
{'title': 'Account', 'pos': '/ ə-ˈkau̇nt/, noun', 'englishMeaning': 'Hisa:b', 'kashmiriMeaning': 'حِساب', 'englishExample': 'She was asked to give an account of her actions.', 'kashmiriExample': 'Winni chai kaem chalan'}
>>> 
```


* `AssertionError` will be thrown if you search for some gibberish

```python
>>> find("osama bin laden")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/izan/Documents/Kaeshir-Database/kashmiri/kashmiri.py", line 5, in find
    assert word.isalpha(), "You might be a Haput, else you could have entered a correct word."
AssertionError: You might be a Haput, else you could have entered a correct word.
>>> 
```
* Get access to whole database in the form of tuple using `data` variable in `database` file

```python
>>> from kashmiri.database import data
>>> data[0]
{'title': 'Abandoned', 'pos': '/ ə-ˈban-dənd/, adjective', 'englishMeaning': 'Trovmut (m.)', 'kashmiriMeaning': 'ترٛومُت', 'englishExample': 'An abandoned factory.', 'kashmiriExample': 'Akh traivmich factry.'}
>>> 
```
