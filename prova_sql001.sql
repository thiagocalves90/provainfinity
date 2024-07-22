CREATE DATABASE Pessoas;

USE Pessoas;

CREATE TABLE Pessoas (
    ID INT PRIMARY KEY,
    NomeCompleto VARCHAR(255),
    Idade INT,
    Genero VARCHAR(10),
    Nacionalidade VARCHAR(50),
    Email VARCHAR(255),
    EstadoCivil VARCHAR(20),
    NomePai VARCHAR(255),
    NomeMae VARCHAR(255)
);

INSERT INTO Pessoas (ID, NomeCompleto, Idade, Genero, Nacionalidade, Email, EstadoCivil, NomePai, NomeMae)
VALUES (1, 'João da Silva', 30, 'Masculino', 'Brasileiro', 'joao.silva@email.com', 'Casado', 'José da Silva', 'Maria da Silva');

INSERT INTO Pessoas (ID, NomeCompleto, Idade, Genero, Nacionalidade, Email, EstadoCivil, NomePai, NomeMae)
VALUES (2, 'Maria Oliveira', 25, 'Feminino', 'Brasileira', 'maria.oliveira@email.com', 'Solteira', 'Pedro Oliveira', 'Ana Oliveira');

INSERT INTO Pessoas (ID, NomeCompleto, Idade, Genero, Nacionalidade, Email, EstadoCivil, NomePai, NomeMae)
VALUES (3, 'Carlos Santos', 40, 'Masculino', 'Brasileiro', 'carlos.santos@email.com', 'Divorciado', 'Antonio Santos', 'Luiza Santos');

UPDATE Pessoas
SET EstadoCivil = 'Casada', Email = 'maria.oliveira.casada@email.com'
WHERE ID = 2;

DELETE FROM Pessoas
WHERE ID = 3;
