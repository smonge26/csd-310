DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;

ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;

DROP TABLE IF EXISTS book;

DROP TABLE IF EXISTS wishlist;

DROP TABLE IF EXISTS user;

/*
   creating tables
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    store information
*/
INSERT INTO store(locale)
    VALUES('5701 Sunset Dr. Ste 196, Miami, FL 33143');

/*
    books information
*/
INSERT INTO book(book_name, author, details)
    VALUES('ANNIHILATION', 'Jeff VanderMeer', 'In Annihilation, The first volume of Jeff VanderMeer’s Southern Reach trilogy, we join the twelfth expedition to Area X.');

INSERT INTO book(book_name, author, details)
    VALUES('AUTHORITY', 'Jeff VanderMeer', 'In Authority, The New York Times bestselling second volume of Jeff VanderMeer’s Southern Reach trilogy, Area X’s most disturbing questions are answered . . . but the answers are far from reassuring.');

INSERT INTO book(book_name, author, details)
    VALUES('ACCEPTANCE', 'Jeff VanderMeer', 'In this New York Times bestselling final installment of Jeff VanderMeer’s Southern Reach trilogy, the mysteries of Area X may be solved, but their consequences and implications are no less profound — or terrifying.');

INSERT INTO book(book_name, author, details)
    VALUES('The Alchemists of Loom.', 'Elise Kova', 'Her vengeance. His vision. The first book in the Loom Saga.');

INSERT INTO book(book_name, author, details)
    VALUES('The Dragons Of Nova', 'Elise Kova', 'The second book in the Loom Saga.');

INSERT INTO book(book_name, author, details)
    VALUES('The Rebels Of Gold', 'Elise Kova', 'This is the final installment of USA Today bestselling author Elise Kova’s Loom Saga, THE REBELS OF GOLD will reveal the fate of Loom’s brilliantly contrasting world and its beloved inhabitants.');

INSERT INTO book(book_name, author, details)
	VALUES('Binti', 'Nnedi Okorafor', 'Her name is Binti, and she is the first of the Himba people ever to be offered a place at Oomza University, the finest institution of higher learning in the galaxy. But to accept the offer will mean giving up her place in her family to travel between the stars among strangers who do not share her ways or respect her customs.');

INSERT INTO book(book_name, author, details)
    VALUES('Home', 'Nnedi Okorafor', 'It’s been a year since Binti and Okwu enrolled at Oomza University. A year since Binti was declared a hero for uniting two warring planets. A year since she found friendship in the unlikeliest of places.');

INSERT INTO book(book_name, author, details)
    VALUES('The Night Masquerade', 'Nnedi Okorafor', 'Binti has returned to her home planet, believing that the violence of the Meduse has been left behind. Unfortunately, although her people are peaceful on the whole, the same cannot be said for the Khoush, who fan the flames of their ancient rivalry with the Meduse.');

/*
    users information
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Ross', 'Geller');

INSERT INTO user(first_name, last_name)
    VALUES('Rachel', 'Green');

INSERT INTO user(first_name, last_name)
    VALUES('Chandler', 'Bing');

/*
	wishslist information
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ross'), 
        (SELECT book_id FROM book WHERE book_name = 'ACCEPTANCE')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Rachel'),
        (SELECT book_id FROM book WHERE book_name = 'Binti')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chandler'),
        (SELECT book_id FROM book WHERE book_name = 'The Dragons of Nova')
    );