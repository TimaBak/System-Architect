# Соответствие справочника книге

**Первоисточник:** Mark Richards, Neal Ford. *Fundamentals of Software Architecture: A Modern Engineering Approach*, Second Edition, O’Reilly, 2025. Русский перевод: *Фундаментальный подход к программной архитектуре. Паттерны, свойства, проверенные методы*, 2026, 544 с.

Таблица указывает **начальные страницы в русском издании**, совпадающие с нумерацией предоставленного PDF. Это навигация к первоисточнику, а не его воспроизведение.

| Глава | Название | Стр. | Основная тема нашего справочника |
|---:|---|---:|---|
| 1 | Введение | 26 | [Архитектурное мышление](../docs/01-foundations/architecture-thinking.md) |
| 2 | Архитектурное мышление | 40 | [Архитектурное мышление](../docs/01-foundations/architecture-thinking.md) |
| 3 | Модульность | 60 | [Модульность](../docs/01-foundations/modularity.md) |
| 4 | Определение свойств архитектуры | 79 | [Свойства](../docs/01-foundations/quality-attributes.md) |
| 5 | Выбор архитектурных свойств | 92 | [Свойства](../docs/01-foundations/quality-attributes.md) |
| 6 | Измерение и управление свойствами | 106 | [Функции пригодности](../docs/04-decisions/risks-and-fitness-functions.md) |
| 7 | Область действия свойств | 120 | [Свойства](../docs/01-foundations/quality-attributes.md) |
| 8 | Компонентно-ориентированное мышление | 132 | [Компоненты](../docs/01-foundations/component-design.md) |
| 9 | Основные понятия | 154 | [Стили](../docs/02-styles/README.md) |
| 10 | Многоуровневая архитектура | 177 | [Layered](../docs/02-styles/layered.md) |
| 11 | Модульный монолит | 190 | [Modular Monolith](../docs/02-styles/modular-monolith.md) |
| 12 | Конвейерная архитектура | 205 | [Pipeline](../docs/02-styles/pipeline.md) |
| 13 | Микроядерная архитектура | 218 | [Microkernel](../docs/02-styles/microkernel.md) |
| 14 | Архитектура на основе сервисов | 235 | [Service-based](../docs/02-styles/service-based.md) |
| 15 | Архитектура, управляемая событиями | 254 | [Event-driven](../docs/02-styles/event-driven.md) |
| 16 | Архитектура на основе пространства | 313 | [Space-based](../docs/02-styles/space-based.md) |
| 17 | Оркестрированная сервис-ориентированная архитектура | 346 | [Orchestrated SOA](../docs/02-styles/orchestrated-soa.md) |
| 18 | Микросервисы | 362 | [Microservices](../docs/02-styles/microservices.md) |
| 19 | Выбор стиля | 391 | [Выбор](../docs/04-decisions/architecture-selection.md) |
| 20 | Паттерны архитектуры | 404 | [Паттерны](../docs/03-patterns/README.md) |
| 21 | Архитектурные решения | 418 | [ADR](../docs/04-decisions/adr.md) |
| 22 | Архитектурные риски | 437 | [Риски](../docs/04-decisions/risks-and-fitness-functions.md) |
| 23 | Диаграммы архитектуры | 455 | [Документация](../docs/05-practice/documentation-and-communication.md) |
| 24 | Эффективная команда | 464 | [Команды](../docs/05-practice/teams-ai-and-governance.md) |
| 25 | Лидерство и переговоры | 485 | [Команды](../docs/05-practice/teams-ai-and-governance.md) |
| 26 | Пересечения архитектуры | 503 | [Работа архитектора](../docs/05-practice/architecture-workflow.md) |
| 27 | Законы архитектуры ПО | 522 | [Мышление](../docs/01-foundations/architecture-thinking.md) |

### Как отличать первоисточник от расширений

- Помета **«по главе N»** означает тематическую опору на книгу, не текстуальное копирование.
- Образцы API, SLO, таблицы действий, примеры доменных модулей, чек-листы и шаблоны здесь — **оригинальный прикладной материал**, если явно не указано иное.
- Конкретные продукты (например, Kafka, PostgreSQL, Kubernetes) — **иллюстрации применения**, не обязательные рекомендации авторов.
- Каждое архитектурное решение должно проверяться на контексте проекта, даже если аналогичный подход упоминается в литературе.

**Права:** содержание и иллюстрации книги принадлежат их правообладателям. PDF, сканы и оригинальные рисунки намеренно не загружаются в публичный репозиторий.
