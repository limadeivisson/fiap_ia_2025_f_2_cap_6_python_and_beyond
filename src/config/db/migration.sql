SELECT table_name FROM user_tables;

select * from AREA;
select * from CULTURA;
select * from PLANTIO;
select * from IRRIGACAO;
select * from FEEDBACK;

DROP TABLE FEEDBACK;
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

INSERT INTO area (nome, localizacao, hectar) VALUES ('Fazenda São João', 'Zona Rural - MG', 25.50);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Sítio Verde Vale', 'Interior de SP', 12.30);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Chácara Bela Vista', 'Sul de GO', 8.00);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Fazenda Sol Nascente', 'Norte de MT', 32.75);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Sítio Santa Clara', 'Oeste da BA', 15.10);

CREATE TABLE cultura (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    consumo_hidrico_diario_l_m2 NUMBER(6,2)
);

INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Milho', 5.20);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Soja', 4.80);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Cana-de-açúcar', 6.50);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Feijão', 3.90);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Algodão', 5.75);

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

INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 1', 'Início da safra', 1, 1, DATE '2024-11-01');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 2', 'Boa germinação', 2, 2, DATE '2024-11-05');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 3', 'Chuva leve', 3, 3, DATE '2024-11-10');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 4', 'Aplicado fertilizante', 4, 4, DATE '2024-11-12');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 5', 'Replantio parcial', 5, 5, DATE '2024-11-15');

CREATE TABLE irrigacao (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    plantio_id NUMBER NOT NULL,
    data_irrigacao DATE NOT NULL,
    volume_agua_l NUMBER(10,2),
    CONSTRAINT fk_plantio_id FOREIGN KEY (plantio_id) REFERENCES plantio(id) ON DELETE CASCADE
);

INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (1, DATE '2024-11-02', 1500.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (1, DATE '2024-11-03', 1600.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (2, DATE '2024-11-06', 1200.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (3, DATE '2024-11-11', 1350.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (4, DATE '2024-11-13', 1450.00);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (5, DATE '2024-11-16', 1550.00);

CREATE TABLE feedback (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cultura_id NUMBER NOT NULL,
    message_feedback VARCHAR2(400) NOT NULL,
    tips VARCHAR2(400) NOT NULL,
    percent NUMBER NOT NULL,
    CONSTRAINT fk_feedback_cultura_id FOREIGN KEY (cultura_id) REFERENCES cultura(id) ON DELETE CASCADE
);

-- Cultura 1: Milho
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Irrigação adequada ao longo da semana.', 'Continue com o monitoramento diário do solo.', 94);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Volume de água abaixo do ideal.', 'Ajuste o sistema para manter 5.2 L/m²/dia.', 78);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Desperdício de água detectado em alguns dias.', 'Evite irrigação após chuvas.', 82);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Consumo hídrico estável e eficiente.', 'Parabéns pelo controle hídrico!', 96);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Início promissor, mas com variações.', 'Verifique os aspersores para distribuição uniforme.', 88);

-- Cultura 2: Soja
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Boa performance hídrica.', 'Mantenha os 4.8 L/m² por dia com pequenas variações.', 91);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Déficit hídrico registrado na segunda semana.', 'Revise a frequência de irrigação.', 76);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Uso eficiente dos recursos hídricos.', 'Continue o acompanhamento com sensores de umidade.', 89);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Oscilação de consumo detectada.', 'Ajuste nos dias mais quentes.', 83);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Excelente manejo de irrigação.', 'Modelo atual está bem equilibrado.', 97);

-- Cultura 3: Cana-de-açúcar
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Irrigação próxima do ideal.', 'Atenção ao consumo diário de 6.5 L/m².', 88);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Excesso leve de irrigação registrado.', 'Reduza um pouco em dias nublados.', 81);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Consumo hídrico bem distribuído.', 'Continue o controle por setor da área.', 93);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Período de seca compensado com eficiência.', 'Bom uso de irrigação complementar.', 90);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Necessidade de correção detectada.', 'Aumentar irrigação nas manhãs.', 75);

-- Cultura 4: Feijão
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Irrigação aquém do necessário.', 'Refaça o cálculo com base nos dados climáticos.', 70);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Boa regularidade de irrigação.', 'Continue com o atual cronograma.', 90);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Oscilação prejudicial no consumo.', 'Padronize os horários de irrigação.', 76);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Atenção: variações por setor da área.', 'Considere setorização inteligente.', 80);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Desempenho hídrico ideal.', 'Manejo muito bem executado.', 94);

-- Cultura 5: Algodão
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Controle de irrigação eficiente.', 'Continue observando o volume por metro quadrado.', 92);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Pequeno excesso identificado.', 'Ajuste o tempo de irrigação noturno.', 79);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Níveis abaixo do ideal.', 'Melhorar frequência nos dias secos.', 74);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Consistência nos volumes irrigados.', 'Muito bom, mantenha o padrão atual.', 95);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Oscilações sazonais compensadas corretamente.', 'Controle climático bem feito.', 87);