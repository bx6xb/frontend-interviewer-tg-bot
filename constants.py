from questions.html import html_questions
from questions.css import css_questions
from questions.js import js_questions
from questions.ts import ts_questions
from questions.react import react_questions
from questions.redux import redux_questions
from questions.next import next_questions
from questions.web import web_questions
from questions.general import general_questions

HTML = 'HTML'
CSS = 'CSS'
JS = 'JavaScript'
TS = 'TypeScript'
REACT = 'React'
REDUX = 'Redux'
NEXT = 'Next'
WEB = 'Web'
GENERAL = 'Общие вопросы'
QUESTIONS_LIST = [HTML, CSS, JS, TS, REACT, REDUX, NEXT, WEB, GENERAL]
CATEGORIES = {
  HTML: html_questions,
  CSS: css_questions,
  JS: js_questions,
  TS: ts_questions,
  REACT: react_questions,
  REDUX: redux_questions,
  NEXT: next_questions,
  WEB: web_questions,
  GENERAL: general_questions,
}