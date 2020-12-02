# Описание

Данный репозиторий содержит лексический и синтаксический(LR) анализаторы, разработанные на языке Python с использованием конечного автомата для распознавания лексем.

## Архитектура проекта:
* **[classes](https://github.com/uselesscloudlet/compiler/tree/master/classes)** (папка с лексическим анализатором)
    * *definitions* (определение списков и enum)
    * *lexem* (выделение лексем в отдельный класс. Объект хранит в себе строчку кода, тип лексемы, её значение и аттрибут)
    * *stateMachine* (класс, содержащий реализацию конечного автомата с использованием вспомогательных функций)
* **[syntax](https://github.com/uselesscloudlet/compiler/tree/master/syntax)** (папка с синтаксическим анализатором)
    * **[settings](https://github.com/uselesscloudlet/compiler/tree/master/syntax/settings)** (папка для настроек)
        * *control_table.csv* (управляющая таблица)
        * *lexem_to_term*
        * *lexems.csv* (файл с лексемами)
        * *syntax.json* (json управляющая таблица)
    * *draw* (рисование дерева синтаксического разбора)
    * *parser* (класс с парсером)
* **[tests](https://github.com/uselesscloudlet/compiler/tree/master/tests)** (папка с тестами)
    * *digits.c* (проверка чисел)
    * *example.c* (проверка других правил)
    * *grammar_example.c* (проверка синтаксическим анализатором)
* **[attachemnt](https://github.com/uselesscloudlet/compiler/tree/master/attachment)**
    * *FSMgraph.drawio* (файл, содержащий информацию о построенном графе. Его можно открыть по [ссылке](https://app.diagrams.net/))
    * *FSMgraph.png* (реализованный конечный автомат в виде графа)
    * *grammar.txt* (грамматика по которой создавался анализатор)
    * *control_table.csv* (управляющая таблица)
    * *tree.png* (дерево синтаксического разбора)

*identifier* (файл, позволяющий прочитать и анализировать входной текст и выдать конечный результат)    
*lexer* (запускающий файл лексического анализатора)   
*requirements.txt* (файл с требуемыми модулями (pip install -r requirements.txt))   
*syntax* (запускающий файл синтаксического анализатора)