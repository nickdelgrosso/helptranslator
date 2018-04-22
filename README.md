
# helptranslator: help() for everyone.

This is an experimental python package that translates Python's **help()** text
to any language using Google Translate!  

Why?  Because learning Python shouldn't require fluency in English, and the help() function
is the most language-intensive part of the early programming language learning experience.
Plus, Python 3 fully supports Unicode, so why not?

## Installation

```bash
  pip install helptranslator
```

## Example

Calling the **set_help_lang()** function overrides the built-in **help()** function,
so working with helptranslator is essentially a two-liner:

```python
  import helptranslator
  helptranslator.set_help_lang('german')
```

That's it!  Let's change the help text to German and look at the sum() function:

```python
  import helptranslator
  helptranslator.set_help_lang('german')

  help(sum)
  >> Hilfe zur eingebauten Funktionssumme in den eingebauten Modulen:

 Summe (iterierbar, Start = 0, /)
    Gibt die Summe eines "Start" -Werts (Standard: 0) plus einer Anzahl von Zahlen zurück
    
    Wenn das iterable leer ist, geben Sie den Startwert zurück.
    Diese Funktion ist speziell für die Verwendung mit numerischen Werten und möglicherweise vorgesehen
    lehnen Sie nicht-numerische Typen ab.

```

Or Chinese:

```python
  import helptranslator
  helptranslator.set_help_lang('chinese (simplified)')

  help(sum)
  >> Hilfe zur eingebauten Funktionssumme in den eingebauten Modulen:

  帮助内置函数总和模块builtins：

  sum（iterable，start = 0，/）
      返回“开始”值（默认值：0）加上可迭代的数字的总和
      
      当迭代器为空时，返回起始值。
      此功能专门用于数字值和可能
      拒绝非数字类型。

```

Or Russian:

```python
  import helptranslator
  helptranslator.set_help_lang('russian')

  help(sum)
  >> Справка по встроенной функции sum в встроенных модулях:

  sum (iterable, start = 0, /)
      Возвращает сумму значения «start» (по умолчанию: 0) плюс итерабельность чисел
      
      Когда итерабельность пуста, верните начальное значение.
      Эта функция предназначена специально для использования с числовыми значениями и может
      отклонять нечисловые типы.
```


## Todos

Well, clearly this is a limited approach.  It requires an internet connection, long
texts fail in their connections, and I haven't added IPython support yet.  The last
two can be fixed pretty easily (if you are interested in having this, let me know!) but
the first requires a more thoughtful approach.  Personally, I'm imagining some kind of
stub file that package developers can create for their packages.  

Hopefully, this is useful, and generates some conversation about increasing programming
education around the world!
