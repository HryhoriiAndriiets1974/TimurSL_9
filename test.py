# test.py

from objects import Question, Answer, TestEndData

def getResults():
    # get most scored programming language
    max_score = 0
    scored_language = ""
    for language, lang_score in scores.items():
        if lang_score > max_score:
            max_score = lang_score
            scored_language = language

    return programming_languages[scored_language if scored_language else "Error"]


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

    "Unity": TestEndData(
        title="Unity Developer",
        desc="You are a Unity Developer!",
        image="path/to/unity_developer_image.png"
    ),

    "SQL": TestEndData(
        title="SQL Developer",
        desc="You are a SQL Developer!",
        image="path/to/sql_developer_image.png"
    ),

    "Kotlin": TestEndData(
        title="Kotlin Developer",
        desc="You are a Kotlin Developer!",
        image="path/to/kotlin_developer_image.png"
    ),

    "Unreal": TestEndData(
        title="Unreal Developer",
        desc="You are a Unreal Developer!",
        image="path/to/unreal_developer_image.png"
    ),

    "Rust": TestEndData(
        title="Rust Developer",
        desc="You are a Rust Developer!",
        image="path/to/rust_developer_image.png"
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
    "Swift": 0,
    "Unity": 0,
    "SQL": 0,
    "Kotlin": 0,
    "Unreal": 0,
    "Rust": 0,
}

def initialize_scores():
    for language in scores:
        scores[language] = 0


def score(lang):
    print(f"Scored {lang}")
    scores[lang] += 1

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
                                    Answer("Створювати анімацію", lambda: score("CSS")),
                                    Answer("Розробляти інтерактивні елементи", lambda: score("HTML")),
                                    Answer("Оптимізувати сайт", lambda: score("JavaScript")),
                                    Answer("Розробляти бекенд", lambda: score("PHP")),
                                ]
                            )
                        ),
                        Answer("Розробка мобільних додатків", None, next_question=
                            Question(
                                title="Якій платформі ти віддаєш перевагу?",
                                image="path/to/image4.png",
                                answers=[
                                    Answer("Android", lambda: score("Java")),
                                    Answer("iOS", lambda: score("Swift"))
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
                                Answer("Ігри на ПК", None, next_question=
                                    Question(
                                        title="Які ігри ти віддаєш перевагу?",
                                        image="path/to/image5.png",
                                        answers=[
                                            Answer("Ігри з відкритим світом", lambda: score("Unreal")),
                                            Answer("Ігри з глибоким сюжетом", lambda: score("Unreal")),
                                            Answer("Інді-ігри", lambda: score("Unity")),
                                            Answer("Ігри на вдачу", lambda: score("Python"))
                                        ]
                                    )
                                ),
                                Answer("Ігри на смартфоні", None, next_question=
                                       Question(
                                            title="Які ігри ти віддаєш перевагу?",
                                            image="path/to/image5.png",
                                            answers=[
                                                Answer("Пазли", lambda: score("JavaScript")),
                                                Answer("Простi, такi як Subway Surfers", lambda: score("Unity")),
                                                Answer("Складні, такі як PUBG", lambda: score("Unreal")),
                                            ]
                                       )
                                ),
                                Answer("Ігри в браузері", lambda: score("JavaScript"))
                            ]
                   )
            ),
            Answer("Вчити нові технології", None, next_question=
                   Question(
                            title="Які технології тебе цікавлять?",
                            image="path/to/image6.png",
                            answers=[
                                Answer("Машинне навчання", lambda: score("Python")),
                                Answer("Розробка ігор", lambda: score("C++")),
                                Answer("Розробка веб-сайтів", lambda: score("JavaScript")),
                                Answer("Розробка мобільних додатків", lambda: score("Java")),
                            ]
                    )
            ),
        ]
    )
    return [q1]

