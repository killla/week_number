# Задание

- Определить номер недели. Первый день недели - воскресенье. Недели считаются с единицы, в том числе неполные.

- Размещение на хостинге https://www.pythonanywhere.com/

- Код на github.com

- Наличие тестов

- Наличие комментариев в коде


### Раскрытие умолчаний, не указанных в ТЗ

Задача реализовывается в виде сайта с публичным доступом.

Точка отсчета на первый взгляд это всегда начало года. Но с учетом контекста (сервис составления спортивных программ тренировок) началом периода может быть любая дата.
Соответственно входные данные: начальная дата, конечная дата. Выходные данные: номер недели.

Реализовывать будем на Django. Для данной задачи избыточно. Но т.к. в описании вакансии основным фреймворком для работы указана Django и основной целью тестового задания является определение владения рабочими инструментами, считаем это условие ключевым при выборе инструментов реализации.


### Алгоритм

Номера недель считаются делением по модулю (оператор `//` в python). Делимое - количество дней, прошедшее с начальной даты. Делитель - длина недели - 7.

С учетом того, что первая неделя может начаться в середине недели, для точного учета границ недели, дополняем делимое некоторым поправочным коэффициентом. 
Поправочный коэффициент зависит от порядкового номера дня недели начальной даты.

1 января 2019 года: `0 // 7 = 0`

5 января 2019 года: `4 // 7 = 0`

6 января: `5 // 7 = 0` -> здесь должен быть поправочный коэффициент, дополняющий до семи 

6 января: `(5+2) // 7 = 1`

Следующая смена номера недели

12 января: `(11+2) // 7 = 1`

13 января: `(12+2) // 7 = 2`

По условию номера недель считаются с единицы, деление по модулю "считает" с нуля. Добавляем к результату единицу.

Поправочный коэффициент есть ни что иное, как стандартная функция Python isoweekday().  

Итоговая функция

`номер недели = (количество дней + коэффициент) // 7+1`


Остается только проверить, что вторая дата находится позже первой. Даты валидны (в формате, который python может прочитать). И вообще к нам прилетели с фронта именно даты, а не что-то другое.

# Результат

[https://killla.pythonanywhere.com/week/](https://killla.pythonanywhere.com/week/)
