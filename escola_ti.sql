
USE escola_ti; -- No MySQL, o comando "USE" funciona para selecionar o banco!

-- 1. Limpa as tabelas existentes para eliminar incompatibilidades anteriores
DROP TABLE IF EXISTS Matricula;
DROP TABLE IF EXISTS Telefone_Aluno;
DROP TABLE IF EXISTS Aluno;
DROP TABLE IF EXISTS Curso;
DROP TABLE IF EXISTS Instrutor;

-- 2. Tabela de Instrutores
CREATE TABLE Instrutor (
	id_instrutor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR (100) NOT NULL,
    especialidade VARCHAR (50) NOT NULL
) ENGINE=InnoDB;

-- 3. Tabela de Cursos
CREATE TABLE Curso (
   id_curso INT AUTO_INCREMENT PRIMARY KEY,
   nome_curso VARCHAR (100) NOT NULL,
   carga_horaria INT CHECK (carga_horaria > 0),
   vagas_maximas INT DEFAULT 30 CHECK (vagas_maximas > 0),
   id_instrutor INT NULL,
   CONSTRAINT fk_curso_instrutor FOREIGN KEY (id_instrutor)
       REFERENCES Instrutor(id_instrutor) ON DELETE SET NULL
)ENGINE=InnoDB;

-- 4. Tabela de Alunos
CREATE TABLE Aluno (
  id_aluno INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR (100) NOT NULL,
  email VARCHAR (100) UNIQUE NOT NULL
)ENGINE=InnoDB;

-- 5. Tabela Multivalorada para Telefones do Aluno
CREATE TABLE Telefone_Aluno (
  id_telefone INT AUTO_INCREMENT PRIMARY KEY,
  id_aluno INT NOT NULL,
  numero VARCHAR (20) NOT NULL,
  CONSTRAINT fk_telefone_aluno FOREIGN KEY (id_aluno)
      REFERENCES Aluno (id_aluno) ON DELETE CASCADE
)ENGINE=InnoDB;

-- 6. Tabela Associativa de Matrícula (N:M)
CREATE TABLE Matricula (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    id_curso INT NOT NULL,
    data_matricula DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Ativa' CHECK (status IN ('Ativa', 'Cancelada', 'Concluida')),
    CONSTRAINT fk_matricula_aluno FOREIGN KEY (id_aluno)
        REFERENCES Aluno (id_aluno) ON DELETE RESTRICT,
    CONSTRAINT fk_matricula_curso FOREIGN KEY (id_curso)
        REFERENCES Curso (id_curso) ON DELETE RESTRICT, -- Corrigido para REFERENCES
    CONSTRAINT unq_aluno_curso UNIQUE (id_aluno, id_curso)
)ENGINE=InnoDB;

-- DEFINIÇÃO DE DEFAULT DE DATA VIA TRIGGER (Para compatibilidade de versões do MySQL)
DELIMITER //
CREATE TRIGGER trg_matricula_bi
BEFORE INSERT ON Matricula
FOR EACH ROW
BEGIN
    IF NEW.data_matricula IS NULL THEN
       SET NEW.data_matricula = CURRENT_DATE ();
	END IF;
END;
//
DELIMITER ;
 
-- Inserindo Instrutores
INSERT INTO Instrutor (nome, especialidade) VALUES
('Carlos Eduardo', 'DevOps & Cloud'),
('Mariana Lima', 'Python & Data Science'),
('Roberto Alves', 'Desenvolvimento Web Fullstack');

-- Inserindo Cursos
INSERT INTO Curso (nome_curso, carga_horaria, vagas_maximas, id_instrutor) VALUES
('Docker & Kubernete', 60, 25, 1),
('Python para Análise de Dados', 80, 30, 2),
('Desenvolvimento Web', 120, 20, 3);

-- Inserindo Alunos
INSERT INTO Aluno (nome, email) VALUES
('Ana Clara Souza', 'ana.souza@email.com'),
('Lucas Gabriel Pereira', 'lucas.pereira@email.com'),
('Fernando Silva', 'fernando.silva@email.com');

-- Inserindo Número de Telefone dos Alunos
INSERT INTO Telefone_Aluno (id_aluno, numero) VALUES
(1, '(11) 98765-4321'),
(1, '(11) 3344-7766'),
(2, '(21) 99887-7665');

-- Inserindo Matriculas
INSERT INTO Matricula (id_aluno, id_curso, data_matricula, status) VALUES
(1, 1, CURRENT_DATE, 'Ativa'),
(1, 2, CURRENT_DATE, 'Ativa'),
(2, 2, CURRENT_DATE, 'Ativa'),
(3, 3, CURRENT_DATE, 'Ativa');

-- TRANSAÇÃO NO MySQL

START TRANSACTION;

-- Passo 1: Inserção de novo aluno
INSERT INTO Aluno (nome, email)
VALUES ('Beatriz Mendes', 'beatriz.mendes@email.com');

-- Passo 2: Registro do número de telefone do novo aluno
INSERT INTO Telefone_Aluno (id_aluno, numero)
VALUES (LAST_INSERT_ID(), '(31) 99123-4567');

-- Passo 3: Efetivação da Matrícula no Curso Python
INSERT INTO Matricula (id_aluno, id_curso, data_matricula, status)
VALUES (LAST_INSERT_ID(), 2, CURRENT_DATE, 'Ativa');

-- Confirmação da Transação
COMMIT;

-- CONSULTA / RELATÓRIO
SELECT
m.id_matricula,
a.nome AS nome_aluno,
a.email AS email_aluno,
c.nome_curso,
i.nome AS nome_instrutor,
m.data_matricula,
m.status
FROM matricula m
INNER JOIN Aluno a ON m.id_aluno = a.id_aluno
INNER JOIN Curso c ON m.id_curso = c.id_curso
INNER JOIN Instrutor i ON c.id_instrutor = i.id_instrutor
ORDER BY m.data_matricula DESC;







 


  

