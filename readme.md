# Описание

Данный репозиторий содержит лексический анализатор, разработанный на языке Python с использованием конечного автомата для распознавания лексем.

## Архитектура проекта:
* **[classes](https://github.com/uselesscloudlet/compiler/tree/master/classes)** (папка с классами)
    * *definitions* (определение списков и enum)
    * *lexem* (выделение лексем в отдельный класс. Объект хранит в себе строчку кода, тип лексемы, её значение и аттрибут)
    * *stateMachine* (класс, содержащий реализацию конечного автомата с использованием вспомогательных функций)
* **[tests](https://github.com/uselesscloudlet/compiler/tree/master/tests)** (папка с тестами)
    * *digits.c* (проверка чисел)
    * *example.c* (проверка других правил)
* **[attachemnt](https://github.com/uselesscloudlet/compiler/tree/master/attachment)**
    * *FSMgraph.drawio* (файл, содержащий информацию о построенном графе. Его можно открыть по [ссылке](https://app.diagrams.net/))
    * *FSMgraph.png* (реализованный конечный автомат в виде графа)
    * *grammar.txt* (грамматика по которой создавался анализатор)

*identifier* (файл, позволяющий прочитать и анализировать входной текст и выдать конечный результат)    
*main* (запускающий файл)   
*requirements.txt* (файл с требуемыми модулями (pip install -r requirements.txt))   
*result* (файл с результатами анализа)