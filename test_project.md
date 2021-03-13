## TASK

В карьере находятся 3 самосвала с бортовыми номерами “101”, “102” и “K103”.
“101” и “102” самосвалы модели “БЕЛАЗ”, а “K103” – “Komatsu”. 
У моделей “БЕЛАЗ” максимальная грузоподъемность 120 т руды, а у “Komatsu” – 110 т. На текущий момент “101”
самосвал везет 100 т руды, “102” – 125 т, “K103” – 120 т.

* Руда характеризуется процентным содержанием полезных веществ - диоксида кремния и железа.
- “101” самосвал везет руду с содержанием 32% SiO2 и 67% Fe
- “102” - 30% SiO2 и 65% Fe
- “K103” - 35% SiO2 и 62% Fe
- Самосвалы везут руду на склад, на котором уже находится 900т руды с содержанием 34% SiO2 и 65% Fe.
* Территория склада ограничена полигоном, представление которого в формате WKT: POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)).

Самосвалы разгружаются, пытаясь попасть в координаты полигона, но не всегда это у них
получается.

#### Задача
    Реализовать веб-приложение на фреймворке Django
    1. Спроектировать ORM-модели для перечисленных объектов и событий
    2. Создать страницу, которая открывается первой при заходе на адрес веб-приложения, на
    которой отобразить таблицы следующего вида:

## TO DO
#### Create project
- [ ] Add validation form for system.
- [ ] 
- [ ] Explore how interpretier format WKT on Django model.
- [ ] Add format WKT on Django model.
- [ ] Create templates as example
- [x] Create Base Storage model
- [x] Crate Base Truck model
- [x] Create Admin view for models 
#### Deploy project

## INFO

## Sources
- https://ru.stackoverflow.com/questions/824011/%D0%92%D1%8B%D0%B2%D0%BE%D0%B4-%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%BC%D0%BE%D0%B3%D0%BE-%D0%B1%D0%B0%D0%B7%D1%8B-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-django  Вывод содержимого базы данных с помощью Django
- https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html  How to Reset Migrations
## Admin data: ivan, gremlin40