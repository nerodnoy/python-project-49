## Hexlet tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/a609a610ad188db3b246/maintainability)](https://codeclimate.com/github/nerodnoy/python-project-49/maintainability)

[![Actions Status](https://github.com/nerodnoy/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/nerodnoy/python-project-49/actions)


## Hexlet Project: Brain Games

Этот проект был создан для обучающей платформы **Hexlet** в рамках программы по изучению профессии **Python-разработчик**. Он содержит пять математических мини-игр:

 - Посчитай-ка! *(Calculations)*
 - Чётное / Нечётное *(Even / Odd)*
 - Вставь пропущнное число *(Fill a Progression)*
 - Найди наибольший общий делитель *(Get a Greatest Common Divisor)*
 - Простое ли это число? *(Prime or Not Prime)*

> Аскинемы с примером работы мини-игр находятся в конце readme.

### Необходимые требования

[Python 3.8.1+](https://www.python.org/downloads/)

[Poetry](https://python-poetry.org/docs/)

### Установка
   

    git clone git@github.com:nerodnoy/python-project-49.git

>>

    cd python-project-49/
    poetry build
    python -m pip install --user dist/*.whl

### Команды для вызова игр

    brain-even # Чётное / Нечётное
    brain-calc # Вычисления 
    brain-gcd # Нахождение наибольшего общего делителя
    brain-progression # Заполнение прогрессии
    brain-prime # Простое число или нет

### Правила игры
Для **успешного** прохождения любой из игр необходимо дать **три правильных** ответа.

В случае предоставления **неверного** ответа, игра **завершается**.

### Демонастрация возможностей игр

    brain-even 
[![asciicast](https://asciinema.org/a/gxYTRyXnzjhfKyZQEOIRpsaGp.svg)](https://asciinema.org/a/gxYTRyXnzjhfKyZQEOIRpsaGp)

    brain-calc

[![asciicast](https://asciinema.org/a/BVeQtFNNTPAj2Za4739bJ7q4e.svg)](https://asciinema.org/a/BVeQtFNNTPAj2Za4739bJ7q4e)

    brain-gcd
[![asciicast](https://asciinema.org/a/2Fo9xcvCZNwnvG8bayW9P0qMX.svg)](https://asciinema.org/a/2Fo9xcvCZNwnvG8bayW9P0qMX)

    brain-progression

[![asciicast](https://asciinema.org/a/wMUj5iSIL7Aaig6nvJkUnIKQt.svg)](https://asciinema.org/a/wMUj5iSIL7Aaig6nvJkUnIKQt)

    brain-prime
[![asciicast](https://asciinema.org/a/OtAi6NBbteuikyBMVfCMYZJ3O.svg)](https://asciinema.org/a/OtAi6NBbteuikyBMVfCMYZJ3O)
