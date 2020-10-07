## City Quest Competition task

Суть задания: за 4 часа кодинга реализовать по максимуму фунционал системы квестов в городе (вроде pokemon go)  
Существует singleton соревнование между несколькими командами, каждой команде выдается 6 квестов с координатами, куда надо прибежать и ответить на задание. За ошибки начисляются штрафные баллы, можно брать подсказки. 

По итогу формируется лидерборд, побеждает команда с наибольшим количеством сделанных заданий или наименьшим потраченным временем.

Что получилось реализовать за 4 часа:
 - создание и авторизация команд
 - создание заданий
 - просмотр своих заданий и статусов (не начато, не сдано, сдано)
 - сдача заданий по геолокации
 - лидерборд с штрафным временем за ошибки и сданными заданиями
 - обернуть всё в docker
 - написать документацию для API

API Docs (main business logics flow inside):  
https://documenter.getpostman.com/view/5482678/TVK5cMBf

Run project:  
`docker-compose up -d`

Hosts on http://127.0.0.1:5000  
Includes mongodb, so no extra actions required.

Why MongoDB over SQL:  
Didn't want to spend extra time on imlementing geo math, mongo has included one out of the box.