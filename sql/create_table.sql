CREATE TABLE `Price` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`Date` DATETIME NOT NULL,
	`Area_Code` varchar(8) NOT NULL,
	`Total_Condo_Sold_Number` INT NOT NULL,
	`Avg_Price` FLOAT NOT NULL,
	`Med_Price` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Date` (
	`Date` DATETIME NOT NULL,
	`Inflation` FLOAT NOT NULL,
	`GDP` FLOAT NOT NULL,
	`Metal_Price` FLOAT NOT NULL,
	`NASDAQ` FLOAT NOT NULL,
	PRIMARY KEY (`Date`)
);

CREATE TABLE `Toronto` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`Date` DATETIME NOT NULL,
	`Prime_Rate` FLOAT NOT NULL,
	`Median_Age` FLOAT NOT NULL,
	`Participation_Rate` FLOAT NOT NULL,
	`Employment_Rate` FLOAT NOT NULL,
	`Population` FLOAT NOT NULL,
	`UT_Total_Enrollment` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Ontario` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`Date` DATETIME NOT NULL,
	`Immigrants_International` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `New` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`Date` DATETIME NOT NULL,
	`Units_Number_Planned` INT NOT NULL,
	`Units_Number_Construction` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `All` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`Date` DATETIME NOT NULL,
	`Condo_Sold_Number` INT NOT NULL,
	`Avg_Price` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Price` ADD CONSTRAINT `Price_fk0` FOREIGN KEY (`Date`) REFERENCES `Date`(`Date`);

ALTER TABLE `Toronto` ADD CONSTRAINT `Toronto_fk0` FOREIGN KEY (`Date`) REFERENCES `Date`(`Date`);

ALTER TABLE `Ontario` ADD CONSTRAINT `Ontario_fk0` FOREIGN KEY (`Date`) REFERENCES `Date`(`Date`);

ALTER TABLE `New` ADD CONSTRAINT `New_fk0` FOREIGN KEY (`Date`) REFERENCES `Date`(`Date`);

ALTER TABLE `All` ADD CONSTRAINT `All_fk0` FOREIGN KEY (`Date`) REFERENCES `Date`(`Date`);
