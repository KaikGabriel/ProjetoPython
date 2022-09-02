create database bdTI14TProjeto;
use bdTI14TProjeto;

create table pessoa(
	codigo int not null primary key auto_increment,
    login varchar(120) not null,
    senha varchar(15) not null
) engine = InnoDB;

select * from pessoa;