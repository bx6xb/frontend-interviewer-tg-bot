ts_questions = {
  1: {
    "question": "Что такое TypeScript и зачем он нужен?",
    "answer": "TypeScript — это надмножество JavaScript, которое добавляет статическую типизацию. Он позволяет находить ошибки на этапе компиляции, улучшает автодополнение в IDE и повышает читаемость и поддержку кода."
  },
  2: {
    "question": "Какие преимущества TypeScript перед JavaScript?",
    "answer": "Основные преимущества TypeScript — это статическая типизация, улучшенное автодополнение, возможность использовать современные возможности JavaScript, поддержка интерфейсов и типов, а также обнаружение ошибок на этапе компиляции."
  },
  3: {
    "question": "Какие основные типы данных есть в TypeScript?",
    "answer": "Основные типы данных в TypeScript: `number`, `string`, `boolean`, `array`, `tuple`, `enum`, `any`, `void`, `never`, `null`, `undefined`, `object`, а также специализированные типы, такие как `unknown`."
  },
  4: {
    "question": "Что такое any, unknown, never и в чём их различие?",
    "answer": "`any` — это тип, который может быть чем угодно и отключает типизацию. `unknown` аналогичен `any`, но требует явной проверки типа перед использованием. `never` — это тип, который обозначает значение, которое никогда не существует (например, функции, которые выбрасывают ошибки)."
  },
  5: {
    "question": "Чем null отличается от undefined в TypeScript?",
    "answer": "`null` — это значение, которое явно указывает на отсутствие значения, в то время как `undefined` означает, что переменная была объявлена, но ей не присвоено значение. В TypeScript их поведение также зависит от конфигурации строгой типизации."
  },
  6: {
    "question": "Как объявить переменную с конкретным типом?",
    "answer": "Переменную с конкретным типом можно объявить с помощью аннотации типа: `let name: string = 'John';` или `const age: number = 30;`."
  },
  7: {
    "question": "Что такое type inference (выведение типов)?",
    "answer": "Type inference — это механизм TypeScript, который автоматически определяет тип переменной, функции или выражения на основе её значений, без явной аннотации типа."
  },
  8: {
    "question": "Как работает строгая типизация в TypeScript?",
    "answer": "Строгая типизация в TypeScript запрещает выполнение операций с несовместимыми типами. Например, нельзя сложить строку с числом без явного преобразования типов."
  },
  9: {
    "question": "Можно ли отключить строгую типизацию?",
    "answer": "Да, можно отключить строгую типизацию, изменив настройки в `tsconfig.json`, установив флаг `strict` в `false`."
  },
  10: {
    "question": "Как включить TypeScript в проекте?",
    "answer": "Чтобы включить TypeScript в проект, нужно установить TypeScript с помощью `npm install typescript`, создать файл `tsconfig.json`, а затем изменить расширение файлов с `.js` на `.ts` или `.tsx`."
  },
  11: {
    "question": "Как задать тип для аргументов функции?",
    "answer": "Типы для аргументов функции задаются в её сигнатуре: `function greet(name: string): void {}`."
  },
  12: {
    "question": "Как задать возвращаемый тип функции?",
    "answer": "Тип возвращаемого значения функции указывается после списка параметров: `function add(a: number, b: number): number { return a + b; }`."
  },
  13: {
    "question": "Как сделать необязательные параметры в функции?",
    "answer": "Необязательные параметры функции указываются с помощью оператора `?`: `function greet(name?: string) {}`."
  },
  14: {
    "question": "Как задать параметры по умолчанию?",
    "answer": "Параметры по умолчанию задаются с использованием значения после знака равенства: `function greet(name: string = 'Guest') {}`."
  },
  15: {
    "question": "Что такое перегрузка функций в TypeScript?",
    "answer": "Перегрузка функций в TypeScript позволяет создавать несколько сигнатур для одной функции, где одна и та же функция может принимать разные типы аргументов и возвращать разные типы значений в зависимости от входных данных."
  },
  16: {
    "question": "Как описать объектный тип?",
    "answer": "Объектный тип описывается с помощью фигурных скобок, внутри которых перечисляются свойства и их типы: `let person: { name: string; age: number; } = { name: 'John', age: 30 };`."
  },
  17: {
    "question": "Чем интерфейсы отличаются от типов (type vs interface)?",
    "answer": "Интерфейсы (`interface`) и типы (`type`) в TypeScript похожи, но интерфейсы предназначены для описания структуры объектов, а типы могут использоваться для описания любых значений, включая примитивы, объединения и пересечения типов. Интерфейсы могут расширять другие интерфейсы, а типы — нет."
  },
  18: {
    "question": "Можно ли расширять интерфейсы и типы?",
    "answer": "Интерфейсы можно расширять с помощью ключевого слова `extends`, а типы — с помощью оператора пересечения `&`."
  },
  19: {
    "question": "Как описать массив в TypeScript?",
    "answer": "Массив в TypeScript можно описать с помощью типа элемента в квадратных скобках: `let numbers: number[] = [1, 2, 3];` или используя тип `Array`: `let numbers: Array<number> = [1, 2, 3];`."
  },
  20: {
    "question": "Как работает readonly для объектов и массивов?",
    "answer": "`readonly` используется для того, чтобы сделать свойства объектов или элементы массива неизменяемыми. Например, `let arr: readonly number[] = [1, 2, 3];` или `let person: { readonly name: string } = { name: 'John' };`."
  },
  21: {
    "question": "Что такое дженерики в TypeScript?",
    "answer": "Дженерики (generics) в TypeScript — это механизмы, позволяющие создавать компоненты, функции, классы или интерфейсы, которые могут работать с любыми типами данных, при этом сохраняя типовую безопасность. Это позволяет писать более гибкий и повторно используемый код."
  },
  22: {
    "question": "Как создать обобщённую (generic) функцию?",
    "answer": "Обобщённую функцию можно создать, указав тип-параметр в угловых скобках: `function identity<T>(arg: T): T { return arg; }`. Тип `T` будет заменён на тип аргумента, который передан при вызове функции."
  },
  23: {
    "question": "Как задать несколько параметров-типов?",
    "answer": "Можно задать несколько параметров-типов, перечислив их через запятую: `function merge<T, U>(obj1: T, obj2: U): T & U { return { ...obj1, ...obj2 }; }`. В данном примере `T` и `U` — два типа, которые могут быть использованы в функции."
  },
  24: {
    "question": "Как использовать ограничения (extends) в дженериках?",
    "answer": "Ограничения с помощью `extends` используются для того, чтобы указать, что тип-документ должен быть подтипом другого типа. Например: `function merge<T extends object, U extends object>(obj1: T, obj2: U): T & U { return { ...obj1, ...obj2 }; }`."
  },
  25: {
    "question": "Как применять дженерики в интерфейсах и типах?",
    "answer": "Дженерики можно использовать в интерфейсах и типах так же, как и в функциях. Например, интерфейс с дженериками: `interface Box<T> { value: T; }`. Тип с дженериками: `type Pair<T, U> = { first: T; second: U; };`."
  },
  26: {
    "question": "Как работает keyof в TypeScript?",
    "answer": "Оператор `keyof` используется для извлечения типа всех ключей объекта. Например, для объекта `{ name: string, age: number }` тип `keyof typeof obj` будет равен `'name' | 'age'`."
  },
  27: {
    "question": "Как сделать дженерик с параметром по умолчанию?",
    "answer": "Можно задать значение по умолчанию для дженерика, используя `=`, например: `function identity<T = string>(arg: T): T { return arg; }`. В данном случае, если не передан параметр типа, он будет по умолчанию `string`."
  },
  28: {
    "question": "Можно ли ограничить тип дженерика несколькими интерфейсами?",
    "answer": "Да, это можно сделать с помощью пересечения типов. Например: `function combine<T extends A & B>(arg: T): T { return arg; }`, где `A` и `B` — это интерфейсы, и `T` ограничен их пересечением."
  },
  29: {
    "question": "Как создать обобщённый класс с дженериками?",
    "answer": "Обобщённый класс создаётся с использованием дженериков в его определении: `class Box<T> { value: T; constructor(value: T) { this.value = value; } }`. Здесь `T` — это тип, который будет подставлен при создании экземпляра класса."
  },
  30: {
    "question": "Как TypeScript выводит тип дженерика по переданным данным?",
    "answer": "TypeScript автоматически выводит тип дженерика на основе переданных значений. Например, для вызова функции `identity(5)` TypeScript выведет тип `T` как `number`."
  },
  31: {
    "question": "Что такое union-тип (|) в TypeScript?",
    "answer": "Union-тип (с помощью оператора `|`) позволяет переменной принимать значения нескольких типов. Например, `let value: string | number;` позволяет переменной `value` быть как строкой, так и числом."
  },
  32: {
    "question": "Что такое intersection-тип (&) в TypeScript?",
    "answer": "Intersection-тип (с помощью оператора `&`) позволяет создать тип, который объединяет несколько типов. Например, `type A = { name: string }; type B = { age: number }; type C = A & B;` создаст тип, который содержит и свойства `name`, и `age`."
  },
  33: {
    "question": "Как работает typeof в TypeScript?",
    "answer": "Оператор `typeof` используется для извлечения типа переменной или выражения. Например, `let num: number = 5; let str: typeof num;` в этом случае `str` будет иметь тип `number`."
  },
  34: {
    "question": "Как работает as для приведения типов?",
    "answer": "Оператор `as` используется для явного приведения типов. Например, если у вас есть `let value: any = 'hello'; let str = value as string;`, то вы приводите переменную `value` к типу `string`."
  },
  35: {
    "question": "Что такое keyof и как его использовать?",
    "answer": "`keyof` используется для извлечения типа всех ключей объекта. Например, `type Person = { name: string; age: number; }; type PersonKeys = keyof Person;` тип `PersonKeys` будет равен `'name' | 'age'`."
  },
  36: {
    "question": "Как работает in в TypeScript?",
    "answer": "Оператор `in` используется для проверки наличия свойства в объекте или для работы с типами, где проверяется, какой тип присваивается переменной. Например, `if ('name' in person) { ... }`."
  },
  37: {
    "question": "Что делают Partial<T>, Required<T>, Readonly<T>?",
    "answer": "Эти утилиты работают с типами: `Partial<T>` делает все свойства типа `T` необязательными, `Required<T>` — обязательными, а `Readonly<T>` делает все свойства типа `T` только для чтения."
  },
  38: {
    "question": "Как Pick<T, K> отличается от Omit<T, K>?",
    "answer": "`Pick<T, K>` создает новый тип с выбранными свойствами из типа `T` (по ключам `K`), а `Omit<T, K>` создает тип, исключающий эти свойства."
  },
  39: {
    "question": "Что делает Record<K, T>?",
    "answer": "`Record<K, T>` создает тип, где `K` — это тип ключей, а `T` — тип значений для этих ключей. Например, `Record<string, number>` создаст тип, где ключи — строки, а значения — числа."
  },
  40: {
    "question": "Как работает ReturnType<T>?",
    "answer": "`ReturnType<T>` — это утилита, которая извлекает тип возвращаемого значения функции типа `T`. Например, если есть функция `function add(a: number, b: number) { return a + b; }`, то `ReturnType<typeof add>` будет `number`."
  },
  41: {
    "question": "Как объявить класс в TypeScript?",
    "answer": "Класс в TypeScript объявляется аналогично JavaScript, с добавлением типов для свойств и методов: `class Person { name: string; constructor(name: string) { this.name = name; } }`."
  },
  42: {
    "question": "Какие модификаторы доступа есть в TypeScript? (public, private, protected)",
    "answer": "В TypeScript есть три модификатора доступа: `public` (по умолчанию, доступен везде), `private` (доступен только внутри класса), `protected` (доступен внутри класса и его наследников)."
  },
  43: {
    "question": "Как задать класс, который нельзя наследовать?",
    "answer": "Чтобы класс нельзя было наследовать, нужно использовать ключевое слово `final` (оно не поддерживается напрямую в TypeScript), но можно применить подход с `Object.freeze()`, что предотвращает модификацию прототипа, хотя это не является полным запретом на наследование."
  },
  44: {
    "question": "Как сделать абстрактный класс?",
    "answer": "Абстрактный класс в TypeScript создается с использованием ключевого слова `abstract`. Он может содержать абстрактные методы, которые должны быть реализованы в подклассах: `abstract class Animal { abstract sound(): void; }`."
  },
  45: {
    "question": "Как реализовать интерфейс в классе?",
    "answer": "Интерфейс реализуется с помощью ключевого слова `implements`. Класс должен реализовать все методы и свойства, указанные в интерфейсе: `class Dog implements Animal { sound() { console.log('Woof!'); } }`."
  },
  46: {
    "question": "Можно ли указывать тип для this?",
    "answer": "Да, можно указать тип для `this` в методах класса с помощью явного указания типа: `class MyClass { method(this: MyClass) { ... } }`."
  },
  47: {
    "question": "Как работает static в TypeScript?",
    "answer": "Ключевое слово `static` используется для объявления статических свойств и методов класса, которые принадлежат самому классу, а не его экземплярам. Например: `class MyClass { static myMethod() { ... } }`."
  },
  48: {
    "question": "Как работают get и set в TypeScript?",
    "answer": "В TypeScript можно использовать геттеры и сеттеры для управления доступом к свойствам класса. Геттер позволяет получить значение, а сеттер — изменить его. Например: `get fullName() { return `${this.firstName} ${this.lastName}`; }`."
  },
  49: {
    "question": "Можно ли наследоваться сразу от нескольких классов?",
    "answer": "Нет, TypeScript не поддерживает множественное наследование классов. Вместо этого можно использовать интерфейсы для реализации нескольких типов поведения или композицию."
  },
  50: {
    "question": "В чём разница между implements и extends?",
    "answer": "`extends` используется для наследования от класса, т.е. создание нового класса на основе существующего, а `implements` — для реализации интерфейса, т.е. гарантии, что класс будет соответствовать определенному набору методов и свойств."
  },
  51: {
    "question": "Как работает система модулей в TypeScript?",
    "answer": "Система модулей в TypeScript работает с использованием ES6 модулей, где файлы могут быть экспортированы и импортированы. Это позволяет разделять код на независимые части, которые могут быть использованы в других модулях."
  },
  52: {
    "question": "Как настроить tsconfig.json для работы с модулями?",
    "answer": "Для работы с модулями в `tsconfig.json` необходимо указать опцию `module: \"esnext\"` или другой тип модуля, например `commonjs`. Также можно настроить пути и алиасы с помощью `baseUrl` и `paths`."
  },
  53: {
    "question": "Чем import отличается от require?",
    "answer": "`import` — это синтаксис ES6 модулей, который является статическим и поддерживает типизацию. `require` — это синтаксис CommonJS, который является динамическим и не поддерживает типизацию напрямую в TypeScript."
  },
  54: {
    "question": "Как использовать namespace в TypeScript?",
    "answer": "Namespace в TypeScript используется для организации кода и объединения нескольких сущностей в один объект. Например: `namespace MyNamespace { export class MyClass { ... } }`."
  },
  55: {
    "question": "Как работают декларации модулей (declare module)?",
    "answer": "Декларации модулей позволяют TypeScript понимать сторонние библиотеки, для которых нет типов. Например, `declare module 'my-lib' { export function myFunc(): void; }` позволяет указать, что существует модуль с определённым API."
  },
  56: {
    "question": "Как экспортировать несколько значений из модуля?",
    "answer": "Для экспорта нескольких значений используется ключевое слово `export`. Например: `export const a = 5; export function foo() { ... }`."
  },
  57: {
    "question": "В чём разница между export default и именованным экспортом?",
    "answer": "`export default` используется для экспорта одного значения, которое можно импортировать без указания имени, а именованный экспорт (`export { name }`) позволяет экспортировать несколько значений, каждый из которых должен быть импортирован с указанием имени."
  },
  58: {
    "question": "Как подключить сторонние библиотеки с @types?",
    "answer": "Для использования сторонних библиотек с типами нужно установить их типы через `npm install @types/название-библиотеки`. Это позволяет TypeScript распознавать типы библиотеки и работать с ними."
  },
  59: {
    "question": "Как работать с alias-импортами в TypeScript?",
    "answer": "Алиасы можно настроить в `tsconfig.json` с помощью опции `paths`. Например: `\"paths\": { \"@models/*\": [\"src/models/*\"] }`, чтобы использовать импорт как `import { User } from '@models/user';`."
  },
  60: {
    "question": "Как использовать import type?",
    "answer": "`import type` используется для импорта только типов из других модулей, что помогает избежать включения ненужного кода в финальную сборку. Например: `import type { MyType } from './types';`."
  },
  61: {
    "question": "Как типизировать props в функциональном компоненте?",
    "answer": "Props типизируются с использованием дженериков. Например: `const MyComponent: React.FC<{ name: string; age: number }> = ({ name, age }) => { ... }`."
  },
  62: {
    "question": "Как задать дефолтные значения пропсов с TypeScript?",
    "answer": "Для задания дефолтных значений пропсов можно использовать оператор `defaultProps` или задавать дефолтные значения непосредственно в деструктуризации: `const MyComponent = ({ name = 'Default' }: { name?: string }) => { ... }`."
  },
  63: {
    "question": "Как типизировать state в классовом компоненте?",
    "answer": "В классовых компонентах state типизируется с помощью дженериков в `State`: `class MyComponent extends React.Component<{}, { count: number }> { state = { count: 0 }; }`."
  },
  64: {
    "question": "Как типизировать useState?",
    "answer": "Для типизации `useState` используется дженерик. Например: `const [count, setCount] = useState<number>(0);`."
  },
  65: {
    "question": "Как типизировать useReducer?",
    "answer": "Типизировать `useReducer` можно следующим образом: `const [state, dispatch] = useReducer(reducer, initialState);`, где `reducer` и `initialState` имеют соответствующие типы."
  },
  66: {
    "question": "Как описать children в компоненте?",
    "answer": "Тип для `children` можно задать как `ReactNode`, что охватывает все типы, которые могут быть детьми компонента: `const MyComponent: React.FC<{ children: React.ReactNode }> = ({ children }) => { ... }`."
  },
  67: {
    "question": "Как работает React.FC и почему его не рекомендуют использовать?",
    "answer": "React.FC (или React.FunctionComponent) автоматически типизирует props, включая `children`, но его не рекомендуют использовать, так как это может привести к неожиданным типовым конфликтам и избыточной типизации. Лучше типизировать props вручную."
  },
  68: {
    "question": "Как типизировать ref?",
    "answer": "Для типизации `ref` используется `React.RefObject` или `React.forwardRef`. Например: `const inputRef = useRef<HTMLInputElement>(null);`."
  },
  69: {
    "question": "Как типизировать event в обработчике событий?",
    "answer": "Типизация события зависит от типа элемента, к которому оно привязано. Например, для клика по кнопке: `const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => { ... }`."
  },
  70: {
    "question": "Как типизировать forwardRef?",
    "answer": "Для типизации `forwardRef` используется дженерик, который принимает тип props и тип ref. Например: `const MyComponent = React.forwardRef<HTMLInputElement, MyComponentProps>((props, ref) => { ... });`."
  },
  71: {
    "question": "Как типизировать fetch в TypeScript?",
    "answer": "Типизация для `fetch` зависит от структуры возвращаемых данных. Например: `const fetchData = async (): Promise<MyDataType> => { const res = await fetch('/api'); return res.json(); }`."
  },
  72: {
    "question": "Как работает Promise<T>?",
    "answer": "Promise<T> представляет собой объект, который асинхронно возвращает значение типа T. Когда промис выполнен, он может либо вернуть значение типа T, либо выбросить ошибку."
  },
  73: {
    "question": "Как типизировать async/await функции?",
    "answer": "Для типизации асинхронной функции используется `Promise<T>`. Например: `const fetchData = async (): Promise<MyDataType> => { return fetchDataFromApi(); }`."
  },
  74: {
    "question": "Как типизировать axios?",
    "answer": "Для типизации `axios` используется тип `AxiosResponse`. Например: `const response: AxiosResponse<MyDataType> = await axios.get('/api');`."
  },
  75: {
    "question": "Можно ли задать timeout для запроса?",
    "answer": "Да, можно задать таймаут с помощью свойства `timeout` в настройках `axios`: `axios.get('/api', { timeout: 1000 });`."
  },
  76: {
    "question": "Как типизировать WebSockets?",
    "answer": "WebSocket типизируется как `WebSocket` объект. Например: `const socket: WebSocket = new WebSocket('ws://example.com');`."
  },
  77: {
    "question": "Как работать с AbortController в TypeScript?",
    "answer": "Для работы с `AbortController` создается экземпляр с типом `AbortController`. Например: `const controller = new AbortController(); fetch('/api', { signal: controller.signal });`."
  },
  78: {
    "question": "Как типизировать setTimeout и setInterval?",
    "answer": "Для `setTimeout` и `setInterval` можно использовать тип `NodeJS.Timeout` в Node.js или `number` в браузере. Например: `const timer: NodeJS.Timeout = setTimeout(() => { ... }, 1000);`."
  },
  79: {
    "question": "Как правильно обработать ошибки в try/catch?",
    "answer": "Ошибки в `try/catch` обрабатываются с типизацией через `unknown`, чтобы обеспечить проверку типа ошибки. Например: `try { ... } catch (error: unknown) { if (error instanceof Error) { console.error(error.message); } }`."
  },
  80: {
    "question": "Чем any отличается от unknown в обработке API-ответов?",
    "answer": "`any` позволяет использовать значение без проверки типа, в то время как `unknown` требует явной проверки типа перед использованием, что делает его более безопасным в контексте обработки ошибок или данных."
  },
  81: {
    "question": "Как типизировать useSelector в Redux Toolkit?",
    "answer": "Для типизации `useSelector` необходимо указать тип состояния, используя `RootState`. Пример: `const value = useSelector((state: RootState) => state.someValue);`."
  },
  82: {
    "question": "Как типизировать useDispatch?",
    "answer": "Для типизации `useDispatch` используйте тип `AppDispatch`, определённый в вашем store. Пример: `const dispatch = useDispatch<AppDispatch>();`."
  },
  83: {
    "question": "Как типизировать createSlice?",
    "answer": "Для типизации `createSlice` нужно указать типы для `initialState` и редьюсеров. Пример: `const slice = createSlice({ name: 'example', initialState: { count: 0 } as { count: number }, reducers: { increment(state) { state.count += 1; } } });`."
  },
  84: {
    "question": "Как описать глобальный стейт в Redux?",
    "answer": "Глобальный стейт описывается через `RootState`, который типизируется с помощью `combineReducers`. Пример: `const rootReducer = combineReducers({ user: userReducer }); type RootState = ReturnType<typeof rootReducer>;`."
  },
  85: {
    "question": "Как типизировать middleware в Redux?",
    "answer": "Типизация middleware в Redux зависит от используемой библиотеки, но обычно типизируется как функция, принимающая `store` и `next`. Пример: `const customMiddleware: Middleware = store => next => action => { ... }`."
  },
  86: {
    "question": "Как типизировать RTK Query?",
    "answer": "RTK Query типизируется через создание API-сервисов с использованием `createApi`. Пример: `const api = createApi({ reducerPath: 'api', baseQuery: fetchBaseQuery({ baseUrl: '/api' }), endpoints: (builder) => ({ getUsers: builder.query<User[], void>({ query: () => 'users' }) }) });`."
  },
  87: {
    "question": "Можно ли типизировать Zustand?",
    "answer": "Да, Zustand можно типизировать, используя типы для состояния. Пример: `const useStore = create<Store>((set) => ({ count: 0, increase: () => set((state) => ({ count: state.count + 1 })) }));`."
  },
  88: {
    "question": "Как типизировать createStore?",
    "answer": "Типизация `createStore` зависит от используемой библиотеки, но обычно вы указываете тип состояния и экшенов. Пример для Redux: `const store = createStore(reducer, initialState); type Store = typeof store.getState;`."
  },
  89: {
    "question": "Как типизировать экшены в Redux?",
    "answer": "Типизация экшенов в Redux зависит от используемой библиотеки. Например, для Redux Toolkit экшены можно типизировать с помощью `createSlice`: `const slice = createSlice({ name: 'example', initialState, reducers: { setValue(state, action: PayloadAction<string>) { state.value = action.payload; } } });`."
  },
  90: {
    "question": "Можно ли использовать immer с TypeScript?",
    "answer": "Да, можно использовать `immer` с TypeScript, так как Redux Toolkit включает `immer` по умолчанию, и типизация будет работать автоматически, обеспечивая иммутабельность данных."
  },
  91: {
    "question": "Какие основные флаги есть в tsconfig.json?",
    "answer": "Основные флаги включают: `strict`, `target`, `module`, `lib`, `esModuleInterop`, `noImplicitAny`, `outDir`, `rootDir`, и другие. Эти флаги конфигурируют поведение компилятора и поддержку различных ECMAScript функций."
  },
  92: {
    "question": "Что делает strict в TypeScript?",
    "answer": "`strict` включает все строгие проверки в TypeScript, такие как `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`, и другие, которые помогают улучшить безопасность типов и предотвратить потенциальные ошибки."
  },
  93: {
    "question": "Как работает noImplicitAny?",
    "answer": "Флаг `noImplicitAny` запрещает неявное использование типа `any`. Если переменная или параметр не имеют явно указанного типа, TypeScript выдаст ошибку."
  },
  94: {
    "question": "Как включить strictNullChecks и зачем он нужен?",
    "answer": "`strictNullChecks` включается в `tsconfig.json` и предотвращает присваивание `null` и `undefined` переменным, которые не имеют этих значений в своем типе."
  },
  95: {
    "question": "Как настроить поддержку ESModules?",
    "answer": "Для поддержки ESModules в `tsconfig.json` нужно указать `module: 'ESNext'` и `moduleResolution: 'node'`. Также потребуется использовать `.mjs` или `.ts` файлы и использовать `import`/`export`."
  },
  96: {
    "question": "Что делает paths в tsconfig.json?",
    "answer": "Флаг `paths` в `tsconfig.json` позволяет настраивать алиасы для путей, чтобы использовать более короткие и удобные пути при импорте модулей. Пример: `paths: { '@components/*': ['src/components/*'] }`."
  },
  97: {
    "question": "Как настроить tsconfig для фронтенда и бэкенда?",
    "answer": "Для фронтенда и бэкенда можно настроить два отдельных файла `tsconfig.json`, где для фронтенда укажете `module: 'ESNext'` и для бэкенда — `module: 'CommonJS'`. Также можно использовать `extends` для общего конфигурационного файла."
  },
  98: {
    "question": "Как настроить алиасы для путей?",
    "answer": "Для настройки алиасов в `tsconfig.json` нужно использовать свойство `paths`, например: `paths: { '@src/*': ['src/*'] }`. Это позволяет использовать такие пути как `import { SomeComponent } from '@src/components';`."
  },
  99: {
    "question": "Как транспилировать TypeScript в JavaScript?",
    "answer": "Для транспиляции TypeScript в JavaScript используйте команду `tsc`, которая скомпилирует файлы, указанные в `tsconfig.json`. Для одноразовой компиляции можно выполнить `tsc --project tsconfig.json`."
  },
  100: {
    "question": "Как работать с declaration файлом (.d.ts)?",
    "answer": "Файлы `.d.ts` используются для описания типов для существующих JavaScript библиотек. В них можно указать интерфейсы, типы и декларации, чтобы предоставить TypeScript информацию о типах, которые не включены в исходный код."
  },
  "total": 100
}