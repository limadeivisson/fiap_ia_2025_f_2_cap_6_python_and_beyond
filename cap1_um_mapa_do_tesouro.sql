
-- DER - der_fase2_cap1_um_mapa_do_tesouro

-- Entidade: Sensor
CREATE TABLE Sensor (
    id_sensor INTEGER PRIMARY KEY,
    tipo VARCHAR2(10),
    modelo VARCHAR2(50),
    data_instalacao DATE
);

-- Entidade: Cultura
CREATE TABLE Cultura (
    id_cultura INTEGER PRIMARY KEY,
    nome VARCHAR2(50),
    ph_minimo NUMBER,
    ph_maximo NUMBER,
    umidade_minima NUMBER,
    nutriente_p_minimo NUMBER,
    nutriente_k_minimo NUMBER
);

-- Entidade: Talhao
CREATE TABLE Talhao (
    id_talhao INTEGER PRIMARY KEY,
    nome VARCHAR2(50),
    area NUMBER,
    localizacao_gps VARCHAR2(100),
    id_cultura INTEGER,
    FOREIGN KEY (id_cultura) REFERENCES Cultura(id_cultura)
);

-- Entidade: Leitura
CREATE TABLE Leitura (
    id_leitura INTEGER PRIMARY KEY,
    id_sensor INTEGER,
    id_talhao INTEGER,
    data_hora DATE,
    umidade NUMBER,
    ph NUMBER,
    fosforo NUMBER,
    potassio NUMBER,
    FOREIGN KEY (id_sensor) REFERENCES Sensor(id_sensor),
    FOREIGN KEY (id_talhao) REFERENCES Talhao(id_talhao)
);

-- Entidade: AplicacaoAgua
CREATE TABLE AplicacaoAgua (
    id_aplicacao_agua INTEGER PRIMARY KEY,
    id_talhao INTEGER,
    data_hora DATE,
    quantidade_aplicada NUMBER,
    FOREIGN KEY (id_talhao) REFERENCES Talhao(id_talhao)
);

-- Entidade: AplicacaoNutriente
CREATE TABLE AplicacaoNutriente (
    id_aplicacao_nutriente INTEGER PRIMARY KEY,
    id_talhao INTEGER,
    data_hora DATE,
    tipo_nutriente VARCHAR2(50),
    quantidade_aplicada NUMBER,
    FOREIGN KEY (id_talhao) REFERENCES Talhao(id_talhao)
);
