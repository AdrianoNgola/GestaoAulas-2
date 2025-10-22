# DOCUMENTAÇÃO TÉCNICA
## Sistema de Gestão de Aulas com Quadro Digital Interativo

---

## 1. INTRODUÇÃO

O presente documento estabelece as diretrizes, requisitos e cronograma para o desenvolvimento do **Sistema de Gestão de Aulas**, um projeto solicitado para modernizar o processo de ensino através de uma plataforma digital integrada que combina gestão administrativa, interatividade em tempo real e registro audiovisual de aulas.

Este documento serve como especificação técnica completa e guia de execução para a equipa de desenvolvimento, garantindo alinhamento entre expectativas, prazos e entregas.

---

## 2. APRESENTAÇÃO DO PROJECTO

### 2.1 Visão Geral
O Sistema de Gestão de Aulas é uma aplicação web que permite a gestão completa do ciclo de uma aula, desde o cadastro de participantes até a gravação e armazenamento do conteúdo didático produzido durante a sessão.

### 2.2 Objectivos do Projecto
- Digitalizar o processo de gestão de aulas e presenças
- Proporcionar ambiente de ensino interativo com quadro digital
- Registrar conteúdo das aulas para consulta posterior
- Facilitar o acompanhamento pedagógico através de dados estruturados

### 2.3 Componentes Principais
1. **API RESTful** - Backend robusto desenvolvido em FastAPI
2. **Quadro Digital Interativo** - Integração com Excalidraw para ensino visual
3. **Sistema de Gravação** - Captura sincronizada de áudio, vídeo e tela
4. **Interface Web** - Frontend responsivo para gestão e visualização
5. **Base de Dados** - Armazenamento persistente de todas as informações

---

## 3. CRONOGRAMA DE EXECUÇÃO

**Período Total:** 15 dias úteis  
**Data de Início:** Dia 1 - 20/10/2025  
**Data Actual:** Dia 2 - 21/10/2025  
**Data de Entrega:** Dia 15 - 07/11/2025  
**Dias Restantes:** 13 dias

### 3.1 Faseamento Recomendado

| Fase | Dias | Entregas |
|------|------|----------|
| **Fase 1 - Fundação** | Dias 2-4 | Base de dados, estrutura do projeto, API básica |
| **Fase 2 - Core Features** | Dias 5-9 | CRUD completo, integração Excalidraw, sistema de presenças |
| **Fase 3 - Features Avançadas** | Dias 10-12 | Sistema de gravação, armazenamento de conteúdo |
| **Fase 4 - Interface e Testes** | Dias 13-14 | Frontend completo, testes integrados |
| **Fase 5 - Entrega** | Dia 15 | Apresentação, documentação final, deploy |

---

## 4. INFORMAÇÕES DO PROJECTO

### 4.1 Requisitos Funcionais

#### RF01 - Gestão de Utilizadores
- Cadastro, edição, listagem e remoção de **Professores**
- Cadastro, edição, listagem e remoção de **Alunos**
- Campos mínimos: Nome, Email, Telefone, Número de Identificação

#### RF02 - Gestão de Aulas
- Cadastro de aulas com: Título, Descrição, Data/Hora, Professor responsável
- Associação de alunos a cada aula
- Listagem e detalhamento de aulas

#### RF03 - Controlo de Presenças
- Marcação de presença por aluno em cada aula
- Registro de horário de entrada
- Visualização de relatório de presenças por aula

#### RF04 - Quadro Digital Interativo
- Integração com Excalidraw API
- Permitir desenho, escrita e anotações durante a aula
- Salvar estado do quadro no banco de dados (JSON)

#### RF05 - Gravação de Aulas
- Captura de áudio do professor
- Gravação da tela do quadro digital
- Sincronização entre áudio e vídeo
- Armazenamento do ficheiro de vídeo resultante

#### RF06 - Armazenamento e Recuperação
- Guardar conteúdo do quadro (JSON) associado à aula
- Armazenar metadados da gravação
- Permitir visualização posterior do conteúdo

### 4.2 Requisitos Técnicos

**Backend:**

- Python 3.9+
- FastAPI framework
- SQLAlchemy (ORM)
- PostgreSQL ou SQLite
- Pydantic para validação

**Frontend:**

- HTML5, CSS3, JavaScript ES6+
- Opcional: React.js (se o estagiário tiver conhecimento)
- Integração com Excalidraw
- MediaRecorder API para gravação

**Infraestrutura:**

- Sistema de ficheiros para armazenar vídeos
- Estrutura RESTful para todas as operações
- CORS configurado para comunicação frontend-backend

---

## 5. CHECKLIST DE EXECUÇÃO

### ✅ FASE 1: Configuração e Estrutura Base (Dias 2-4)

**Backend:**
- [ ] Criar ambiente virtual Python
- [x] Instalar dependências (FastAPI, SQLAlchemy, Uvicorn, etc.)
- [x] Estruturar projeto (pastas: models, routes, schemas, database)
- [x] Configurar base de dados e criar conexão
- [x] Implementar models: Professor, Aluno, Aula, Presenca, ConteudoQuadro

**Database:**
- [x] Definir schema da base de dados
- [x] Criar tabelas necessárias
- [x] Estabelecer relacionamentos (foreign keys)
- [x] Testar conexão e operações básicas

**Documentação:**
- [ ] Documentar estrutura do projeto
- [ ] Criar README com instruções de setup
- [ ] Subir a pasta do projecto no github

---

### ✅ FASE 2: Funcionalidades Core (Dias 5-9)

**API - CRUD Professores:**
- [ ] POST /professores - Criar professor
- [ ] GET /professores - Listar todos
- [ ] GET /professores/{id} - Detalhar um professor
- [ ] PUT /professores/{id} - Atualizar professor
- [ ] DELETE /professores/{id} - Remover professor

**API - CRUD Alunos:**
- [ ] POST /alunos - Criar aluno
- [ ] GET /alunos - Listar todos
- [ ] GET /alunos/{id} - Detalhar um aluno
- [ ] PUT /alunos/{id} - Atualizar aluno
- [ ] DELETE /alunos/{id} - Remover aluno

**API - CRUD Aulas:**
- [ ] POST /aulas - Criar aula
- [ ] GET /aulas - Listar aulas
- [ ] GET /aulas/{id} - Detalhar aula
- [ ] PUT /aulas/{id} - Atualizar aula
- [ ] DELETE /aulas/{id} - Remover aula
- [ ] POST /aulas/{id}/alunos - Associar alunos à aula

**API - Presenças:**
- [ ] POST /aulas/{id}/presencas - Marcar presença
- [ ] GET /aulas/{id}/presencas - Listar presenças da aula
- [ ] PUT /presencas/{id} - Atualizar presença

**Testes:**
- [ ] Testar todos os endpoints com Postman/Insomnia
- [ ] Validar regras de negócio
- [ ] Documentar API com Swagger (automático do FastAPI)

---

### ✅ FASE 3: Features Avançadas (Dias 10-12)

**Integração Excalidraw:**
- [ ] Estudar documentação do Excalidraw
- [ ] Integrar biblioteca no frontend
- [ ] Criar endpoint POST /aulas/{id}/quadro para salvar conteúdo
- [ ] Criar endpoint GET /aulas/{id}/quadro para recuperar conteúdo
- [ ] Testar salvamento e carregamento do quadro

**Sistema de Gravação:**
- [ ] Implementar MediaRecorder API no frontend
- [ ] Capturar stream da tela (quadro)
- [ ] Capturar stream de áudio do microfone
- [ ] Combinar streams em gravação única
- [ ] Criar endpoint POST /aulas/{id}/gravacao para upload
- [ ] Armazenar ficheiro de vídeo no servidor
- [ ] Salvar metadados da gravação na BD

**Armazenamento:**
- [ ] Criar estrutura de pastas para ficheiros
- [ ] Implementar lógica de nomes únicos (UUID)
- [ ] Endpoint GET /aulas/{id}/gravacao para download/stream

---

### ✅ FASE 4: Frontend Completo (Dias 13-14)

**Interface de Gestão:**
- [ ] Página de listagem de professores com ações (adicionar, editar, remover)
- [ ] Página de listagem de alunos com ações
- [ ] Página de listagem de aulas com ações
- [ ] Formulários de cadastro e edição

**Interface de Aula:**
- [ ] Página da aula com quadro Excalidraw
- [ ] Botão para iniciar/parar gravação
- [ ] Interface de marcação de presenças
- [ ] Visualização de alunos da aula

**Funcionalidades Adicionais:**
- [ ] Visualização de aulas gravadas
- [ ] Relatório de presenças
- [ ] Design responsivo básico
- [ ] Feedback visual de operações (loading, success, error)

**Integração:**
- [ ] Conectar todas as páginas à API
- [ ] Implementar tratamento de erros
- [ ] Validação de formulários no frontend
- [ ] Testes de usabilidade

---

### ✅ FASE 5: Finalização (Dia 15)

- [ ] Testes finais end-to-end
- [ ] Correção de bugs identificados
- [ ] Documentação do código
- [ ] README atualizado com instruções de uso
- [ ] Preparação da apresentação
- [ ] Deploy (se aplicável)

---

## 6. INFORMAÇÕES ADICIONAIS

### 6.1 Estrutura de Pastas Sugerida

```
projeto-gestao-aulas/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── professor.py
│   │   │   ├── aluno.py
│   │   │   ├── aula.py
│   │   │   └── presenca.py
│   │   ├── schemas/
│   │   │   └── ... (Pydantic schemas)
│   │   ├── routes/
│   │   │   ├── professores.py
│   │   │   ├── alunos.py
│   │   │   ├── aulas.py
│   │   │   └── presencas.py
│   │   └── utils/
│   ├── storage/
│   │   ├── videos/
│   │   └── quadros/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   ├── api.js
│   │   ├── main.js
│   │   └── quadro.js
│   └── pages/
│       ├── professores.html
│       ├── alunos.html
│       └── aulas.html
└── README.md
```

### 6.2 Tecnologias e Bibliotecas Recomendadas

**Python (Backend):**
```
fastapi
uvicorn[standard]
sqlalchemy
pydantic
python-multipart
python-dotenv
psycopg2-binary (PostgreSQL) ou sqlite3
```

**JavaScript (Frontend):**
- Excalidraw: `@excalidraw/excalidraw`
- Axios ou Fetch API para requisições HTTP
- (Opcional) React.js + Vite

### 6.3 Recursos de Apoio

- **Documentação FastAPI:** https://fastapi.tiangolo.com/
- **Excalidraw API:** https://docs.excalidraw.com/
- **MediaRecorder API:** https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder
- **SQLAlchemy:** https://docs.sqlalchemy.org/

### 6.4 Boas Práticas Esperadas

1. **Código Limpo:** Nomes de variáveis descritivos, funções com responsabilidade única
2. **Versionamento:** Commits frequentes com mensagens claras
3. **Tratamento de Erros:** Try/catch adequados, mensagens de erro informativas
4. **Validação:** Validar dados no backend e frontend
5. **Segurança:** Não expor informações sensíveis, validar inputs do utilizador
6. **Documentação:** Comentários onde necessário, README completo

---

## 7. DINÂMICA E MÉTODO DE AVALIAÇÃO

### 7.1 Critérios de Avaliação

A avaliação do projeto será realizada através de análise objetiva baseada nos seguintes critérios:

| Critério | Peso | Descrição |
|----------|------|-----------|
| **Funcionalidades Core** | 35% | Todos os CRUDs funcionando corretamente |
| **Integração Excalidraw** | 20% | Quadro funcional com salvamento e recuperação |
| **Sistema de Gravação** | 20% | Gravação de áudio/vídeo operacional |
| **Qualidade do Código** | 10% | Organização, boas práticas, legibilidade |
| **Interface do Utilizador** | 10% | Usabilidade e apresentação do frontend |
| **Documentação** | 5% | README e comentários de código |

### 7.2 Níveis de Completude

**Excelente (90-100%):**

- Todas as funcionalidades implementadas e funcionais
- Código bem estruturado e documentado
- Interface intuitiva e responsiva
- Sistema de gravação robusto

**Bom (75-89%):**
- Funcionalidades principais implementadas
- Pequenos bugs não críticos
- Interface funcional
- Gravação básica operacional

**Satisfatório (60-74%):**
- CRUDs completos
- Quadro digital funcional (sem gravação)
- Interface básica funcional

**Insuficiente (<60%):**
- Funcionalidades incompletas
- Bugs críticos impedindo uso básico

### 7.3 Checkpoints de Acompanhamento

- **Dia 4:** Revisão da estrutura base e base de dados
- **Dia 9:** Demonstração dos CRUDs e sistema de presenças
- **Dia 12:** Apresentação do quadro e gravação
- **Dia 15:** Entrega e apresentação final

---

## 8. HABILIDADES DO ESTAGIÁRIO

### 8.1 Competências Técnicas a Desenvolver

#### 8.1.1 Backend Development
- **Arquitetura de APIs RESTful:** Compreensão profunda de endpoints, métodos HTTP, status codes
- **ORM e Modelagem de Dados:** Utilização do SQLAlchemy para mapear objetos e estruturar bases de dados relacionais
- **Validação e Serialização:** Uso de Pydantic para garantir integridade de dados
- **Gestão de Ficheiros:** Upload, armazenamento e servir ficheiros no servidor

#### 8.1.2 Frontend Development
- **Integração com APIs:** Consumo de endpoints RESTful, tratamento de respostas assíncronas
- **Manipulação de DOM:** JavaScript vanilla para interatividade
- **Web APIs Avançadas:** MediaRecorder, Canvas, Screen Capture
- **Integração de Bibliotecas:** Trabalhar com bibliotecas de terceiros (Excalidraw)

#### 8.1.3 Desenvolvimento Full-Stack
- **Visão End-to-End:** Compreender fluxo completo desde frontend até persistência em BD
- **Debugging:** Identificar e resolver problemas em múltiplas camadas
- **Comunicação Cliente-Servidor:** CORS, requisições HTTP, formato de dados

#### 8.1.4 Ferramentas e Práticas
- **Controlo de Versão:** Git para gestão de código
- **Ambientes Virtuais:** Isolamento de dependências Python
- **Testes de API:** Postman para validação de endpoints
- **Documentação Automática:** Swagger/OpenAPI

### 8.2 Competências Profissionais (Soft Skills)

#### 8.2.1 Gestão de Projeto
- **Planeamento:** Dividir projeto grande em tarefas executáveis
- **Priorização:** Identificar o que é crítico vs. desejável
- **Gestão de Tempo:** Cumprir prazos em ambiente profissional
- **Autonomia:** Pesquisar soluções e tomar decisões técnicas

#### 8.2.2 Comunicação Técnica
- **Documentação:** Escrever documentação clara e útil
- **Apresentação:** Comunicar decisões técnicas e demonstrar trabalho
- **Pedido de Ajuda:** Saber quando e como solicitar apoio

#### 8.2.3 Resolução de Problemas
- **Análise:** Decompor problemas complexos
- **Pesquisa:** Utilizar documentação oficial e recursos online
- **Debugging Sistemático:** Abordagem metódica para identificar bugs
- **Adaptabilidade:** Ajustar planos quando confrontado com obstáculos

### 8.3 Experiência Profissional Real

Este projeto simula condições reais de trabalho em desenvolvimento de software:

✓ **Especificações de Cliente:** Trabalhar a partir de requisitos definidos  
✓ **Prazos Apertados:** Gerir tempo e expectativas  
✓ **Stack Tecnológico Definido:** Adaptar-se a escolhas técnicas estabelecidas  
✓ **Entrega de Valor:** Focar em funcionalidades que importam  
✓ **Qualidade do Código:** Equilibrar velocidade e manutenibilidade  
✓ **Apresentação de Resultados:** Demonstrar trabalho a stakeholders  

### 8.4 Preparação para o Mercado

Ao concluir este projeto com sucesso, o estagiário terá:

- **Portfolio:** Projeto completo demonstrável
- **Experiência Prática:** Desenvolvimento de aplicação real com múltiplas integrações
- **Conhecimento de Stack:** Experiência com tecnologias muito procuradas no mercado
- **Metodologia:** Vivência de processo de desenvolvimento profissional
- **Confiança:** Capacidade comprovada de entregar soluções completas

---

## 9. CONCLUSÃO

O Sistema de Gestão de Aulas representa um desafio técnico significativo e uma oportunidade única de crescimento profissional. Em 15 dias, o estagiário terá a possibilidade de aplicar conhecimentos teóricos, adquirir novas competências e, mais importante, vivenciar o ritmo e as exigências do desenvolvimento profissional de software.

Este projeto não é apenas sobre código funcional - é sobre desenvolver a mentalidade, a disciplina e as habilidades que distinguem um programador júnior de um desenvolvedor profissional. A capacidade de receber requisitos, planejar execução, implementar soluções, resolver problemas e entregar resultados dentro do prazo são competências fundamentais que transcendem tecnologias específicas.

Encorajamos o estagiário a encarar este desafio com seriedade, curiosidade e perseverança. Erros farão parte do processo - o importante é aprender com eles e continuar avançando. Ao final destes 15 dias, independentemente do nível de completude alcançado, a experiência adquirida será inestimável para a carreira profissional.

**A equipa de orientação está disponível para suporte técnico e esclarecimento de dúvidas. O sucesso deste projeto depende do compromisso, dedicação e proatividade do estagiário.**

---

**Documento preparado em:** 21 de Outubro de 2025  
**Validade:** Projeto em execução  
**Revisão:** Versão 1.0

---

## ANEXOS

### Anexo A - Comandos Úteis

**Setup Backend:**
```bash
python -m venv venv
venv\Scripts\activate     # Windows
pip install -r requirements.txt # Ou use o py -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Executar Frontend:**

```bash
# Servidor simples Python
python -m http.server 8000
# Ou com Node.js
npx serve frontend/
```

### Anexo B - Estrutura de Dados Exemplo

**Professor:**
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@escola.com",
  "telefone": "+244 923 456 789"
}
```

**Aula:**
```json
{
  "id": 1,
  "titulo": "Introdução ao Python",
  "descricao": "Aula sobre conceitos básicos",
  "data_hora": "2025-10-22T14:00:00",
  "professor_id": 1,
  "conteudo_quadro": {...},
  "url_gravacao": "/storage/videos/aula-1-uuid.webm"
}
```

---

**FIM DO DOCUMENTO**