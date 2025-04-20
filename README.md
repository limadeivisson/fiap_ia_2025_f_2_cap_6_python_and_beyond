
# 🌿 Projeto FIAP – Capítulo 1: Um Mapa do Tesouro

[![GitHub](https://img.shields.io/badge/Grupo-FarmTech%20Solutions-green)](https://github.com/LucianBinner/fiap_ia_2025_f_2_cap_1_treasure_map)
[![Turma](https://img.shields.io/badge/Turma-1TIAOB%2F2025-blue)]()
[![Status](https://img.shields.io/badge/Status-Concluído-success)]()

## 💡 Descrição

Este projeto foi desenvolvido como parte da atividade avaliativa da FIAP para a Fase 2, capítulo 1 "Um Mapa do Tesouro" na disciplina de Banco de Dados. A proposta simula um sistema de monitoramento agrícola com sensores de solo e automação para irrigação e aplicação de nutrientes.

---

## 🎯 Objetivos

- Coletar dados de sensores de umidade, pH e nutrientes (NPK)
- Otimizar o uso de água e fertilizantes por meio de um sistema inteligente
- Aplicar os conceitos de modelagem de dados (MER e DER)
- Construir um banco de dados relacional com integridade referencial

---

## 📊 MER (Modelo Entidade Relacionamento)

As principais entidades do sistema são:
- Sensor
- Talhao
- Cultura
- Leitura
- AplicacaoAgua
- AplicacaoNutriente

As cardinalidades entre as entidades foram analisadas com base nas regras de negócio da agricultura digital.

## 🗃️ Entidades e Atributos

### `Sensor`
- id_sensor (PK, INT)
- tipo (VARCHAR(10)) — S1, S2, S3
- modelo (VARCHAR(50))
- data_instalacao (DATE)

### `Talhao`
- id_talhao (PK, INT)
- nome (VARCHAR(50))
- area (NUMBER)
- localizacao_gps (VARCHAR(100))
- id_cultura (FK, INT)

### `Cultura`
- id_cultura (PK, INT)
- nome (VARCHAR(50))
- ph_minimo (NUMBER)
- ph_maximo (NUMBER)
- umidade_minima (NUMBER)
- nutriente_p_minimo (NUMBER)
- nutriente_k_minimo (NUMBER)

### `Leitura`
- id_leitura (PK, INT)
- id_sensor (FK, INT)
- id_talhao (FK, INT)
- data_hora (DATE)
- umidade (NUMBER)
- ph (NUMBER)
- fosforo (NUMBER)
- potassio (NUMBER)

### `AplicacaoAgua`
- id_aplicacao_agua (PK, INT)
- id_talhao (FK, INT)
- data_hora (DATE)
- quantidade_aplicada (NUMBER)

### `AplicacaoNutriente`
- id_aplicacao_nutriente (PK, INT)
- id_talhao (FK, INT)
- data_hora (DATE)
- tipo_nutriente (VARCHAR(50))
- quantidade_aplicada (NUMBER)

---

## 🔁 Relacionamentos

- **Sensor** 1:N **Leitura**
- **Talhao** 1:N **Leitura**
- **Cultura** 1:N **Talhao**
- **Talhao** 1:N **AplicacaoAgua**
- **Talhao** 1:N **AplicacaoNutriente**

📄 Detalhes completos no arquivo `farmtech_modelo_corrigido.sql`.

---

## 🧩 DER (Diagrama Entidade-Relacionamento)

O DER foi modelado no Oracle SQL Developer Data Modeler e está disponível em:
- 📁 `logico_cap1_um_mapa_do_tesouro.dmd`
- 🖼️ `der_cap1_um_mapa_do_tesouro.png`

---

## 🗂️ Estrutura do Repositório

```
📁 fiap_ia_2025_f_2_cap_1_treasure_map/
├── README.md
├── cap1_um_mapa_do_tesouro.sql
├── der_cap1_um_mapa_do_tesouro.dmd
├── der_cap1_um_mapa_do_tesouro.png
└── Grupo82_1TIAOB2025_Fase 2 - Capítulo 1 Um Mapa do Tesouro.pdf
```

---

## 🧠 Como abrir os arquivos `.dmd` e `.sql`

### Abrir `.dmd`
1. Instale o Oracle SQL Developer Data Modeler: [Download](https://www.oracle.com/br/database/sqldeveloper/technologies/sql-data-modeler/)
2. Vá em `File > Open` e selecione `logico_cap1_um_mapa_do_tesouro.dmd`

### Executar `.sql`
1. Utilize Oracle SQL Developer, DBeaver ou outro client SQL
2. Execute o script `cap1_um_mapa_do_tesouro.sql` para criar as tabelas no banco

---

## 👥 Integrantes do Grupo

- Deivisson Gonçalves Lima – RM565095 – deivisson.engtele@gmail.com  
- Lucian Paiva Binner – RM563350 – lucian.binner@hotmail.com
- Omar Calil Abrão Mustafá Assem – RM561375 – ocama12@gmail.com  
- Paulo Henrique de Sousa – RM564262 – pauloo.sousa16@outlook.com  
- Renan Danilo dos Santos Pereira – RM566175 – renansantos4978@gmail.com  

---

## ✅ Status

Entrega realizada com sucesso na plataforma FIAP via PDF com repositório completo em GitHub.
