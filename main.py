from flask import Flask
import json
import utils

app = Flask(__name__)
candidates = utils.load_candidates()

#assert (False)

@app.route("/")
def page_index():
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate ['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += '</pre>'
    return str_candidates


@app.route("/canndidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidates = f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    return str_candidates


@app.route("/skills/<skill>")
def skills(skill):
    str_candidates = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"

    str_candidates += '</pre>'
    return str_candidates
skills('python')

app.run(debug=True)

# candidates = utils.load_candidates()
# str_candidates = '<pre>'
# for candidate in candidates.values():
#     str_candidates += f"{candidate ['name']} \n {candidate['position']} \n {candidate['skills']}\n\n"
# str_candidates += '</pre>'
# print(str_candidates)

# <рге>
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# <рге>