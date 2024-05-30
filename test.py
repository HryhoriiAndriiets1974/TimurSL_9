# test.py

from objects import Question, Answer, TestEndData

def getResults():
    # get most scored programming language
    max_score = 0
    max_scored_language = ""
    for language, score in scores.items():
        if score > max_score:
            max_score = score
            max_scored_language = language

    return programming_languages[max_scored_language if max_scored_language else "Error"]


programming_languages = {
    "Python": TestEndData(
        title="Python Developer",
        desc="You are a Python Developer!",
        image="path/to/python_developer_image.png"
    ),

    "Java": TestEndData(
        title="Java Developer",
        desc="You are a Java Developer!",
        image="path/to/java_developer_image.png"
    ),

    "C++": TestEndData(
        title="C++ Developer",
        desc="You are a C++ Developer!",
        image="path/to/cpp_developer_image.png"
    ),

    "JavaScript": TestEndData(
        title="JavaScript Developer",
        desc="You are a JavaScript Developer!",
        image="path/to/js_developer_image.png"
    ),

    "Ruby": TestEndData(
        title="Ruby Developer",
        desc="You are a Ruby Developer!",
        image="path/to/ruby_developer_image.png"
    ),

    "PHP": TestEndData(
        title="PHP Developer",
        desc="You are a PHP Developer!",
        image="path/to/php_developer_image.png"
    ),

    "HTML": TestEndData(
        title="Frontend Developer",
        desc="You are a Frontend Developer with a focus on HTML!",
        image="path/to/frontend_developer_image.png"
    ),

    "CSS": TestEndData(
        title="Frontend Developer",
        desc="You are a Frontend Developer with a focus on CSS!",
        image="path/to/frontend_developer_image.png"
    ),

    "C#": TestEndData(
        title="C# Developer",
        desc="You are a C# Developer!",
        image="path/to/csharp_developer_image.png"
    ),

    "Swift": TestEndData(
        title="Swift Developer",
        desc="You are a Swift Developer!",
        image="path/to/swift_developer_image.png"
    ),

    "Error": TestEndData(
        title="Error",
        desc="An error occurred while processing the test results.",
        image="path/to/error_image.png"
    )


}

scores = {
    "Python": 0,
    "Java": 0,
    "C++": 0,
    "JavaScript": 0,
    "Ruby": 0,
    "PHP": 0,
    "HTML": 0,
    "CSS": 0,
    "C#": 0,
    "Swift": 0
}

def initialize_scores():
    for language in scores:
        scores[language] = 0

def on_python_answer():
    scores["Python"] += 1

def on_java_answer():
    scores["Java"] += 1

def on_cpp_answer():
    scores["C++"] += 1

def on_js_answer():
    scores["JavaScript"] += 1

def on_ruby_answer():
    scores["Ruby"] += 1

def on_php_answer():
    scores["PHP"] += 1

def on_html_answer():
    scores["HTML"] += 1

def on_css_answer():
    scores["CSS"] += 1

def on_cs_answer():
    scores["C#"] += 1

def on_swift_answer():
    scores["Swift"] += 1

def create_test():
    q1 = Question(
        title="Що ти любиш робити у вільний час?",
        image="path/to/image1.png",
        answers=[
            Answer("Програмувати", None, next_question=
                Question(
                    title="Якій з цих задач ти віддаєш перевагу?",
                    image="path/to/image2.png",
                    answers=[
                        Answer("Розробка веб-сайтів", None, next_question=
                            Question(
                                title="Що тобі подобається робити на веб-сайтах?",
                                image="path/to/image3.png",
                                answers=[
                                    Answer("Створювати анімацію", on_css_answer),
                                    Answer("Розробляти інтерактивні елементи", on_html_answer),
                                    Answer("Оптимізувати сайт", on_js_answer),
                                    Answer("Розробляти бекенд", on_php_answer)
                                ]
                            )
                        ),
                        Answer("Розробка мобільних додатків", None, next_question=
                            Question(
                                title="Якій платформі ти віддаєш перевагу?",
                                image="path/to/image4.png",
                                answers=[
                                    Answer("Android", on_java_answer),
                                    Answer("iOS", on_swift_answer)
                                ]
                            )
                        ),
                    ]
                )
            ),
            Answer("Грати в ігри", None, next_question=
                   Question(
                            title="Які ігри ти найчастіше граєш?",
                            image="path/to/image5.png",
                            answers=[
                                Answer("Ігри на ПК", on_cpp_answer, next_question=
                                    Question(
                                        title="Які ігри ти віддаєш перевагу?",
                                        image="path/to/image5.png",
                                        answers=[
                                            Answer("Ігри з відкритим світом", on_cpp_answer),
                                            Answer("Ігри з глибоким сюжетом", on_java_answer),
                                            Answer("Інді-ігри", on_python_answer),
                                            Answer("Ігри на вдачу", on_ruby_answer)
                                        ]
                                    )
                                ),
                                Answer("Ігри на смартфоні", on_java_answer, next_question=
                                       Question(
                                            title="Які ігри ти віддаєш перевагу?",
                                            image="path/to/image5.png",
                                            answers=[
                                                Answer("Пазли", on_js_answer),
                                                Answer("Простi, такi як Subway Surfers", on_cs_answer()),
                                            ]
                                       )
                                ),
                                Answer("Ігри в браузері", on_js_answer)
                            ]
                   )
            ),
            Answer("Вчити нові технології", None, next_question=
                   Question(
                            title="Які технології тебе цікавлять?",
                            image="path/to/image6.png",
                            answers=[
                                Answer("Машинне навчання", on_python_answer),
                                Answer("Розробка ігор", on_cpp_answer),
                                Answer("Розробка веб-сайтів", on_js_answer),
                                Answer("Розробка мобільних додатків", on_ruby_answer)
                            ]
                    )
            ),
        ]
    )
    return [q1]

