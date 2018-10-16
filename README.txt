Файл notes_app\database_functions имеет 2 функции для работы с бд через MySQL, для записи и получения
В файле notes_app\views находится функция сортировки записей, от меньшего количества уникальных слов до большего
Функция обработки запроса также находится в notes_app\views
Страница генерируется с помощью html файла, notes_app\templates\notes\post_list.html


Генерация таблицы в базе данных, применялась на моем компьютере:
"CREATE TABLE notes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), text TEXT)"
