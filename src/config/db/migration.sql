SELECT table_name FROM user_tables;

select * from AREA;
select * from CULTURA;
select * from PLANTIO;
select * from IRRIGACAO;

DROP TABLE IRRIGACAO;
DROP TABLE PLANTIO;
DROP TABLE CULTURA;
DROP TABLE AREA;

CREATE TABLE area (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    localizacao VARCHAR2(200) NOT NULL,
    hectar NUMBER(10,2)
);

CREATE TABLE cultura (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    consumo_hidrico_diario_l_m2 NUMBER(6,2)
);

CREATE TABLE plantio (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    observacao VARCHAR2(100) NOT NULL,
    area_id NUMBER NOT NULL,
    cultura_id NUMBER NOT NULL,
    data_plantio DATE NOT NULL,
    CONSTRAINT fk_area_id FOREIGN KEY (area_id) REFERENCES area(id) ON DELETE CASCADE,
    CONSTRAINT fk_cultura_id FOREIGN KEY (cultura_id) REFERENCES cultura(id) ON DELETE CASCADE
);

CREATE TABLE irrigacao (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    plantio_id NUMBER NOT NULL,
    data_irrigacao DATE NOT NULL,
    volume_agua_l NUMBER(10,2),
    CONSTRAINT fk_plantio_id FOREIGN KEY (plantio_id) REFERENCES plantio(id) ON DELETE CASCADE
);

INSERT INTO area (nome, localizacao, hectar) VALUES ('Fazenda São João', 'Zona Rural - MG', 25.50);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Sítio Verde Vale', 'Interior de SP', 12.30);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Chácara Bela Vista', 'Sul de GO', 8.00);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Fazenda Sol Nascente', 'Norte de MT', 32.75);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Sítio Santa Clara', 'Oeste da BA', 15.10);

INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Milho', 5.20);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Soja', 4.80);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Cana-de-açúcar', 6.50);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Feijão', 3.90);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Algodão', 5.75);

INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 1', 'Início da safra', 1, 1, DATE '2024-11-01');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 2', 'Boa germinação', 2, 2, DATE '2024-11-05');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 3', 'Chuva leve', 3, 3, DATE '2024-11-10');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 4', 'Aplicado fertilizante', 4, 4, DATE '2024-11-12');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 5', 'Replantio parcial', 5, 5, DATE '2024-11-15');

INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (1, DATE '2024-11-02', 1500.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (1, DATE '2024-11-03', 1600.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (2, DATE '2024-11-06', 1200.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (3, DATE '2024-11-11', 1350.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (4, DATE '2024-11-13', 1450.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (5, DATE '2024-11-16', 1550.00);