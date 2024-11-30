# Retrospective 30.11.2024
### 1. Denormalizacja
 - Składowe umowy handlowej (chciane surowce, wymagane surwoce), moglibyśmy trzymać to zapisane w JSON'ie. 2 tabele mniej, łatwiejsze wyszukiwanie, mniej przechodzenia po tabelach.

 ### 2. Ogólne zmiany
 - Dodanie pola z odnośnikiem do zdjęcia przypisanego do encji (np. dla Państwa, Surowca). Funkcjonalność, której nie uwzględniliśmy. Natomiast, jest ona przydatana końcowemu użytkownikowi.
 - Modyfikatory - moglibyśmy użyć GenericKey na cel modyfikatora.