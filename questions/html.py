html_questions = {
  1: {
    "question": "Что такое HTML и какова его основная роль в веб-разработке?",
    "answer": "HTML - язык гипертекстовой разметки, с его помощью пишется структура сайта."
  },
  2: {
    "question": "Какова структура HTML-документа? Какие обязательные теги он должен содержать?",
    "answer": "<!DOCTYPE html> указывает на версию HTML5. <html> — корневой элемент. <head> содержит метаинформацию. <body> содержит контент страницы."
  },
  3: {
    "question": "В чём разница между <div> и <span>?",
    "answer": "<div> - блочный элемент, используется для оборачивания блока контента, <span> - строчный, используется для выделения части текста."
  },
  4: {
    "question": "Какие бывают семантические теги в HTML и зачем их использовать?",
    "answer": "Семантические теги - header, footer, p, nav, aside, article, section, main. Нужны для SEO и общей читаемости кода."
  },
  5: {
    "question": "Как работает <meta charset=\"UTF-8\"> и почему он важен?",
    "answer": "Этот тег устанавливает кодировку страницы в UTF-8, что позволяет корректно отображать символы разных языков. Без него возможны проблемы с кодировкой."
  },
  6: {
    "question": "Какие атрибуты можно использовать с тегом <img>?",
    "answer": "Основные атрибуты: src (путь к изображению), alt (альтернативный текст), width и height (размеры), loading (ленивая загрузка), title (подсказка при наведении)."
  },
  7: {
    "question": "В чём разница между id и class?",
    "answer": "Id может быть один на странице, также имеет большую специфичность (100). Class можно использовать для нескольких элементов, его специфичность - 10."
  },
  8: {
    "question": "Чем section отличается от article?",
    "answer": "<section> - это логическая секция страницы, объединяющая связанные элементы. <article> - автономный блок контента, который может существовать отдельно, например, статья или пост."
  },
  9: {
    "question": "Что такое alt у изображения и зачем он нужен?",
    "answer": "Alt - атрибут тега <img>, отображается вместо картинки, если та не загрузилась, участвует в SEO."
  },
  10: {
    "question": "Как работает <iframe>? Какие у него есть плюсы и минусы?",
    "answer": "<iframe> встраивает другую веб-страницу внутрь текущей. Плюсы: возможность встраивания внешнего контента. Минусы: проблемы с безопасностью, ухудшение производительности, сложности с адаптивностью."
  },
  11: {
    "question": "Какие основные теги используются для создания формы?",
    "answer": "Основные теги для создания формы: <form>, <input>, <label>, <textarea>, <select>, <option>, <button>, <fieldset>, <legend>, <datalist>, <optgroup>."
  },
  12: {
    "question": "Как работает <label> и зачем его использовать?",
    "answer": "Тег <label> связывает метку с элементом формы, улучшая доступность и позволяя пользователю кликать по метке для фокуса на соответствующем поле. Он используется для улучшения взаимодействия с формами."
  },
  13: {
    "question": "Чем <button> отличается от <input type=\"submit\">?",
    "answer": "<button> является более гибким элементом, позволяющим использовать HTML и CSS для стилизации, а также поддерживает динамический контент, например, изображения. <input type=\"submit\"> ограничен только текстом."
  },
  14: {
    "question": "Какие бывают типы полей ввода (<input type=\"...\")?",
    "answer": "Некоторые типы полей ввода: checkbox (квадрат с галочкой), radio (кружок), range (выбор значения на отрезке), button (кнопка), date (выбор даты), color (выбор цвета), number (число), email (почта), tel (телефон), file (файл), url (ссылка), time (время)."
  },
  15: {
    "question": "Как работает required в форме?",
    "answer": "Атрибут required в форме не позволяет отправить форму, пока поле не будет заполнено валидным значением."
  },
  16: {
    "question": "Чем placeholder отличается от value?",
    "answer": "Placeholder — это текст, который отображается в поле ввода, пока оно пустое, в качестве подсказки пользователю. Value — это текущее значение, введенное пользователем в поле ввода."
  },
  17: {
    "question": "Как отправить данные формы без перезагрузки страницы?",
    "answer": "Чтобы отправить данные формы без перезагрузки страницы, нужно вызвать метод event.preventDefault() в событии onSubmit, чтобы отменить стандартное поведение формы."
  },
  18: {
    "question": "Какие способы валидации форм существуют в HTML?",
    "answer": "В HTML доступны встроенные способы валидации с использованием атрибутов, таких как required, pattern, min, max, type (например, email, number), а также можно использовать JavaScript для дополнительной валидации."
  },
  19: {
    "question": "Как работает <fieldset> и <legend>?",
    "answer": "Тег <fieldset> используется для группировки элементов формы, а тег <legend> задает заголовок для этой группы, улучшая структуру и доступность формы."
  },
  20: {
    "question": "Что делает атрибут autocomplete в <input>?",
    "answer": "Атрибут autocomplete в <input> позволяет браузеру автоматически заполнять поле на основе ранее введенных данных, улучшая удобство ввода для пользователя."
  },
  21: {
    "question": "Чем href=\"#\" отличается от href=\"/\"?",
    "answer": "href=\"#\" указывает на текущую страницу и используется для якорей или для предотвращения перехода по ссылке, тогда как href=\"/\" указывает на корень сайта и ведет на главную страницу."
  },
  22: {
    "question": "Как открыть ссылку в новой вкладке?",
    "answer": "Чтобы открыть ссылку в новой вкладке, нужно добавить атрибут target=\"_blank\"."
  },
  23: {
    "question": "Как сделать ссылку, которая звонит по номеру телефона?",
    "answer": "Для того чтобы ссылка инициировала звонок, нужно указать href=\"tel:\" и добавить номер телефона."
  },
  24: {
    "question": "Чем <a> отличается от <button> с onClick?",
    "answer": "Тег <a> используется для навигации, и его можно использовать с href для перехода на другой ресурс. <button> предназначен для выполнения действий, например, при обработке событий, и не связан напрямую с переходами."
  },
  25: {
    "question": "Что делает атрибут download в <a>?",
    "answer": "Атрибут download в теге <a> позволяет скачать файл, на который ссылается ссылка, вместо того чтобы переходить по ней."
  },
  26: {
    "question": "Как вставить видео в HTML?",
    "answer": "Для вставки видео в HTML используется тег <video>, который позволяет вставлять видеофайлы на страницу с возможностью управления воспроизведением."
  },
  27: {
    "question": "Чем <audio> отличается от <video>?",
    "answer": "Тег <audio> предназначен для вставки аудиофайлов, а тег <video> используется для встраивания видеоконтента. Оба тега поддерживают элементы управления воспроизведением."
  },
  28: {
    "question": "Как встроить PDF-документ на страницу?",
    "answer": "Для встраивания PDF-документа на страницу можно использовать тег <embed> или <iframe> с указанием пути к PDF-файлу."
  },
  29: {
    "question": "Как сделать адаптивное изображение без CSS?",
    "answer": "Для адаптивного изображения без CSS можно использовать атрибуты width и height в теге <img> с процентными значениями, или применить тег <picture> для загрузки разных изображений в зависимости от устройства."
  },
  30: {
    "question": "Чем <picture> полезен для адаптивной загрузки изображений?",
    "answer": "Тег <picture> позволяет загружать разные версии изображения в зависимости от условий, таких как размер экрана или плотность пикселей, что делает страницу более адаптивной и эффективной по загрузке."
  },
  31: {
    "question": "Какой атрибут <meta> отвечает за адаптивность страницы?",
    "answer": "Атрибут <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> используется для настройки адаптивности страницы на мобильных устройствах."
  },
  32: {
    "question": "Как сделать редирект через <meta>?",
    "answer": "Для редиректа через <meta> используется тег <meta http-equiv=\"refresh\" content=\"5;url=https://example.com\">, где content указывает время в секундах и URL для перенаправления."
  },
  33: {
    "question": "Как запретить индексирование страницы поисковиками?",
    "answer": "Чтобы запретить индексирование страницы, можно добавить тег <meta name=\"robots\" content=\"noindex, nofollow\"> в <head>."
  },
  34: {
    "question": "Какие meta-теги помогают улучшить SEO?",
    "answer": "Для улучшения SEO полезны meta-теги, такие как <meta name=\"description\" content=\"...\">, <meta name=\"keywords\" content=\"...\"> и Open Graph метатеги для социальных сетей."
  },
  35: {
    "question": "Как работает Open Graph (OG-теги)?",
    "answer": "Open Graph (OG) теги позволяют управлять тем, как содержимое страницы отображается при его распространении в социальных сетях, улучшая видимость и привлекательность ссылки."
  },
  36: {
    "question": "Что такое data- атрибуты и как их использовать?",
    "answer": "Data-атрибуты используются для хранения нестандартных данных в HTML-элементах. Они начинаются с \"data-\" и могут быть использованы для передачи информации в JavaScript."
  },
  37: {
    "question": "Как работает contenteditable?",
    "answer": "Атрибут contenteditable позволяет сделать содержимое HTML-элемента редактируемым пользователем прямо в браузере."
  },
  38: {
    "question": "Как создать кастомный атрибут в HTML?",
    "answer": "Для создания кастомного атрибута в HTML используется префикс \"data-\", например, data-user-id=\"123\"."
  },
  39: {
    "question": "Как работает localStorage и sessionStorage?",
    "answer": "localStorage и sessionStorage предоставляют способ хранения данных в браузере. localStorage сохраняет данные на постоянной основе, а sessionStorage — только на время сессии пользователя."
  },
  40: {
    "question": "В чём разница между Canvas API и SVG?",
    "answer": "Canvas API предоставляет программный интерфейс для рисования изображений на холсте с помощью JavaScript, в то время как SVG использует XML-разметку для создания и отображения векторной графики."
  },
  41: {
    "question": "Как улучшить доступность сайта с помощью HTML?",
    "answer": "Для улучшения доступности можно использовать семантические теги (например, <header>, <footer>, <main>), правильно оформлять формы, добавлять альтернативный текст для изображений с помощью атрибута alt, а также использовать ARIA-атрибуты."
  },
  42: {
    "question": "Какие атрибуты помогают пользователям с ограниченными возможностями?",
    "answer": "Атрибуты, такие как aria-label, aria-describedby, aria-hidden и role, помогают улучшить доступность для пользователей с ограниченными возможностями, предоставляя описание элементов и их состояния."
  },
  43: {
    "question": "Как работает tabindex и зачем он нужен?",
    "answer": "Атрибут tabindex управляет порядком фокусировки элементов на странице при навигации с помощью клавиши Tab. Он помогает сделать интерфейс более доступным для пользователей с ограниченными возможностями."
  },
  44: {
    "question": "Как aria-label влияет на читателей экрана?",
    "answer": "Атрибут aria-label предоставляет текстовое описание для элемента, который не имеет видимого текста, помогая пользователям с нарушениями зрения понять его назначение при использовании экранного чтеца."
  },
  45: {
    "question": "Чем <button> лучше <div> для кликабельных элементов?",
    "answer": "<button> является семантически правильным элементом для кликабельных элементов, так как он предоставляет доступность, например, поддержку фокуса и событий для клавиатуры, в отличие от <div>, который требует дополнительной обработки."
  },
  46: {
    "question": "Как уменьшить время загрузки HTML-страницы?",
    "answer": "Для уменьшения времени загрузки можно минимизировать HTML-код, использовать асинхронную загрузку скриптов, сжимать изображения и применять кэширование ресурсов."
  },
  47: {
    "question": "В чём разница между defer и async для <script>?",
    "answer": "Атрибут defer откладывает выполнение скрипта до завершения загрузки HTML-документа, а async загружает и выполняет скрипт асинхронно, не ожидая загрузки страницы."
  },
  48: {
    "question": "Как работает lazy loading для изображений?",
    "answer": "Lazy loading позволяет загружать изображения только тогда, когда они становятся видимыми на экране, что ускоряет начальную загрузку страницы и экономит трафик."
  },
  49: {
    "question": "Что делает атрибут preload?",
    "answer": "Атрибут preload указывает браузеру заранее загрузить ресурсы, такие как изображения или шрифты, что улучшает производительность, позволяя быстро отображать контент."
  },
  50: {
    "question": "Чем <noscript> полезен?",
    "answer": "Тег <noscript> используется для отображения содержимого, когда JavaScript отключен в браузере, обеспечивая альтернативный контент для пользователей с отключенным скриптами или браузеров, не поддерживающих JavaScript."
  },
  51: {
    "question": "Что такое semantic HTML?",
    "answer": "Semantic HTML использует теги, которые имеют явное значение, например, <article>, <section>, <header>, <footer>, что улучшает доступность и SEO."
  },
  52: {
    "question": "Как работает <meta name='description'> и зачем он нужен?",
    "answer": "Тег <meta name='description'> содержит описание страницы, которое отображается в поисковых системах, улучшая SEO и повышая привлекательность страницы для пользователей."
  },
  53: {
    "question": "Как использовать теги <strong> и <em>?",
    "answer": "<strong> выделяет важность текста, обычно отображается жирным, а <em> используется для выделения текста курсивом, обозначая эмфазу."
  },
  54: {
    "question": "Что такое <mark> и как его использовать?",
    "answer": "<mark> используется для выделения текста, который будет подсвечен, например, при поиске, чтобы подчеркнуть важность или релевантность."
  },
  55: {
    "question": "Чем отличается <ol> от <ul>?",
    "answer": "<ol> представляет собой упорядоченный список с нумерацией, а <ul> — неупорядоченный список с маркерами."
  },
  56: {
    "question": "Как добавить таблицу в HTML?",
    "answer": "Таблицу можно добавить с помощью тегов <table>, <tr> для строк, <td> для ячеек и <th> для заголовков."
  },
  57: {
    "question": "Что такое <blockquote> и когда его использовать?",
    "answer": "<blockquote> используется для выделения цитат, обычно отображается с отступом для обозначения заимствованного текста."
  },
  58: {
    "question": "Как задать шрифт в HTML?",
    "answer": "Шрифт можно задать с помощью тега <style> или внешнего CSS-файла, используя свойство font-family."
  },
  59: {
    "question": "Как сделать ссылку на внешний файл в HTML?",
    "answer": "Ссылку на внешний файл можно сделать с помощью тега <a href='URL'>, где URL указывает на файл, например, <a href='https://example.com'>."
  },
  60: {
    "question": "Как работает атрибут target в <a>?",
    "answer": "Атрибут target указывает, как будет открыта ссылка: _blank — в новой вкладке, _self — в той же вкладке."
  },
  61: {
    "question": "Что такое <nav> и когда его следует использовать?",
    "answer": "<nav> используется для группировки навигационных ссылок на странице, что помогает улучшить структуру и доступность сайта."
  },
  62: {
    "question": "Как работает атрибут href с якорем?",
    "answer": "Атрибут href с якорем (#) позволяет прокручивать страницу до элемента с указанным id, например, <a href='#section1'>."
  },
  63: {
    "question": "Что такое <em> и как его использовать?",
    "answer": "<em> используется для выделения текста с добавлением акцента или эмоциональной нагрузки, обычно отображается курсивом."
  },
  64: {
    "question": "Какие существуют атрибуты для тега <input>?",
    "answer": "Тег <input> может иметь такие атрибуты, как type (определяет тип поля), value (значение), placeholder (подсказка), required (обязательное поле) и другие."
  },
  65: {
    "question": "Что такое <label> и как его использовать?",
    "answer": "<label> используется для создания метки для элементов формы, улучшая доступность и удобство взаимодействия с пользователем."
  },
  66: {
    "question": "Что делает атрибут placeholder в <input>?",
    "answer": "Атрибут placeholder предоставляет подсказку для пользователя, показывая текст, который исчезает, когда он начинает вводить значение."
  },
  67: {
    "question": "Как работает атрибут <input type='file'>?",
    "answer": "Атрибут <input type='file'> позволяет пользователю выбрать файл с локального устройства для отправки через форму."
  },
  68: {
    "question": "Как задать высоту и ширину изображения в HTML?",
    "answer": "Для задания размеров изображения используют атрибуты width и height в теге <img>, например, <img src='image.jpg' width='500' height='300'>."
  },
  69: {
    "question": "Как вставить картинку в HTML?",
    "answer": "Изображение вставляется с помощью тега <img>, указывая путь к файлу в атрибуте src, например, <img src='image.jpg' alt='description'>."
  },
  70: {
    "question": "Что такое <code> и как его использовать?",
    "answer": "<code> используется для отображения фрагментов кода, обычно отображается моноширинным шрифтом."
  },
  71: {
    "question": "Как работает атрибут action в форме?",
    "answer": "Атрибут action указывает URL, на который будет отправлена форма при её отправке. Это может быть адрес сервера или скрипт для обработки данных."
  },
  72: {
    "question": "Что такое <header> и как его использовать?",
    "answer": "<header> используется для обозначения верхней части страницы или секции, обычно содержащей логотип, навигацию и заголовки."
  },
  73: {
    "question": "Как работает <meta name='viewport'>?",
    "answer": "Атрибут <meta name='viewport'> помогает управлять масштабированием и видимой областью страницы на мобильных устройствах, улучшая адаптивность."
  },
  74: {
    "question": "Что такое <footer> и где его обычно используют?",
    "answer": "<footer> используется для добавления нижней части страницы или секции, где обычно размещается информация о правах, контактные данные или ссылки."
  },
  75: {
    "question": "Как работает атрибут target='_blank'?",
    "answer": "Атрибут target='_blank' открывает ссылку в новой вкладке браузера, что удобно для внешних сайтов или документов."
  },
  "total": 75
}
