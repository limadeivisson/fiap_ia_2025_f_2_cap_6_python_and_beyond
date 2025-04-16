CREATE TABLE area (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    hectar NUMBER(10,2)
);

CREATE TABLE cultura (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    coeficiente_kc NUMBER(4,2),
    profundidade_raiz_cm NUMBER(5),
    consumo_hidrico_diario_l_m2 NUMBER(6,2)
);

CREATE TABLE plantio (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    area_id NUMBER NOT NULL,
    cultura_id NUMBER NOT NULL,
    data_plantio DATE NOT NULL,
    fase_atual VARCHAR2(50),
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

CREATE TABLE recomendacao_irrigacao (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    irrigacao_id NUMBER NOT NULL,
    status VARCHAR2(50),
    feedback VARCHAR2(255),
    CONSTRAINT fk_irrigacao_id FOREIGN KEY (irrigacao_id) REFERENCES irrigacao(id) ON DELETE CASCADE
);
